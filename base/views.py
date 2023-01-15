from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Song
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from django.http import FileResponse
# Create your views here.
from django.conf import settings
import os


def home(request):
    return render(request, 'base/FIRSTPAGE.html')


def add_song(request):
    if not request.user.is_authenticated:
        return redirect("BSMain")

    if request.method == 'POST':
        song = request.FILES.get('song')
        if song:
            new_song = Song(song_file=song, user=request.user)
            new_song.save()

        return redirect('Music')


def landingpage(request):
    return render(request, 'base/LandingPage.html')


def my_books(request):
    if not request.user.is_authenticated:
        return redirect("BSMain")

    if request.method == "POST":
        name = request.POST.get("name")
        cover = request.FILES.get("cover")
        book_file = request.FILES.get("book_file")
        if name and cover and book_file:
            new_book = Book(
                name=name,
                cover=cover,
                book_file=book_file,
                user=request.user
            )
            new_book.save()

    all_books = Book.objects.filter(user=request.user)
    return render(request, "base/mybooks.html", {"all_books": all_books})


def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exsits! ')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('BSMain')

    context = {'page': page}
    return render(request, 'base/Login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    pass


def signuppage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpass')

        if User.objects.filter(username=username):
            messages.error(request, 'User already exsits!')
            return redirect('signup')
        else:
            if User.objects.filter(email=email):
                messages.error(request, 'Email already used!')
                return redirect('signup')
            else:
                if password != confirm_password:
                    messages.error(request, 'Password does not Match!')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    login(request, user)
                    return redirect('home')

    return render(request, 'base/signup.html')


def bsMain(request):

    return render(request, 'base/BSMain.html')


def bookSllider(request):
    page = 'books'
    context = {'page': page}
    return render(request, 'base/BSMain.html', context)


def Music(request):
    all_songs = Song.objects.filter(user=request.user)
    context = {
        'all_songs': all_songs
    }
    return render(request, 'base/musicplayer.html', context)
