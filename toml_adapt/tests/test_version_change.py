from unittest import TestCase
from toml_adapt.ManipulateToml import ManipulateToml
import os

class SimpleBasicTestCase(TestCase):
    def setUp(self):
        self.__path = os.path.join(os.path.dirname(__file__), "data", 'pyproject2.toml')
        self.__action = "change"
        self.__dependency = "ALL"
        self.__version = "X"

    def test_change_all(self):
         a = ManipulateToml(self.__path, self.__action, self.__dependency, self.__version)
         a.make_action()
         version_change = a.check_for_specific_version("*")

         self.assertEqual(7, version_change)
