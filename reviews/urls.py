from django.urls import path

from . import views

urlpatterns = [
  path("", views.ReviewView.as_view()),  # updated for class based approach
  # path("", views.review),  # removed since replaced using class based approach
  path("thank-you", views.ThankYouView.as_view()),
  # path("thank-you", views.thank_you) # removed since replaced using class based approach
  path("reviews", views.ReviewsListView.as_view()),
  path("reviews/<int:pk>", views.SingleReviewView.as_view())
]