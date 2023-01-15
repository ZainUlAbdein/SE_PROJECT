from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='flashpage'),
    path('home/', views.landingpage, name='home'),
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signuppage, name='signup'),
    path('BSMain', views.bsMain, name='BSMain'),
    path('Music/', views.Music, name='Music'),
    path('books/', views.bookSllider, name='books'),
    path('my-books', views.my_books, name="my-books"),
    path('add-song', views.add_song, name="add-song"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
