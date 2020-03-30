from modeltranslation.translator import translator, TranslationOptions
from .models import Articles


class ArticlesTranslationOptions(TranslationOptions):
    fields = ('full_description',)


translator.register(Articles, ArticlesTranslationOptions)