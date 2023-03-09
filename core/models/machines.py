import uuid as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Machines(models.Model):
    """ Machines of the quarry """
    numbers = models.CharField(_("Номер машины"), max_length=100)

    dumper_models = models.ForeignKey(
        "DumperModels", on_delete=models.PROTECT, null=False, blank=True
    )

    # Можно вытащить и из 'dumper_models', но потом с этим легко замучиться,
    # а в текущих условиях (и будущем) на производительность особо не повлияет
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.PROTECT, null=False, blank=True
    )

    is_active = models.BooleanField(_("Активно"), default=False, db_index=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)

    def __str__(self):
        return self.numbers

    class Meta:
        verbose_name = _("Машина")
        verbose_name_plural = _("Машины")
        db_table = "core_machines"
        ordering = ["numbers"]
