from django.conf.urls import patterns, url
from openstack_dashboard.dashboards.integra.workflows import views

INDEX_URL = r'^$'
CREATE_URL = r'^create'
EXECUTE_URL = r'^execute'

urlpatterns = patterns('openstack_dashboard.dashboards.integra.workflows.views',
    url(INDEX_URL, views.PostIndexView.as_view(), name='index'),
    url(CREATE_URL, views.PostCreateView.as_view(), name='create'),
    url(EXECUTE_URL, views.ExecuteWorkflowView.as_view(), name='execute'),
)