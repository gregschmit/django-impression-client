Impression Client
#################

.. image:: https://travis-ci.org/gregschmit/django-impression-client.svg?branch=master
    :alt: TravisCI
    :target: https://travis-ci.org/gregschmit/django-impression-client

.. image:: https://img.shields.io/pypi/v/django-impression-client
    :alt: PyPI
    :target: https://pypi.org/project/django-impression-client/

.. image:: https://coveralls.io/repos/github/gregschmit/django-impression-client/badge.svg?branch=master
    :alt: Coverage
    :target: https://coveralls.io/github/gregschmit/django-impression-client?branch=master

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: Code Style
    :target: https://github.com/ambv/black

Source: https://github.com/gregschmit/django-impression-client

PyPI: https://pypi.org/project/django-impression-client/

Impression Client is a reusable Django app that provides helpers for interacting with
remote systems running `Impression <https://pypi.org/project/django-impression/>`_.


Installation
############

.. code-block:: shell

    $ pip install django-impression-client


Configuration
#############

Add ``django-impression-client`` to your requirements file to ensure it's installed in
the environment. Configure your ``settings.py``:

.. code-block:: python

    EMAIL_BACKEND = "impression_client.backends.RemoteEmailBackend"
    IMPRESSION_DEFAULT_TARGET = "https://impression.example.org/api/send_message/"
    IMPRESSION_DEFAULT_TOKEN = "my_api_auth_token_here"

If you want to store your credentials in the database rather than statically in your
project ``settings.py`` file, include ``impression_client`` in your ``INSTALLED_APPS``,
then run database migrations. Finally, remove the ``IMPRESSION_DEFAULT_TARGET`` and
``IMPRESSION_DEFAULT_TOKEN`` from your project ``settings.py``, and go into the Django
admin UI to add impression servers.


Tests
#####

.. code-block:: shell

    $ python manage.py test
