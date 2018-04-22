# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=140)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=500)
