from django import forms
from .models import Category


cat = [(1, "hello"), (2, "hello2")]

def categories():
    # Convert list to indexed tuple list
    all_categories = Category.objects.all()
    list_tuple = []
    for i in range(0, len(all_categories)):
        list_tuple.append((i, all_categories[i].name))
    return list_tuple

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class PostsForm(forms.Form):
    title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Add title"
        })
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Add text"
            }
        )
    )
    #category = forms.MultipleChoiceField(required=True, choices=categories)
    category=forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

