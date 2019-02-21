#! usr/bin/python 
# -*- coding: ISO-8859-1 -*- 
##########################################################
#     ___         __                                     #
#    /   |  _____/ /_  ______                            #
#   / /| | / ___/ / / / / __ \                           #
#  / ___ |(__  ) / /_/ / / / /                           # 
# /_/  |_/____/_/\__,_/_/ /_/                            #
#                                                        #
# Développeur multi-platerformes                         #
# Twitter : https://twitter.com/bastlanguedoc?lang=fr    #
##########################################################

# coding: utf-8

#Import
import json
import ovh
import string
import uuid
import smtplib
import random
import config
# import time, math, urllib2, urllib, os, shutil, zipfile, smtplib, sys

# Function choix datacenter aléatoire + ID aléatoire
datacenter = ["GRA5", "UK1", "BHS3", "DE1", "WAW1"] # List Datacenter OVH
lowercase_str = uuid.uuid4().hex  
uppercase_str = lowercase_str.upper()
uppercase_str



#Code apps OVH API
client = ovh.Client(
    endpoint='ovh-eu',              
    application_key=config.KEY, 
    application_secret=config.SECRET, 
    consumer_key=config.CONSKEY,  
)

#Exécution de l'API OVH
result = client.post('/cloud/project/8e759a7a7a26449eb1e61d11d26a3853/storage', # ID Project de votre OVH Cloud
    archive=True, # Container d'archivage
    containerName=uppercase_str, # Nom aléatoire
    region=random.choice(datacenter), # Choix du datacenter alétoire
)

#Resultat
print json.dumps(result, indent=4)