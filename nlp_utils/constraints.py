from django.db import models


class Constraint(models.Model):

    @staticmethod
    def is_abstract_noun(token):
        abstract_structure = ('acy', 'ncy', 'ence', 'ism', 'ity', 'hood', 'ment', 'ness', 'ship', 'sion', 'phy')
        return token.pos_ == 'NOUN' and token.suffix_ in abstract_structure

    def __str__(self):
        return self.name
    
    constraint_methods = {
    1 : (is_abstract_noun, 'is_abstract_noun')
    }