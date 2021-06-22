from unittest import TestCase
from toml_adapt.ManipulateToml import ManipulateToml
import os

class SimpleBasicTestCase(TestCase):
    def setUp(self):
        self.__path = os.path.join(os.path.dirname(__file__), "data", 'pyproject.toml')
        self.__action = "add"
        self.__dependency = "niaclass"
        self.__version = "X"

    def test_make_simple_action(self):
         a = ManipulateToml(self.__path, self.__action, self.__dependency, self.__version)
         a.make_action()
         number_of_deps = a.get_number_of_dependencies()

         self.assertEqual(8, number_of_deps)
