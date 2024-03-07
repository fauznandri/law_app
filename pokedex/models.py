import os
from django.db import models
from .storage import OverwriteStorage

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('pokemon', "jpg")
    return os.path.join('images', filename)
    # return filename

class Pokemon(models.Model):
    image = models.ImageField(upload_to=content_file_name, storage=OverwriteStorage())
