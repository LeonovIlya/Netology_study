from django.contrib import admin
from django.urls import path, include
from authorization.views import profileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('backend.urls', namespace='backend')),
    path('auth/', include('authorization.urls')),
    path('authorization/profile/', profileView, name='profile'),
]