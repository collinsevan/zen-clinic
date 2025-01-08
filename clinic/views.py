from django.shortcuts import render


# Create your views here.
def base(request):
    """
    Renders the base template.
    """
    return render(request, 'base.html')
