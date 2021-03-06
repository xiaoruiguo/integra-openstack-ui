from horizon import exceptions, tables, workflows, forms, tabs

from openstack_dashboard.dashboards.integra.providers.tables import ProviderTable
from openstack_dashboard.dashboards.integra.providers import utils
from openstack_dashboard.dashboards.integra.providers.workflows.add_provider import AddProvider

class ProvidersIndexView(tables.DataTableView):
    table_class = ProviderTable
    template_name = 'integra/providers/index.html'

    def get_data(self):
        return utils.getProviders(self)

class AddProviderView(workflows.WorkflowView):
    workflow_class = AddProvider

    def get_initial(self):
        initial = super(AddProviderView, self).get_initial()
        return initial
