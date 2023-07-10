from django.contrib import admin
from .models import Known
from .models import Criminal
from .models import Unknown

# add models to the Django admin so that data for those
# models can be created, deleted, updated and queried through the user interface.
# To display your models in the Django admin panel. 
admin.site.register(Known)
admin.site.register(Criminal)
admin.site.register(Unknown)
