from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    teksti = models.TextField()

    # Vaihtoehto 1: Älä anna poistaa käyttäjää, jolla on blogipostauksia
    kirjoittaja = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
    )

 # Vaihtoehto 2: Poista myös kaikki käyttäjän blogipostaukset, jos poistetaan käyttäjä
   # kirjoittaja = models.ForeignKey
   # (
    #    settings.AUTH_USER_MODEL,
    #    on_delete=models.CASCADE,
   # )

    # Vaihtoehto 3: Aseta kirjoittaja tyhjäksi, jos käyttäjä poistetaan
    #kirjoittaja = models.ForeignKey
    #(
     #   settings.AUTH_USER_MODEL,
     #   on_delete=models.SET_NULL,
     #   null=True,
     #   blank=True,
    #)

    luotu = models.DateTimeField(auto_now_add=True)
    viimeksi_muokattu = models.DateTimeField(auto_now=True)
    julkaisuaika = models.DateTimeField(null=True, blank=True)

    # Metalla muutetaan tietyn luokan tekstejä/nimityksiä jotka näkyvät sivulla
    class Meta:
        verbose_name = _("postaus")
        verbose_name_plural = _("postaukset")

    def __str__(self):
        pvm_muoto = "%-d.%-m.%Y"
        kirjoittaja = self.kirjoittaja.get_full_name()
        return f"{self.otsikko} ({self.kirjoittaja} {self.luotu:{pvm_muoto}})"
