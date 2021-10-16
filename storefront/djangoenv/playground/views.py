from typing_extensions import Concatenate
from django.db.models.expressions import OrderBy
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, query
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from store.models import Collection, Product, OrderItem, Order, Customer
from tags.models import TaggedItem, TaggedItemManager
# Create your views here.


def say_hello(request):
    try:
        # Get Tagged Products
        TaggedItem.objects.get_tags_for(Product, 1)
        # content_type = ContentType.objects.get_for_model(Product)
        # query_set = TaggedItem.objects \
        #     .select_related('tag') \
        #     .filter(
        #         content_type=content_type,
        #         object_id=1  # this should be got dynamically
        #     )
    except ObjectDoesNotExist:
        pass
    return render(request, 'hello.html', {'name': ' Jack'})


def orm_tuts(request):
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

        # select_related to load dependent objects
        # select related is used when the other side has only one object , for eg: Product has one collection
        query_set = Product.objects.select_related('collection').all()

        # use prefetch_related when other side has multiple objects , eg :Many Promotions in a product
        query_set = Product.objects.prefetch_related(
            'promotions').select_related('collection').all()

        # Get last 5 orders with customer and items , incl. Product
        query_set = Order.objects.select_related(
            'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:7]
        # orders = Order.objects.select_related('customer').prefetch_related('OrderItem').select_related('Product').select_related(
        #    'customer').filter().order_by('-placed_at')[:5]

        # Expression Wrapper
        discounted_price = ExpressionWrapper(
            F('unit_price') * 0.8, output_field=DecimalField(6))
        query_set = Customer.objects.annotate(
            discounte_price=discounted_price)
        # orders each customer placed
        query_set = Customer.objects.annotate(
            orders_count=Count('order')
        )

        # concatenation
        query_set = Customer.objects.annotate(new_id=F('id') + 1)
        query_set = Customer.objects.annotate(
            # CONCAT
            full_name=Func(F('first_name'), Value(' '), F(
                'last_name'), function='CONCAT')
        )

        query_set = Customer.objects.annotate(
            # CONCAT
            full_name=Concat('first_name', Value(' '),
                             'last_name')
        )

        result = list(query_set)

    except ObjectDoesNotExist:
        pass
    return render(request, 'orm_tuts.html', {'name': ' Jack', 'products': result, 'orders': query_set})
