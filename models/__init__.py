#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from engine.file_storage import FileStorage
from engine.db_storage import DBStorage
from os import getenv
from base_model import BaseModel
from user import User
from state import State
from city import City
from amenity import Amenity
from place import Place
from review import Review


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
