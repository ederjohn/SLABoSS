# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SLA(models.Model):
    description = models.CharField(max_length=500)
    service = models.CharField(max_length=500)
    penalty = models.IntegerField()
    price = models.IntegerField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    agreedAt = models.DateTimeField()
    
    def __str__ (self):
        return self.description + " - " + self.service

class Term(models.Model):
    sla = models.ForeignKey(SLA, on_delete=models.CASCADE)
    term = models.IntegerField() #have to define 1 for jitter, 2 for throgput and so on
    performanceLevel = models.IntegerField() #50
    operator = models.IntegerField() #>= < =
    currentValue = models.IntegerField(default=0)
    def __str__ (self):
        return str(self.term) + " " + str(self.operator) + " " + str(self.performanceLevel)
