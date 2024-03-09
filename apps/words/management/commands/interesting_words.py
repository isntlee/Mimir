from django.core.management.base import BaseCommand
from nlp_utils.textrank import textrank
import os

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        base_dir = "data/initial_data"
        doc_paths = [os.path.join(base_dir, filename) for filename in os.listdir(base_dir) if filename.endswith('.txt')]
    
        for path in doc_paths:
            with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
                textrank(self, text)
    
                # print("\n\n\n-Abstract Nouns:", "\n")
                # for noun in abstract_nouns:
                #     print(noun.text)
