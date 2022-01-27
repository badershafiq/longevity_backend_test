from rest_framework.routers import DefaultRouter
from .views import RecommendationViewset

router = DefaultRouter()
router.register(r'', RecommendationViewset, basename='recommendation')
urlpatterns = router.urls
