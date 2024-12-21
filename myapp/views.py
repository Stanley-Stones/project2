from django.shortcuts import render, redirect, HttpResponse
from . models import Location, Listing, Profile
from django.contrib.auth.models import auth, User
from django.contrib import messages
from . forms import ListingForm, ProfileForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):

  '''if 'q' in request.GET:
    q = request.GET.get('q')

    listings = Listing.objects.filter(location__name__icontains=q)

  else:
    listings = Listing.objects.all()'''

  listings = Listing.objects.all()
  
  context = {'listings': listings}
  return render(request, 'home.html', context)


def search(request):

  '''if 'q' in request.GET:
    q = request.GET.get('q')

    listings = Listing.objects.filter(location__name__icontains=q)

  else:
    listings = Listing.objects.all()'''

  if 'q' in request.GET:
    q = request.GET.get('q')


  listings = Listing.objects.filter(location__name__icontains=q)

  context = {'listings': listings }
  return render(request, 'search.html', context)


def register(request):

  if request.user.is_authenticated:
    return redirect('homepage')

  code2 = '00000'

  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('pass1')
    password2 = request.POST.get('pass2')
    code1 = request.POST.get('code')

    if password == password2:
      if code1 == code2:

        if User.objects.filter(username=username).exists():
          messages.info(request, 'Username already Exist!')
          return redirect('register')
        else:
          user = User.objects.create_user(username=username, password=password)

          user = auth.authenticate(username=username, password=password)

          if user is not None:
            user = auth.login(request, user)
            return redirect('profile')
          else:
            messages.info(request, 'Account Not Found!')
            return redirect('login')

      else:
        messages.info(request, 'Code Does Not Exist! Contact The Company')
        return redirect('register')

    else:
      messages.info(request, 'Password Does Not Match!')
      return redirect('register')

  return render(request, 'register.html')


def login(request):

  if request.user.is_authenticated:
    return redirect('homepage')

  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      
      user = auth.login(request, user)
      return redirect('homepage')
    else:
      messages.info(request, 'Invalid Account!')
      return redirect('login')
  return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
  auth.logout(request)
  return redirect('homepage')


@login_required(login_url='login')
def create(request):

  form = ListingForm()

  if request.method == "POST":
    form = ListingForm(request.POST, request.FILES)
    if form.is_valid():

      form = form.save(commit=False)
      form.host = request.user
      form.save()
      return redirect('homepage')
    else:
      messages.info(request, 'Invalif Form')
      return redirect('property_create')

  context = {'form': form}
  return render(request, 'property_create.html', context)


def details(request, pk):
  listing = Listing.objects.get(id=pk)

  context ={'listing': listing}
  return render(request, 'property_details.html', context)


@login_required(login_url='login')
def update(request, pk):

 
  listing = Listing.objects.get(id=pk)
  form = ListingForm(instance=listing)
  host = listing.host

  if request.user != host:
    return HttpResponse('get Out!')



  if request.method == "POST":
    form = ListingForm(request.POST, request.FILES, instance=listing)
    if form.is_valid():
      form.save()
      return redirect('homepage')
    else:
      messages.info(request, 'Invalid!')
      return redirect('homepage')
  return render(request, 'property_update.html', {'form': form})


@login_required(login_url='login')
def delete(request, pk):

  if request.user != Listing.host:
    return HttpResponse('You cannot delete this')

  listing = Listing.objects.get(id=pk)
  listing.delete()
  return redirect('homepage')


@login_required(login_url='login')
def profile(request):

  form = ProfileForm()

  if request.method == "POST":
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      form = form.save(commit=False)

      form.name = request.user.username
      form.id = request.user.id

      form.save()
      return redirect('homepage')
    else:
      messages.info(request, 'Something Went WRong!')
      return redirect('profile')

  context = {'form': form}
  return render(request, 'profile.html', context)