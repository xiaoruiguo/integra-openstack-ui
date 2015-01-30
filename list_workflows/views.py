
from horizon import tabs

from openstack_dashboard.dashboards.integra.list_workflows \
    import tabs as integra_tabs


class IndexView(tabs.TabbedTableView):
    tab_group_class = integra_tabs.MypanelTabs
    template_name = 'integra/list_workflows/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
