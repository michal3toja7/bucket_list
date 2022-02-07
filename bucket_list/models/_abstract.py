from django.db import models
from ._helpers import BigCharField
from ._helpers import SmallCharField
from ._helpers import OPTIONAL
from ._choices import REALIZATION_STATUS
from ._choices import TO_REALIZATION
from .category import Category


class DreamAbstract(models.Model):
    title = BigCharField(verbose_name="Tytuł")
    # How to implement image? As file or link?
    # image
    short_description = models.TextField(
        **OPTIONAL, verbose_name="Opis krótki"
    )
    description = models.TextField(**OPTIONAL, verbose_name="Opis")
    deadline = models.DateField(**OPTIONAL, verbose_name="Termin realizacji")
    realisation_status = SmallCharField(
        choices=REALIZATION_STATUS,
        verbose_name="Status realizacji",
        default=TO_REALIZATION,
    )
    realization_desc = models.TextField(
        **OPTIONAL, verbose_name="Opis realizacji"
    )
    extra_fields = models.ManyToManyField(
        Category, blank=True, verbose_name="Kategorie"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Dodano")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Zaktualizowano"
    )

    class Meta:
        abstract = True
