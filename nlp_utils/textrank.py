import spacy, pytextrank


def textrank(self, text, *args, **kwargs):

    abstract_structure = (
                    'acy', 'ncy', 'ence', 'ism', 'ity', 'hood', 'ment', 'ness', 'ship', 'sion', 'phy'
                    )

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    doc = nlp(text)
    
    abstract_nouns = [tok for tok in doc if tok.pos_ == 'NOUN' and tok.suffix_ in abstract_structure]

    return abstract_nouns