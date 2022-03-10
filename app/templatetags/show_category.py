from django import template
from app.models import Category

register = template.Library()


@register.inclusion_tag('app/show_category.html')
def get_category():
	return {'category': Category.objects.all()}
