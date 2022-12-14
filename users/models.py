from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    phone = CharField(max_length=25, null=True, blank=True)
    email = EmailField(max_length=255, unique=True)

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):

        count = User.objects.count()
        while User.objects.filter(pk=count).exists():
            count += 1
        self.username = f'user-{count + 1}'

        super().save(*args, **kwargs)

