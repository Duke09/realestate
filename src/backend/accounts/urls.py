from django.urls import path

from .views import SignupView

app_name = 'accounts'

# Urlpatterns
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
]