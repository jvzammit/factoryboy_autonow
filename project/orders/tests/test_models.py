import arrow
import time_machine
from django.test import TestCase
from orders.models import Order
from orders.tests.factories import OrderFactory


class OrderQuerysetTest(TestCase):
    @time_machine.travel("2023-09-10 14:30")
    def test_created_today(self):
        # Given three orders created on today's date's boundaries
        date1 = arrow.get("2023-09-09 23:59").datetime  # yesterday
        date2 = arrow.get("2023-09-10 00:00").datetime  # today 00:00
        date3 = arrow.get("2023-09-10 00:01").datetime  # today 00:01
        
        # approach 3
        _ = OrderFactory(created_at=date1)
        order2 = OrderFactory(created_at=date2)
        order3 = OrderFactory(created_at=date3)

        # When created_today is called
        queryset = Order.objects.all().created_today()

        # Then the expected orders are returned
        self.assertQuerysetEqual(
            queryset,
            queryset.filter(id__in=[order2.id, order3.id]),
        )
