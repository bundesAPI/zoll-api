"""
    Einfuhrzoll API

    Abfragen von Importzöllen und Wechselkursen  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.zoll.model.category import Category

from deutschland import zoll

globals()["Category"] = Category
from deutschland.zoll.model.categories_data import CategoriesData


class TestCategoriesData(unittest.TestCase):
    """CategoriesData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCategoriesData(self):
        """Test CategoriesData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CategoriesData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()