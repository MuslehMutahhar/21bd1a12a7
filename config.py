# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('osDvxf') or 'you-will-never-guess'
    REGISTER_URL = "http://20.244.56.144/test/register"
    AUTH_URL = "http://20.244.56.144/test/auth"
