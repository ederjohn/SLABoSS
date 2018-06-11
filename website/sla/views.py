# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import SLA,Term

# Create your views here.
def index(request):
    all_slas = SLA.objects.all()
    context = {
        'all_slas': all_slas,
    }
    
    return render(request, 'sla/index.html',context)

def detail(request,sla_id):    
    try:
        sla = SLA.objects.get(id=sla_id)
        all_terms = sla.term_set.all
    except SLA.DoesNotExist:
        raise Http404("SLA does not exist")
    
    context = {
        'sla': sla,
        'all_terms': all_terms
    }

    return render(request, 'sla/detail.html',context)

def termDetail(request,sla_id,term_id):    
    try:
        sla = SLA.objects.get(id=sla_id)
    except SLA.DoesNotExist:
        raise Http404("SLA does not exist")
    try:
        term = sla.term_set.get(id=term_id)
    except Term.DoesNotExist:
        raise Http404("Term does not exist")
    
    context = {
        'sla': sla,
        'term': term
    }

    return render(request, 'sla/term_detail.html',context)