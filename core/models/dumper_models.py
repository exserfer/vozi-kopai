import uuid as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class DumperModels(models.Model):
    name = models.CharField(_("Название модели"), max_length=100)
    dumper_models_unique_name = models.CharField(
        _("Unique model name"),
        max_length=60,
        default=None,
        null=False,
        unique=True
    )
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.PROTECT, null=False, blank=True
    )
    maximum_load = models.IntegerField(_("Максимальная грузоподъёмность"), null=False, default=0)

    is_active = models.BooleanField(_("Активно"), default=False, db_index=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Модель машины")
        verbose_name_plural = _("Модели машин")
        db_table = "core_dumper_models"
        ordering = ["name"]
