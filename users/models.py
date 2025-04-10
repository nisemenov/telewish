import uuid
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower",
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following",
    )

    class Meta:
        unique_together = ["user", "following"]
