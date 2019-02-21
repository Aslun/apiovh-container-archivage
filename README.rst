# apiovh-container-archivage

.. image:: https://github.com/ovh/python-ovh/raw/master/docs/img/logo.png
           :alt: Python & OVH APIs

.. image:: https://travis-ci.org/ovh/python-ovh.svg?branch=master
           :alt: Build Status
           :target: #

Configuration du script python
----------

Editer le fichier config.py

           nano config.py

.. code:: python

    # -*- encoding: utf-8 -*-

    # Instantiate. Visit https://api.ovh.com/createToken/?GET=/me
           KEY = '' 		# Votre key apps ovh 
           CONSKEY = ''	# Votre apps secret OVH
           SECRET = ''		# Votre consumer key OVH
    )
   
Editer le fichier createcontainer.py

           nano createcontainer.py

.. code:: python
       # -*- encoding: utf-8 -*-
     #Exécution de l'API OVH
    result = client.post('/cloud/project/ID DU PROJET/storage', # ID Project de votre OVH Cloud
    archive=True, # Container d'archivage
    containerName=uppercase_str, # Nom aléatoire
    region=random.choice(datacenter), # Choix du datacenter alétoire
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
