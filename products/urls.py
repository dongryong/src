from django.urls import path
from .views import chart_select_view
app_name = 'products'

# main urls.py -> app urls.py 
# create view -> templates -> view to urls app

urlpatterns = [
    path('', chart_select_view, name='main-products-view')
]
