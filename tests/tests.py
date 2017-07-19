from django.test.testcases import TestCase
from django.http.cookie import SimpleCookie
from django.conf import settings
from django.urls.base import reverse


class MiddlewareTest(TestCase):
    def test_redirect(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, settings.LOGIN_URL + "?next=/")

    def test_success(self):
        self.client.cookies = SimpleCookie(
            {
                'auth_pubtkt':
                    'uid=foobar;validuntil=123456789;tokens=;udata=;sig=MEUCIFqF5cxYi85Lsm0M6+1jIEb9AKX3bYa1XsH6h/ggTe6oAiEA0i3laZmjOGXJ/v9N6tt/B0PCFqOKpe7cFwegAU8GYWo='
            }
        )
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, "User: foobar\n")

    # def test_sso_url(self):
    #     response = self.client.get(reverse("django_auth_pubtkt.sso"))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, settings.TKT_AUTH_LOGIN_URL)
