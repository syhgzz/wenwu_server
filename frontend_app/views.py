
# Create your views here.

import os
from django.shortcuts import render
from django.conf import settings
import requests


# 前端网页例子
def frontend(request):

    return render(request,'frontend.html')