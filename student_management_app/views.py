from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render

from student_management_app.EmailBackEnd import EmailBackEnd


# Create your views here.
def demo(request):
    return render(request, 'demo.html')


def showLoginPage(request):
    return render(request, 'login_page.html')


def doLogin(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                         password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return HttpResponse("Email:"+request.POST.get('email')+" password"+request.POST.get('password'))
        else:
            HttpResponse("Invalid Login")
