from django.db import models
import json

# Create your models here.

MESSAGE_FILE = 'messages.json'

def get_messages():
    fhandler = open(MESSAGE_FILE, 'rt')
    cxt = fhandler.read()
    fhandler.close()
    return json.loads(cxt)