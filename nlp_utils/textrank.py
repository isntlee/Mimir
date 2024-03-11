import spacy, pytextrank
from nlp_utils.constraints import Constraint
from apps.words.models import Word
from concurrent.futures import ThreadPoolExecutor


nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")


def process_text(path, text):
    doc = nlp(text)
    words_to_save = []

    for sent in doc.sents:
        for token in sent:
            if Constraint.is_abstract_noun(token):
                print('token:', token)
                words_to_save.append(Word(name=token, sentence=sent, document=path, constraint='is_abstract_noun'))
   
    Word.objects.bulk_create(words_to_save)


def textrank(self, text_objs, *args, **kwargs):
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(lambda obj: process_text(*obj), text_objs)

