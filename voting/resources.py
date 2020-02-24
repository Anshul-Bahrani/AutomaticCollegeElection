from import_export import resources
from .models import Nominee

class NomineeResource(resources.ModelResource):
    class Meta:
        model = Nominee