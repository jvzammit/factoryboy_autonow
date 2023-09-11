import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "orders.Order"

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        # override auto_now_add for "created_at" column
        created_at = kwargs.pop("created_at", None)
        obj = super()._create(model_class, *args, **kwargs)
        if created_at is not None:
            model_class.objects.filter(id=obj.id).update(created_at=created_at)
        return obj
