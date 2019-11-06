from django.test import TestCase

# Create your tests here.
import sys
from django.urls import path
from django.db import connection,transaction
from django import forms
#from misitio.ai.models import Cuidadores,Pacientes,Apoderados,Param,Pauta
from datetime import datetime

import sqlite3
#print ("Hola mundo !!")
#
#
cursor = connection.cursor()
sql_x = cursor.execute("select * from ai_pauta")
for k in sql_x:
	print(k.rut,k.paciente)


