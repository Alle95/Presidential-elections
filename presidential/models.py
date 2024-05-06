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
    
class candidacy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.BooleanField(default=False)
    no_votes = models.IntegerField(default=0)
    voted = models.BooleanField(default=False)

    def __str__ (self):
        return(
            f"{self.user}"
        )
