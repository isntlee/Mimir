import uuid, spacy, pytextrank
from concurrent.futures import ThreadPoolExecutor
from nlp_utils.constraints import Constraint
from apps.words.models import Word

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")


def process_text(path, text, job_id):
    doc = nlp(text)
    words_to_save = []

    for sent in doc.sents:
        for token in sent:
            if Constraint.is_abstract_noun(token):
                id = uuid.uuid4()
                words_to_save.append(Word(id=id, name=token, sentence=sent, document=path, job_id=job_id, constraint='is_abstract_noun'))

    Word.objects.bulk_create(words_to_save)


def textrank(self, text_objs, *args, **kwargs):
    with ThreadPoolExecutor(max_workers=4) as executor:
       results =  executor.map(lambda obj: process_text(*obj), text_objs)