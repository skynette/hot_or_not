from django.shortcuts import render, redirect
from .models import Person, Hotvote, Notvote
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
	persons = Person.objects.all().order_by('hot_vote')
	context = {
		'persons': persons,
		"title":"Home",
	}
	return render(request, 'index.html', context)

def profile(request, username):
	person = Person.objects.get(user__username=username)
	if request.method == "POST":
		vote = request.POST['vote']
		if request.user.is_authenticated:
			v = vote.objects.get_or_create(user=request.user, Person=person)
			v.save()
			return redirect('/')
		return redirect('login')

	context = {
		"person":person,
		"title": "profile page",
	}
	return render(request, 'profile.html', context)

def edit_profile(request, username):
	person = Person.objects.all().filter(user__username=username)
	context={
		"person":person,
	}
	return render(request, 'profile.html', context)

def register(request):
	if request.method == "POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']
		username = username.lower()
		
		if User.objects.filter(username=username).exists():
			messages.warning(request, "Username already exists")
		
		elif User.objects.filter(email=email).exists():
			messages.warning(request, "Email already taken")
		
		elif password != password2:
			messages.warning(request, "Passwords do not match")

		user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
		p = Person.objects.create(user=user)
		messages.success(request, "Successfully registered, proceed to login")
		return redirect("login")
	context = {"title":"Register"}
	return render(request, 'register.html', context)

def login_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			messages.success(request, "Successfully logged in")
			login(request, user)
			return redirect('/')
		else:
			messages.warning(request, "Invalid credentials")
	context = {"title":"Login"}
	return render(request, 'login.html', context)

def logout_view(request):
	logout(request)
	return redirect('/')
	