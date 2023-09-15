# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from  django.views import View

from django.shortcuts import render

# Create your views here.
class RegisterView(View):
    def get(self,request):
        return render(request,"register.html")