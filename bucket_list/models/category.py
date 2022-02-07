from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="child",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (
            "slug",
            "parent",
        )
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"
