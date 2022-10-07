
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, ArtisteViewSet, LyricViewSet
router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='song')
router.register(r'artistes', ArtisteViewSet, basename='artiste')
router.register(r'lyrics', LyricViewSet, basename='lyric')
urlpatterns = router.urls
