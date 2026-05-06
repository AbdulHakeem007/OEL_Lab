from django.shortcuts import render
def home(request):
 """Home page view renders the home template."""
 context = {
 'title': 'Welcome to My Portfolio',
 'name': 'Ahmed Khan',
 'skills': ['Python', 'Django', 'JavaScript', 'HTML/CSS', 'PostgreSQL'],
 'projects': [
 {'name': 'Weather App', 'desc': 'Real-time weather using OpenWeather API'},
 {'name': 'Blog Platform', 'desc': 'Full-featured blog with CRUD operations'},
 {'name': 'Task Manager', 'desc': 'Kanban-style productivity application'},
 ]
 }
 return render(request, 'home.html', context)
