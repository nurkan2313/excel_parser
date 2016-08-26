# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Пользователь')
    first_name = models.CharField(u'Имя', max_length=255)
    last_name = models.CharField(u'Фамилия', max_length=255)
    create_add = models.DateTimeField(u'Профиль был создан: ', auto_now_add=True)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User, dispatch_uid="create_profile")
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
