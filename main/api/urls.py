from django.urls import path
from .views import (
    ContactView, 
    ProjectView, 
    AboutView, 

)

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('projects/', ProjectView.as_view(), name='projects'),
    path('about/', AboutView.as_view(), name='about'),

]