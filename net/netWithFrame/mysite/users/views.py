from django.shortcuts import render,redirect
from django.core.context_processors import csrf
from django.contrib.auth import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def user_login(request):
	ctx={}
	ctx.update(csrf(request))
	if request.POST:
		#form=authenticationForm(request.POST)
		username=password=''
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
			#return redirect('/')
			return render(request, 'result.html', ctx)
		#return diff_response(request)
		
	return render(request, 'login.html', ctx)

def user_logout(request):
	# URL: /users/logout
	logout(request)
	return redirect('/')

def diff_response(request):
	if request.user.is_authenticated():
		content="<p>my dear user</p>"
	else:
		content="<p>you stranger</p>"
	return HttpResponse(content)

@login_required
def user_only(request):
	return HttpResponse("<p>This message is for logged in user only.</p>")

def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			new_user=form.save()
		return redirect("/")
	else:
		form=UserCreationForm()
		ctx={'form': form}
		ctx.update(csrf(request))
		return render(request, "register.html",ctx)
