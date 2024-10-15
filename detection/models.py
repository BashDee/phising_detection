from django.db import models

class PhishingLog(models.Model):
    features = models.CharField(max_length=255)
    result = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.result} - {self.created_at}"
