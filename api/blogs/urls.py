from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blogs', views.BlogViewSet)
router.register('tags', views.TagViewSet)

urlpatterns = [] + router.urls
