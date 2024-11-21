from django.urls import path, include
from rest_framework.routers import DefaultRouter
from result_code.v2.views import CodeReiewViewSet
from result_code.v2.views import CodeReiewViewSet   


router = DefaultRouter()
router.register(r'result_code', CodeReiewViewSet )
urlpatterns = [
    path('', include(router.urls)),
]