from django.urls import path
from .views import start_research, research_history

urlpatterns = [
    path('start/', start_research),
    path('history/', research_history),
]
