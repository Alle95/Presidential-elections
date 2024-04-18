from django.db import models
from django.contrib.auth.models import User

class text(models.Model):
    user = models.ForeignKey(
        User, related_name="description",
        on_delete=models.DO_NOTHING
        )
    content = models.TextField()

    def __str__ (self):
        return(
            f"{self.content}"
        )
