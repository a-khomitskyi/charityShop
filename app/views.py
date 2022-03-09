from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Item


class HomeView(ListView):
	model = Item
	template_name = 'app/index.html'


class ItemDetail(DetailView):
	model = Item


class CategoryView(HomeView):

	def get_queryset(self):
		return Item.objects.filter(slug=self.kwargs['slug'])
