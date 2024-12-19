from django.urls import path
from eeg_app import views

urlpatterns = [
    path('eeg/', views.display_eeg_data, name='display_eeg_data'),
]
