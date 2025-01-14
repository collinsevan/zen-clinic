from django.shortcuts import render


# Create your views here.
def home(request):
    """
    Renders the home page.
    """
    return render(request, 'home.html')


def custom_login_view(request):
    """
    Handles the login page rendering.
    """
    return render(request, "account/login.html")
