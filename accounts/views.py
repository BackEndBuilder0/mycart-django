from django.shortcuts import render



def register_page(request):
    if request.method == 'POST':
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))
        print(request.POST.get('email'))
        print(request.POST.get('gender'))
        print(request.POST.get('city'))
        print(request.POST.get('country'))
        print(request.POST.get('password'))
        print(request.POST.get('repeat_password'))
    return render(request, 'accounts/register.html')


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        print(request.POST.get('user_email'))
        print(request.POST.get('user_password'))
    return render(request, 'accounts/login.html')


