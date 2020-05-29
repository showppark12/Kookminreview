from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import studyboard.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('studyboard/',include('studyboard.urls')),
    path('account/', include('account.urls')),
    path('food/', include('foodboard.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
