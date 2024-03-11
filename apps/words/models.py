from django.db import models
import uuid


class Word(models.Model):

    name = models.CharField(max_length=250)
    sentence = models.CharField(max_length=2500)
    document = models.CharField(max_length=250)
    job_id = models.CharField(max_length=250, null=True)
    constraint = models.CharField(max_length=250)
    active = models.BooleanField(default=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):  
        return self.name
    
    @classmethod
    def create_word(cls, name, sentence, document, job_id, constraint, active=True):
        word = cls(id=id, name=name, sentence=sentence, document=document, job_id=job_id, constraint=constraint, active=active)
        return word
