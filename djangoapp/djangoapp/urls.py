
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('login_app.urls')),
    path("accounts/",include('allauth.urls')),
    # path("accounts/profile/perfilU;suario",include('profile.html')),

]
