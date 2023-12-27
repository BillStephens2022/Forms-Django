from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .forms import ReviewForm
from .models import Review

# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
            "form": form
        })

# removed this code block once implementing a class based view approach
# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#              # removed code block below after replacing manual form with a ModelForm
#             # review = Review( 
#             #     user_name=form.cleaned_data['user_name'], 
#             #     review_text=form.cleaned_data['review_text'], 
#             #     rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    

# commented out code below since replaced with class based approach above.
# def thank_you(request):
#     return render(request, "reviews/thank_you.html")
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    # the below sets the name of the context object so that you can use it in the template with this name
    # by default, if no name is given for this, you need to use 'object_list' in the template
    # therefore, "reviews" will be the name of the data exposed to the template
    context_object_name = "reviews"


    # you can also customize the data returned by adjusting the queryset.  
    # Below example would only return reviews with a rating > 4

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    