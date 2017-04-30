# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)
    username = models.CharField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, balnk=False)
    short_bio = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)