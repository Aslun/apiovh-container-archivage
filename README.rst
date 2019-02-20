# apiovh-container-archivage

.. image:: https://github.com/ovh/python-ovh/raw/master/docs/img/logo.png
           :alt: Python & OVH APIs

.. image:: https://travis-ci.org/ovh/python-ovh.svg?branch=master
           :alt: Build Status
           :target: #

Configuration du script python
----------


.. code:: python

    # -*- encoding: utf-8 -*-

    # Instantiate. Visit https://api.ovh.com/createToken/?GET=/me
    client = ovh.Client(
        endpoint='ovh-eu',
        application_key='<application key>', # <= votre Key
        application_secret='<application secret>', # <= votre Secret
        consumer_key='<consumer key>', # <= votre Consumer
    )




Debian & Distributions dérivées de Debian
----------

Installation de Python

    apt install python & python-pip

Installation pip de OVH

    pip install ovh
    
Exécution du script

    python contairerarchivage.py
    
    
CentOS and RHEL
----------

Installation de Python

    yum install epel-release & python-pip

Installation pip de OVH

    pip install ovh
    
Exécution du script

    python contairerarchivage.py
