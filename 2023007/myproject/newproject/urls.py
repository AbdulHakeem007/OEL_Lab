from csv import reader
from django.urls import path
from . import views
urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('contact/', views.contact, name='contact'),
]
def about(request):
 """About page view."""
 context = {
 'title': 'About Me',
 'bio': 'I am  a Software Engineer.',
 }
 return reader(request, 'about.html', context)

def contact(request):
 """Contact page view."""
 context = {'title': 'Contact Me'}
 return reader(request, 'contact.html', context)
