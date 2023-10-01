from .models import ProjectField

def project_fields(request):
    return {'project_fields': ProjectField.objects.all()}
