DSA or RSA key is required to test the middleware.

Don't use this key pair in production - generate your own

https://neon1.net/mod_auth_pubtkt/install.html

```bash
openssl dsaparam -out dsaparam.pem 2048
openssl gendsa -out privkey.pem dsaparam.pem
openssl dsa -in privkey.pem -out pubkey.pem -pubout
```

The dsaparam.pem file is not needed anymore after key generation and can safely be deleted.


Please refer to https://neon1.net/mod_auth_pubtkt/install.html for information how to generate a ticket

Ticket:
uid=foobar;validuntil=123456789;tokens=;udata=
MEUCIFqF5cxYi85Lsm0M6+1jIEb9AKX3bYa1XsH6h/ggTe6oAiEA0i3laZmjOGXJ/v9N6tt/B0PCFqOKpe7cFwegAU8GYWo=