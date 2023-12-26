from django.urls import path

from . import views

urlpatterns = [
  path("", views.ReviewView.as_view()),  # updated for class based approach
  # path("", views.review),  # removed once started using class based approach
  path("thank-you", views.thank_you)
]