from django.contrib import admin

from blogi.models import Postaus


@admin.register(Postaus)
class PostausAdmin(admin.ModelAdmin):
    list_display = ["otsikko", "kirjoittaja", "luotu", "julkaisuaika"]
    