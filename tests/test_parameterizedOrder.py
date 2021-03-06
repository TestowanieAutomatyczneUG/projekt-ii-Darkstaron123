import unittest
from assertpy import *
from src.order import *
from parameterized import *
from unittest.mock import *

@parameterized_class(('wrongValueInt', 'wrongValueFloat'), [
    (True, False),
    (None, None),
    (-8.0, 9),
    ("", ""),
    ("Cosiek", 0),
    ([9, 3, 6], [6, 3, 9]),
    (9.0, "Bobert"),
    ({'firstName': 8, 'lastName': 2, 'thirdName': 3}, {'firstName': 90, 'lastName': 5, 'thirdName': 4})
])
class TestsParametrizedOrder(unittest.TestCase):

    def setUp(self):
        def mock_get_orders():
            return [(709, 177)]#reczna atrapa
        Order.orders = []
        Queries.find_order = Mock(return_value=(7, 8))#atrapa z uzyciem return value
        self.order = Order(mock_get_orders()[0][0], mock_get_orders()[0][1])

    def test_order_init_wrong_id_one(self):
        assert_that(Order).raises(ValueError).when_called_with(self.wrongValueInt, self.wrongValueFloat)

    def test_order_init_wrong_id_two(self):
        assert_that(Order).raises(ValueError).when_called_with(self.wrongValueFloat, self.wrongValueInt)

    def test_delete_order_wrong_id_one(self):
        assert_that(Order.delete_order).raises(ValueError).when_called_with(self.wrongValueInt)

    def test_delete_order_wrong_id_two(self):
        assert_that(Order.delete_order).raises(ValueError).when_called_with(self.wrongValueFloat)

    def test_get_order_wrong_id_one(self):
        assert_that(Order.find_order).raises(ValueError).when_called_with(self.wrongValueInt)


    def tearDown(self):
        del self.order