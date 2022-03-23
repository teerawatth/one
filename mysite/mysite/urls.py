import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('ubonhouse.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static('media/', document_root=os.path.join(settings.BASE_DIR, 'media'))
