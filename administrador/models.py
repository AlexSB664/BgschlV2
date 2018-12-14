from django.db import models
from django.utils import timezone
from datetime import datetime    
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    nombre = models.CharField(max_length=65, null=True)
    apellido_paterno = models.CharField(max_length=65,null=True)
    apellido_materno = models.CharField(max_length=65,null=True)
    fecha_nacimiento = models.DateTimeField(null=True)
    genero = models.CharField(max_length=65,null=True)
    foto_perfil = models.ImageField(upload_to='profiles',null=True)
    verificado = models.BooleanField(default=False)
    agregado = models.DateTimeField(default=datetime.now, blank=True)
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

class Administrador(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    agregado = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.email.nombre
    
    class Meta:
        
        permissions = (
            ('is_admin', 'Is_Admin'),
        )
class Publicaciones(models.Model):
    admin = models.ForeignKey(Administrador, on_delete=models.CASCADE, blank=True, null=True,related_name="publicaciones")
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    contenido = models.TextField(null=True)
    foto = models.ImageField(upload_to='publicaciones',null=True)

    def __str__(self):
        return str(self.id+self.admin+self.fecha)