import unittest
from assertpy import *
from src.item import *
from parameterized import *
from unittest.mock import *

@parameterized_class(('wrongValueInt','wrongValueString', 'wrongValueFloat'), [
    (True, False, True),
    (None, None, None),
    ("Robert", -8.0, 9),
    ("", "", ""),
    ("Cosiek", 0, "łosiek"),
    ([9, 3, 6], [6, 3, 9], [3, 9, 6]),
    ("Bobert", 9.9, 1),
    ({'firstName': 8, 'lastName': 2, 'thirdName': 3}, {'firstName': 90, 'lastName': 5, 'thirdName': 4},
     {'firstName': 77, 'lastName': 777, 'thirdName': 5}),
])
class TestsParametrizedItem(unittest.TestCase):

    def setUp(self):
        def mock_get_items():
            return [(709, "cosiek", 177.0)]#reczna atrapa
        Item.items = []
        self.item = Item(mock_get_items()[0][0], mock_get_items()[0][1], mock_get_items()[0][2])

    def test_edit_item_name_wrong(self):
        assert_that(self.item.edit_name).raises(ValueError).when_called_with(self.wrongValueString)

    def test_item_init_wrong_id(self):
        assert_that(Item).raises(ValueError).when_called_with(self.wrongValueInt, self.item.name, self.item.value)

    def test_delete_item_wrong_id(self):
        assert_that(Item.delete_item).raises(ValueError).when_called_with(self.wrongValueInt)

    def test_get_item_wrong_id(self):
        assert_that(Item.find_item).raises(ValueError).when_called_with(self.wrongValueInt)

    def test_item_init_wrong_name(self):
        assert_that(Item).raises(ValueError).when_called_with(self.item.id, self.wrongValueString, self.item.value)



    def tearDown(self):
        del self.item