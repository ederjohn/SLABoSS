# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import SLA, Term

# Register your models here.

admin.site.register(SLA)
admin.site.register(Term)


