from unittest import TestCase
from package_archetype.hello_world import get_message


class TestHelloWorld(TestCase):
    def test_get_message(self):
        assert "Hello world!" == get_message()
