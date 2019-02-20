# apiovh-container-archivage

.. image:: https://github.com/ovh/python-ovh/raw/master/docs/img/logo.png
           :alt: Python & OVH APIs


[![Build Status](https://travis-ci.org/ovh/php-ovh.svg)]()

Configuration du script python
----------


.. code:: python

    # -*- encoding: utf-8 -*-

    import ovh

    # Instantiate. Visit https://api.ovh.com/createToken/?GET=/me
    # to get your credentials
    client = ovh.Client(
        endpoint='ovh-eu',
        application_key='<application key>',
        application_secret='<application secret>',
        consumer_key='<consumer key>',
    )




Debian & Distributions dérivées de Debian
----------

Installation de Python

    apt install python & python-pip

Installation pip de OVH

    pip install ovh
    
Exécution du script

    python contairerarchivage.py
