import spacy, pytextrank
from nlp_utils.constraints import Constraint
from apps.words.models import Word


def textrank(self, path, text, *args, **kwargs):

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    doc = nlp(text)


    for sent in doc.sents:
        for token in sent:
            if Constraint.is_abstract_noun(token):
                new_word = Word.create_word(name=token, sentence=sent, document=path, constraint='is_abstract_noun')
                new_word.save()

                print(f"token: {token}")
