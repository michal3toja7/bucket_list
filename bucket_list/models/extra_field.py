from django.db import models

from ._abstract import DreamAbstract
from ._helpers import BigCharField
from ._helpers import OPTIONAL


class ExtraField(models.Model):
    dream = models.ForeignKey(
        DreamAbstract, on_delete=models.CASCADE, related_name="_extra_fields"
    )
    title = BigCharField(verbose_name="Tytuł pola")
    desc = models.TextField(**OPTIONAL, verbose_name="Zawartość pola")

    class Meta:
        verbose_name = "Pole dodatkowe"
        verbose_name_plural = "Pola dodatkowe"
