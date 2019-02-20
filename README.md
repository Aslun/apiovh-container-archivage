# apiovh-container-archivage
Création d'un container Ovh Cloud automatiquement avec ID unique et datacenter aléatoire

.. image:: https://github.com/ovh/python-ovh/raw/master/docs/img/logo.png
           :alt: Python & OVH APIs

[![Build Status](https://travis-ci.org/ovh/php-ovh.svg)]()

Configuration du script python
----------

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
