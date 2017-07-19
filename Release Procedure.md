# Checklist for new release

1. Run unittests: `python runtests.py` or `python setup.py test`
2. Update CHANGELOG.txt
3. Update version in setup.py
4. Push all changes to github
5. Test installation on a different machine in a fresh virtual environment
```bash
cd /tmp
git clone https://github.com/Baguage/django-auth-pubtkt
mkvirtualenv django-auth-pubtkt
cd django-auth-pubtkt
pip install django==1.11 M2Crypto
python runtests.py
python setup.py install
deactivate
rmvirtualenv django-auth-pubtkt
cd ..
rm -rf django-auth-pubtkt
```
6. Make a release/tag

https://github.com/Baguage/django-auth-pubtkt/releases -> Draft a new release

Use v0.6.2 format for tag name

7. Run `setup.py sdist bdist_egg bdist_wininst upload` command