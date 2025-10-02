from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('owner', 'Terminator'),
        ('admin', 'Administrator'),
        ('sysop', 'System Operator'),
        ('opera', 'Operator'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='viewer')

    def __str__(self):
        return f"{self.username} ({self.rol})"
        
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username']
    #email(unique=True)

