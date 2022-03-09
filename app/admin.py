from django.contrib import admin
from django.utils.safestring import mark_safe

from app.models import Item, OrderItem, Order, Category


class ItemAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'price', 'category', 'exist', 'get_image')
	list_display_links = ('title', )
	list_editable = ('exist', 'category')
	fields = ('title', 'slug', 'description', 'get_image', 'image', 'price', 'category', 'size', 'sex', 'exist')
	readonly_fields = ('get_image', )

	def get_image(self, obj):
		if obj.image:
			return mark_safe(f'<img src="{obj.image.url}">')
		return '-'

	get_image.short_description = 'Image'


class OrderItemAdmin(admin.ModelAdmin):
	list_display = ('pk', 'item', 'ordered')
	list_display_links = ('pk', 'item')
	fields = ('pk', 'item', 'ordered', 'user')
	list_editable = ('ordered', )


class CategoryAdmin(admin.ModelAdmin):
	fields = ('title', 'slug', )
	list_display = ('title', )
	list_display_links = ('title', )
	prepopulated_fields = {'slug': ('title', )}

# class OrderAdmin(admin.ModelAdmin):
# 	list_display = '__all__'
# 	fields = ('item', 'start_date', 'ordered_date', 'ordered', 'user')


admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order)
admin.site.register(Category, CategoryAdmin)
