import spacy, pytextrank
from spacy.tokens import Token


def textrank(self, text, *args, **kwargs):

    abstract_structure = (
                    'acy', 'ncy', 'ence', 'ism', 'ity', 'hood', 'ment', 'ness', 'ship', 'sion', 'phy'
                    )

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    Token.set_extension("count", default=0)
    Token.set_extension("sentence", default=None)
    doc = nlp(text)

    for sent in doc.sents:
        for token in sent:
            if token.pos_ == 'NOUN' and token.suffix_ in abstract_structure:
                print(f"{token.text}, sentence: {token.i - sent.start}, word_occ: ")


    
    # abstract_nouns = [tok for tok in doc if tok.pos_ == 'NOUN' and tok.suffix_ in abstract_structure]

    # token = abstract_nouns[0]

    # print('\n\n token details', token)
    # print(f"Text: {token.text}\nLemma: {token.lemma_}\nPOS: {token.pos_}\nDep: {token.dep_}\nShape: {token.shape_}\nAlpha: {token.is_alpha}\nStop: {token.is_stop}\nPunct: {token.is_punct}\nSpace: {token.is_space}\nOov: {token.is_oov}\nBracket: {token.is_bracket}\nCurrency: {token.is_currency}\nSent Start: {token.is_sent_start}\nSent End: {token.is_sent_end}")


    # return abstract_nouns