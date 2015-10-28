from __future__ import unicode_literals

from django.db import models

# Create your models here.
# since this model is in the inventory app, it will be called inventory_item
#field types
#NUMERIC DATA
#IntegerField
#DecimalField
#TEXTUAL DATA
#CharField -requires a max_length attribute 
#example
#models.CharField(max_length=10, null=True, blank=True)
#attribute meanings and usage
#if null is true, then the field can be stored as null meaning no data for that field in a given record
#blank is set true on a textual field to allow for an empty string
#default allows to set default value for a field
#choices used to limit the valies that can be stored to a set of choices that are provided

#TextField unbounded length
#EmailField comes with built-in input validators for format
#URLField comes with built-in input validators for format
#FILE DATA
#FileField stores docs, pdfs, word docs etc
#ImageField stores images validates uploaded file is an image
#MISCELLANEOUS DATA
#BooleanField  true or false
#DateTimeField datetime(1969, 1, 1, 8, 0, 0)


class Item(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()
