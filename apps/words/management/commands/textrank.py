from django.core.management.base import BaseCommand
import spacy


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        abstract_structure = (
                        'acy', 'ncy', 'ence', 'ism', 'ity', 'hood', 'ment', 'ness', 'ship', 'sion', 'phy'
                        )

        nlp = spacy.load("en_core_web_sm")
        nlp.add_pipe("textrank")
        
        document_paths = ["data\initial_data\doc1.txt", "data\initial_data\doc2.txt", "data\initial_data\doc3.txt", "data\initial_data\doc4.txt", "data\initial_data\doc5.txt", "data\initial_data\doc6.txt"]
        
        for path in document_paths:
            with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
                doc = nlp(text)
                abstract_nouns = [tok for tok in doc if tok.pos_ == 'NOUN' and tok.suffix_ in abstract_structure]

                print("\n\n\n-Abstract Nouns:", "\n")
                for noun in abstract_nouns:
                    print(noun.text)
