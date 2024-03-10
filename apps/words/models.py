from django.db import models


class Word(models.Model):

    name = models.CharField(max_length=250)
    sentence = models.CharField(max_length=2500)
    document = models.CharField(max_length=250)
    constraint = models.CharField(max_length=250)
    active = models.BooleanField(default=True, null=True)
    
    def __str__(self):  
        return self.name
    
    @classmethod
    def create_word(cls, name, sentence, document, constraint, active=True):
        word = cls(name=name, sentence=sentence, document=document, constraint=constraint, active=active)
        return word