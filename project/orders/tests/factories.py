import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "orders.Order"
