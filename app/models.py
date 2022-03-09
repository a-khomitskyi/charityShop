from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

SIZE = (
	('XS', 'XS'),
	('S', 'S'),
	('M', 'M'),
	('L', 'L'),
	('XL', 'XL'),
	('2XL', '2XL'),
	('3XL', '3XL')
)

SEX = (
	('M', 'Man'),
	('W', 'Woman'),
	('C', 'Child')
)


class Category(models.Model):
	slug = models.SlugField(max_length=50)
	title = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural = 'categories'

	def get_absolute_url(self):
		return reverse('category', kwargs={'slug': self.slug})


class Item(models.Model):
	slug = models.SlugField(max_length=255)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='images', blank=True, null=True)
	price = models.FloatField(default=0)
	category = models.ForeignKey(Category, models.CASCADE, related_name='category')
	size = models.CharField(max_length=3, choices=SIZE)
	sex = models.CharField(max_length=1, choices=SEX)
	exist = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('item', kwargs={'slug': self.slug})


class OrderItem(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return f'{self.quantity} of {self.item.title}'


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username
