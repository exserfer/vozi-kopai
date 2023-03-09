import uuid as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class MachinesOperation(models.Model):
    """ Cars that are currently on the work """

    machines = models.ForeignKey(
        "Machines", on_delete=models.PROTECT, null=False, blank=True
    )

    current_weight_payload = models.IntegerField(
        _("Текущий вес загрузки в Тоннах"),
        null=False,
        default=0
    )

    is_active = models.BooleanField(_("Активно"), default=False, db_index=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)

    def __str__(self):
        return self.machines.numbers

    def persent_overload(self):
        calc = (self.machines.dumper_models.maximum_load / self.current_weight_payload) * 100 - 100
        return -1*float("{:.2f}".format(calc))

    class Meta:
        verbose_name = _("Машина в работе")
        verbose_name_plural = _("Машины в работе")
        db_table = "core_machines_operation"
        ordering = ["machines"]
