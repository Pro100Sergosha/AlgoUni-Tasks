from django.urls import path
from .views import TimeViewerView

urlpatterns = [
    path('', TimeViewerView.as_view())    
]
