from django.shortcuts import render
from django.http import Http404
# from django.http import HttpResponse

from inventory.models import Item  # used to query the database

# Create your views here.


def index(request):
		items = Item.objects.exclude(amount=0)  # .exclude for index function. this is the items query set
		return render(request, 'inventory/index.html', {  #render is the shortcut method to return an HttpResponse & wires the view up to the template file. the 1st arguement to render is the request & the 2nd is the path to the template file
			'items': items,  # 3rd arguement is the templates context(a dictionary)the keys of the dictionary will be used as variable names inside the template and the values in the dictionary we have defined in the view, this is how the index view passes data into the template. the'items' string is the variable we will use in the template, the items variable on the right is the value from the query set
	})
	# return HttpResponse('<p> In Index View </p>')


def item_detail(request, id):
		try:  #try / except block
			item = Item.objects.get(id=id)
		except Item.DoesNotExist:
			raise Http404('Bro, this item does not exist!')
		return render(request, 'inventory/item_detail.html', {
			'item': item,
		})
	# return HttpResponse('<p> In item_detail view with id {0} </p>'.format(id))
