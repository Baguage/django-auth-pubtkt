# django-auth-pubtkt

Author: Alexander Vyushkov

Implementation of mod_auth_pubtkt: a pragmatic Web Single Sign-On (SSO) solution as Django middleware.
This version was tested on Python == 2.7, Django == 1.11
 
It is incompatible with previous versions (use django-auth-pubtkt==1.1.2 for Django 1.5)

Please refer to https://neon1.net/mod_auth_pubtkt/index.html for additional details.
 
# Installation from GitHub

```bash
pip install git+git://github.com/Baguage/django-auth-pubtkt@master#egg=django-auth-pubtkt
 ```

# Installation:

django-auth-pubtkt uses M2Crypto library. Installation instructions for
different platforms are below.
When M2Crypto is installed, django-auth-pubtkt can be installed using pip
pip install django-auth-pubtkt
or using setuptools
./setup.py install

# Windows

Use binary package available on http://chandlerproject.org/Projects/MeTooCrypto#Downloads

# RedHat 7 + Python 3.5

I got "Failed building wheel for m2crypto" when used "pip install m2crypto" command.
The library was installed successfully, and all tests passed, somehow.

# CentOS 6/RedHat 6/Fedora

Fedora Core (and RedHat, CentOS etc.) have made changes to OpenSSL
configuration compared to many other Linux distributions. If you can not
build M2Crypto normally, try the fedora_setup.sh script included with
M2Crypto sources.

pip install --download=/tmp M2Crypto==0.21.1
cd /tmp
tar -zxf /tmp/M2Crypto-0.21.1.tar.gz
cd M2Crypto-0.21.1
./fedora_setup.sh install
python setup.py test

Note that setup.py test is required in some cases to fix "ImportError: No module named __m2crypto" error. 
lease refer to http://stackoverflow.com/questions/4773659/cant-install-a-python-package for additional details

CentOS 7/RedHat 7 should be fine

# Configuration

Add 'django_auth_pubtkt.middleware.DjangoAuthPubtkt' to MIDDLEWARE (Django 1.11+)

* Change LOGIN_URL to "/sso/"
* Set TKT_AUTH_LOGIN_URL to the address of SSO login page
* Add piece of code below to urls.py

```python
from django.conf.urls import url
from django_auth_pubtkt.views import redirect_to_sso

urlpatterns = [
# ...
url('^sso/', redirect_to_sso),
# ...
]
```

OR

Change LOGIN_URL to the address of SSO login page.
Configure your SSO to use 'next' as redirect field name.

OR

use @method_decorator(login_required(redirect_field_name="back"))

# Configuration variables (settings.py)

```
TKT_AUTH_PUBLIC_KEY
Default: None
Filename of DSA public key in .pem format. It is used to verify ticket signature.

TKT_AUTH_COOKIE_NAME
Default: "auth_pubtkt"
Name of the authentication cookie to use.

TKT_AUTH_USE_GROUPS
Default: False
Treat tokens as group names. Create groups if they don't exist yet.

TKT_AUTH_LOGIN_URL
Default: None
URL that users without a valid ticket will be redirected to

TKT_AUTH_BACK_ARG_NAME
Default: "back"
Name of the GET argument with the originally requested URL (when redirecting to the login page)

TKT_AUTH_ANONYMOUS_USER
Default: True
Add AnonymousUser object if no auth_pubtkt cookie is found. If set, django_auth_pubtkt can be used as a replacement to AuthenticationMiddleware.
If disabled, AuthenticationMiddleware and django_auth_pubtkt can be used together.
```