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


#Import
import json
import ovh
import string
import uuid
import smtplib
import random
# import time, math, urllib2, urllib, os, shutil, zipfile, smtplib, sys

# Function choix datacenter aléatoire + ID aléatoire
datacenter = ["GRA5", "UK1", "BHS3", "DE1", "WAW1"] # List Datacenter OVH
lowercase_str = uuid.uuid4().hex  
uppercase_str = lowercase_str.upper()
uppercase_str

#Code apps OVH API
client = ovh.Client(
    endpoint='ovh-eu',              
    application_key='KEY',  # Votre key apps ovh 
    application_secret='SECRET', # Votre apps secret OVH
    consumer_key='CONSKEY',  #  Votre consumer key OVH   
)

#Exécution de l'API OVH
result = client.post('/cloud/project/IDPROJECT/storage', # ID Project de votre OVH Cloud
    archive=True, # Container d'archivage
    containerName=uppercase_str, # Nom aléatoire
    region=random.choice(datacenter), # Choix du datacenter alétoire
)

#Resultat
print json.dumps(result, indent=4)