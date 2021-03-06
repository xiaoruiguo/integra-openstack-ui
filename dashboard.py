from django.utils.translation import ugettext_lazy as _

import horizon

class Actions(horizon.PanelGroup):
    slug = "actions"
    name = _("Actions")
    panels = ('actions',)

class Providers(horizon.PanelGroup):
    slug = "providers"
    name = _("Providers")
    panels = ('providers',)

class Workflows(horizon.PanelGroup):
    slug = "workflows"
    name = _("Workflows")
    panels = ('workflows',)

class Schedules(horizon.PanelGroup):
    slug = "schedules"
    name = _("Schedules")
    panels = ('schedules',)

class Jobs(horizon.PanelGroup):
    slug = "jobs"
    name = _("Jobs")
    panels = ('jobs',)

class Integra(horizon.Dashboard):
    name = _("Integra")
    slug = "integra"
    panels = (Actions, Providers, Workflows, Schedules, Jobs)  # Add your panels here.
    default_panel = 'providers'  # Specify the slug of the default panel.


horizon.register(Integra)
