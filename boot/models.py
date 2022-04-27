from django.db import models

# Create your models here.

class Inquiry(models.Model):

  fullname = models.CharField(max_length=64)
  email = models.CharField(max_length=64)
  phonenumber = models.CharField(max_length=32)
  message = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

def __str__(self) -> str:
  return f"{self.id}. {self.title}"