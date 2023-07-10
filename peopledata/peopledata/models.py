from distutils.command.upload import upload
from django.db import models

# Creating models for known, unknown and criminal
# Each attribute of the model represents a database field.

class Known(models.Model):

    # to upload image to known database
    
    image = models.ImageField(upload_to='knownimg',
                              max_length=500, null=True, blank=True)
    def _str_(self):
        return str(self.id)

class Unknown(models.Model):

    # to retrieve image of unknown from database

    img = models.TextField(null=True)

    class Meta:
        db_table = "unknowns"

    def _str_(self):
        return str(self.id)

class Criminal(models.Model):

    # to upload image to criminal database
    
    image = models.ImageField(upload_to='criminalimg',
                              max_length=500, null=True, blank=True)

    def _str_(self):
        return str(self.id)


