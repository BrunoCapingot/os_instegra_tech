from django.contrib import admin
from django.urls import path, include
from django.urls import path
from IdentificadorDeItens import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('IdentificadorDeItens.urls')),  # <- essa linha faz a mágica

]
