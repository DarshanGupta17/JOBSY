# decorators.py
from django.http import HttpResponseForbidden
from django.shortcuts import redirect,render
from functools import wraps

def employer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_employer == True:
            return view_func(request, *args, **kwargs)
        else:
            return render(request,"404/404.html")
    return _wrapped_view

def jobseeker_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_jobseeker == True:
            return view_func(request, *args, **kwargs)
        else:
            return render(request,"404/404.html")
    return _wrapped_view

