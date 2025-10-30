from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('citizens.urls')),  # ✅ include only once here
]
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from citizens.views import CitizenViewSet

router = DefaultRouter()
router.register('citizens', CitizenViewSet, basename='citizen')

urlpatterns = [
    # 👇 This defines your homepage
    path('', lambda request: HttpResponse("<h2>Welcome to the Django Country API 🌍</h2><p>Visit /api/citizens/ to explore the endpoints.</p>")),

    # 👇 Your actual API and admin routes
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
