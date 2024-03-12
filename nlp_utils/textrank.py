import uuid, spacy, pytextrank
from concurrent.futures import ThreadPoolExecutor
from nlp_utils.constraints import Constraint
from apps.words.models import Word

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")


def process_text(path, text, job_id):
    try:
        doc = nlp(text)
        words_to_save = []

        for sent in doc.sents:
            for token in sent:
                method_to_call = Constraint.constraint_methods.get(1)
                if method_to_call[0](token):
                    id = uuid.uuid4()
                    words_to_save.append(Word(id=id, name=token, sentence=sent, document=path, job_id=job_id, constraint=method_to_call[1]))

        Word.objects.bulk_create(words_to_save)
        
    except Exception as e:
        raise(f"Error processing text for job {job_id}: {e}")


def textrank(self, text_objs, *args, **kwargs):
    try:
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = executor.map(lambda obj: process_text(*obj), text_objs)
    except Exception as e:
        raise(f"Error in textrank process: {e}")
