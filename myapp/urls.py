from django.contrib import admin
from django.urls import path
from authentication.views import normalRegister as registerView_auth_n,registerView as registerView_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', registerView_auth),
    path('register-normal', registerView_auth_n),
]