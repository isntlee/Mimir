from django.core.management.base import BaseCommand
from nlp_utils.textrank import textrank
from nlp_utils.zero_shot import zero_shot
import os

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        base_dir = "data\initial_data"
        doc_paths = [os.path.join(base_dir, filename) for filename in os.listdir(base_dir) if filename.endswith('.txt')] 

        text_objs = []
        for path in doc_paths:
            with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
                text_obj = (path, text)
                text_objs.append(text_obj)

        textrank(self, text_objs)