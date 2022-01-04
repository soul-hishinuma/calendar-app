from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import EventsModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, password)
            redirect('login')
        except IntegrityError:
            print('this is already used')
            return render(request, 'signup.html', {"error":"このユーザー名は既に使用されています。"})
    return render(request, 'signup.html', {})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('calendar')
        else:
            return render(request, 'login.html', {'context': 'loginに失敗しました。'})
    return render(request, 'login.html', {})

def calendarfunc(request):
    event_list = EventsModel.objects.all()
    return render(request, 'calendar.html', {"event_list" : event_list})

class CalendarCreate(CreateView):
    template_name = "create.html"
    model = EventsModel
    fields = ('event_name', 'start_date', 'end_date')
    success_url = reverse_lazy('calendar')