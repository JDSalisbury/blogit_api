from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blogs', views.BlogViewSet)

urlpatterns = [] + router.urls
