from django import forms

class ExampleForm(forms.Form):
    """
    Form used to demonstrate security best practices like 
    CSRF protection and data sanitization.
    """
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)