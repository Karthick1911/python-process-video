from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=32, blank=False)
    file = models.FileField(blank=False, null=False, upload_to="video", validators=[FileExtensionValidator(allowed_extensions=['mp4'])] )
    timestamp = models.DateTimeField(auto_now_add=True)


# https://newbedev.com/only-accept-a-certain-file-type-in-filefield-server-side