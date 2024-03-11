from django.core.management.base import BaseCommand
from nlp_utils.textrank import textrank
from apps.words.models import Word
import os
import uuid
from django.db.models import Count
import csv


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        base_dir = "data\initial_data"
        doc_paths = [os.path.join(base_dir, filename) for filename in os.listdir(base_dir) if filename.endswith('.txt')] 
        job_id = uuid.uuid4()
        text_objs = []

        for path in doc_paths:
            with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
                text_obj = (path, text, job_id)
                text_objs.append(text_obj)

        textrank(self, text_objs)

        with open('word_frequency.csv', 'w', newline='', encoding='utf-8') as csvfile:
            most_frequent_words = Word.objects.filter(job_id=job_id).values_list('name').annotate(frequency=Count('name')).order_by('-frequency')[:20]
            fieldnames = ['Word Name', 'Frequency', 'Document Source', 'Sentence']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for word in most_frequent_words:
                word_name, word_frequency = word[0], word[1]
                word_list = Word.objects.filter(job_id=job_id).filter(name=word_name)
                rows = [{'Word Name': word_name, 'Frequency': word_frequency}]
                for word in word_list:
                    rows.append({'Document Source': word.document, 'Sentence': word.sentence[:30]})
                writer.writerows(rows)