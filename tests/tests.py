from django.conf import settings
from django.template import Template, Context
from django.test.testcases import TestCase
from django.test.utils import override_settings
from django.core.urlresolvers import reverse

from django.http.cookie import SimpleCookie

class MiddlewareTest(TestCase):
    def test_redirect(self):
        pass


    def test_success(self):
        self.client.cookies = SimpleCookie(
            {
                'auth_pubtkt':
                    'MEUCIFqF5cxYi85Lsm0M6+1jIEb9AKX3bYa1XsH6h/ggTe6oAiEA0i3laZmjOGXJ/v9N6tt/B0PCFqOKpe7cFwegAU8GYWo='
            }
        )
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.user.username, "foobar1")
