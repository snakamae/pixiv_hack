# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.db import models

# Create your models here.


class Log(models.Model):
    page_kind = models.CharField("ページ分類", max_length=15, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)