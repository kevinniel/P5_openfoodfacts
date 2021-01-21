""" This module contains all the constants of the program """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# selected categories for the local data base
URL = "https://fr.openfoodfacts.org/cgi/search.pl"

CATEGORIES = [
                "pates-a-tartiner",
                "boissons",
                "condiments",
                "biscuits-et-gateaux",
                "pizzas"
                ]

# Maximal number of product by categorie
P_MAX = 25

# Mysql server configuration:
HOST = "localhost"
USER = "root"
PASSWORD = "mu122238"
DATABASE = "db_p5"
