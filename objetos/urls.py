from django.urls import path
from .views import ObjetosListView

app_name = 'object'

urlpatterns = [
    path('', ObjetosListView.as_view(), name='objetos')
]