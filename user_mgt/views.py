from django.shortcuts import render_to_response,redirect,RequestContext
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


def login_view(request):
    if request.user and request.user.is_authenticated():
        return HttpResponseRedirect('/blog/')
    else:
        if request.method=='POST':
            form = LoginForm(request.POST)
            user = authenticate(username=request.POST['username'],password=request.POST['password'])
            b = User.objects.get(username=request.POST['username'])
            if user is not None:
		    	if user.is_active:
		        	login(request,user)
		        	return HttpResponseRedirect('/blog/')
        form = LoginForm()
        return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))


@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/blog/')
