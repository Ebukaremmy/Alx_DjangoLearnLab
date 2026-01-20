from django.shortcuts import render
from .forms import ExampleForm

# ... Keep your existing can_view/can_edit views here ...

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Data is sanitized by the form class
            title = form.cleaned_data['title']
            # Process safely...
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})