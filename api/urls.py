from django.urls import path
from .views import HomeView, All_ques_view, QueryView

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path("query", QueryView.as_view(),name='query'),
    path('api', All_ques_view.as_view(),name='api'),
]
