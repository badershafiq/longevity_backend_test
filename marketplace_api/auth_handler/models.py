from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Partner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='partners')
    partner_name = models.CharField(max_length=256)
    partner_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.partner_name


class PartnerParameters(models.Model):
    """
    This would store the parameter a partner would be sending
    """
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='parameters')
    key = models.CharField(max_length=256)
    value = models.CharField(max_length=256)

    def __str__(self):
        return self.partner.partner_name