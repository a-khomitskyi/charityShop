from django.urls import path
from app.views import *


urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('items/<str:slug>', ItemDetail.as_view(), name='item'),
	path('category/<str:slug>', CategoryView.as_view(), name='category'),
]
