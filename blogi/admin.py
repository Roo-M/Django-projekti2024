from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from blogi.models import Postaus


@admin.register(Postaus)
class PostausAdmin(MarkdownxModelAdmin):
    list_display = ["otsikko", "kirjoittaja", "luotu", "julkaisuaika"]
    