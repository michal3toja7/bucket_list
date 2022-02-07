from django.db import models

OPTIONAL = dict(blank=True, null=True)


class BigCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 256
        super(BigCharField, self).__init__(*args, **kwargs)


class SmallCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 16
        super(SmallCharField, self).__init__(*args, **kwargs)
