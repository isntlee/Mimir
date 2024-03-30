from django.db import models
from abc import ABC, abstractmethod


class ConstraintStrategy(ABC):
    @abstractmethod
    def apply(self, token):
        pass

class AbstractNounStrategy(ConstraintStrategy):
    def apply(self, token):
        abstract_structure = ('acy', 'ncy', 'ence', 'ism', 'ity', 'hood', 'ment', 'ness', 'ship', 'sion', 'phy')
        return token.pos_ == 'NOUN' and token.suffix_ in abstract_structure


CONSTRAINT_CHOICES = {
    1: {
        'name': 'abstract nouns',
        'strategy': AbstractNounStrategy
    },
}

class Constraint(models.Model):
    def __init__(self, strategy):
        self.strategy = strategy

    def __str__(self):
        return self.name

    def apply(self, token):
        return self.strategy.apply(token)
    
    @staticmethod
    def user_choice():
        print("\nWhat interesting words to find:")
        for key, value in CONSTRAINT_CHOICES.items():
            print(f"{key}: {value['name']}")
        user_choice = int(input("\nEnter the number choice here: "))
        if user_choice in CONSTRAINT_CHOICES:
            return CONSTRAINT_CHOICES[user_choice]['strategy']()
        else:
            raise ValueError("Invalid choice")