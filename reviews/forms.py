from django import forms
from .models import Review

# class ReviewForm(forms.Form): #manual creation of a form
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!"
#     }) 
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm): # automatic creation of form based on a model
    class Meta:  
        model = Review
        fields = "__all__" # includ all fields, otherwise you can pass an array with each field in quotes.  You can also use all and then use an exclude field to list all fields to be excluded
        # exclude = ['example_field']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }