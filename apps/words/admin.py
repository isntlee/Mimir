from django.contrib import admin
from .models import Word


class WordAdmin(admin.ModelAdmin): 
    list_display = ['name', 'short_sentence', 'document', 'constraint', 'active']

    def short_sentence(self, obj):
        return obj.sentence[:20] + '...'
    short_sentence.short_description = 'sentence'


admin.site.register(Word, WordAdmin)