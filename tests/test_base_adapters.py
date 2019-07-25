from unittest import TestCase
from liasis.base.adapters import BaseAPIAdapter
from liasis.core.protocols import ResponseProtocol
from liasis.core.errors.infrastructure import InfrastructureError


class TestBaseAdapters(TestCase):

    def setUp(self):

        class ResponseDemo(ResponseProtocol):
            data: dict = {}
            error: Exception = None

        self.response = ResponseDemo()

    def test_instanciate_adapter(self):

        adapter = BaseAPIAdapter()

        self.assertIsInstance(adapter, BaseAPIAdapter)

    def test_call_adapter(self):

        adapter = BaseAPIAdapter()

        adapter_call = adapter(self.response)

        self.assertIsInstance(adapter_call, str)

    def test_call_adapter_with_wrong_response(self):

        adapter = BaseAPIAdapter()

        wrong_response_one = dict()
        wrong_response_two = ''
        wrong_response_three = 123

        adapter(wrong_response_one)

        with self.assertRaises(InfrastructureError):

            adapter(wrong_response_one)
        
        with self.assertRaises(InfrastructureError):

            adapter(wrong_response_two)

        with self.assertRaises(InfrastructureError):

            adapter(wrong_response_three)