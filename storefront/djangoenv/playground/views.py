from django.db.models.expressions import OrderBy
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.http import HttpResponse
from store.models import Collection, Product, OrderItem
# Create your views here.


def say_hello(request):
    try:

        #query_set = Product.objects.all()
        # product = Product.objects.get(id=1)  # will error if id does not exist
        # or
        #product = Product.objects.get(pk=1)

        # product = Product.objects.filter(pk=0).first()  # no error
        # exists = Product.objects.filter(pk=0).exists()  # no error

        # filtering
        # query set api - field lookups
        query_set = Product.objects.filter(unit_price__gt=20)
        #query_set = Product.objects.filter(unit_price__range=(20, 40))

        # get product belong to collections 1,2,3
        #query_set = Product.objects.filter(collection__id__range=(1, 2, 3))

        # icontains - case insensitive
        # same goes for startswith , endswith,istartswith , iendswith
        #query_set = Product.objects.filter(title__icontains='coffee')

        # for AND operations
        query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
        # or
        query_set = Product.objects.filter(
            inventory__lt=10).filter(unit_price__lt=20)

        # for OR operations - import Q
        # adding '-' before column name makes it descending
        query_set = Product.objects.filter(
            Q(inventory__lt=10) | Q(unit_price__lt=20)).order_by('unit_price', '-title')

        # reverse inverts the order by conditions
        # query_set = Product.objects.filter(
        #    Q(inventory__lt=10) | Q(unit_price__lt=20)).order_by('unit_price', '-title').reverse()

        # for NOT operation use ~

        #query_set = Product.objects.filter(title__isnull=True)
        #first_product = query_set[0]

        # F objects to reference other fields
        #query_set = Product.objects.filter(inventory=F('unit_price'))

        # sort by unit price in ascending and get first object
        product = Product.objects.earliest('unit_price')

        # returns objects 0,1,2,3,4
        query_set = Product.objects.all()[:5]

        # use 'values' when you want to specify certain columns
        query_set = Product.objects.values('id', 'title')

        # use 'values' when you want to specify certain columns
        # creates an inner join with collection table , returns dictionaries
        query_set = Product.objects.values('id', 'title', 'collection__title')

        # values_list returns tuples
        query_set = Product.objects.values_list(
            'id', 'title', 'collection__title')

        # products that have been ordered , sorted by title
        query_set = Product.objects.filter(
            id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

        query_set = Product.objects.only('id', 'title')
        # deferring fields , returns instances of the product class wheras in 'values' you get dictionaries
        # defer - defer the loading later
        query_set = Product.objects.defer('description')

    except ObjectDoesNotExist:
        pass
    return render(request, 'hello.html', {'name': ' Jack', 'products': list(query_set)})
