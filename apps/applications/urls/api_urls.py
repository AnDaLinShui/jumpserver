# coding:utf-8
#

from django.urls import path, re_path
from rest_framework_bulk.routes import BulkRouter

from common import api as capi
from .. import api

app_name = 'applications'

router = BulkRouter()
router.register(r'applications', api.ApplicationViewSet, 'application')
router.register(r'remote-apps', api.RemoteAppViewSet, 'remote-app')
router.register(r'database-apps', api.DatabaseAppViewSet, 'database-app')
router.register(r'k8s-apps', api.K8sAppViewSet, 'k8s-app')

urlpatterns = [
    path('remote-apps/<uuid:pk>/connection-info/', api.RemoteAppConnectionInfoApi.as_view(), name='remote-app-connection-info'),
]

old_version_urlpatterns = [
    re_path('(?P<resource>remote-app)/.*', capi.redirect_plural_name_api)
]

urlpatterns += router.urls + old_version_urlpatterns
