import uuid as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Manufacturer(models.Model):
    """ Dump truck manufacturers """

    name = models.CharField(_("Производители"), max_length=100)
    manufacturer_unique_name = models.CharField(
        _("Unique Tag Name"),
        max_length=60,
        default=None,
        null=False,
        unique=True
    )
    is_active = models.BooleanField(_("Активно"), default=False, db_index=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Производитель")
        verbose_name_plural = _("Производители")
        db_table = "core_manufacturer"
        ordering = ["name"]
