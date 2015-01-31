from django.utils.translation import ugettext_lazy as _

from horizon import tables

class InstancesTable(tables.DataTable):
    id = tables.Column("id", verbose_name=_("Id"))
    name = tables.Column("name", verbose_name=_("Name"))
    description = tables.Column("description", verbose_name=_("Description"))

    class Meta:
        name = "providers"
        verbose_name = _("Providers")