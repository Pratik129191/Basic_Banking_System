import os
from .common import *


DEBUG = False
ALLOWED_HOSTS = ['localhost:8000']
SECRET_KEY = os.environ['SECRET_KEY']

