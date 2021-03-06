from django.urls import path
from .views import signupfunc, loginfunc, calendarfunc, CalendarCreate

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('calendar/', calendarfunc, name='calendar'),
    path('create/', CalendarCreate.as_view(), name="create"),
]