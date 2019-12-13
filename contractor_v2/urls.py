
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Site
    path('admin/', admin.site.urls),

    #Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    
    # items App
    path('', include('items.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)