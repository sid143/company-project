from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

# authentication related stuff lives here
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.utils.decorators import method_decorator
from .forms import *
from .models import Login,EmployeeModel


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        obj = super().get_context_data()
        obj['loginForm'] = LoginForm()
        return obj

    def get_queryset(self):
        return Login.objects.all()

    def post(self, request):

        form = LoginForm(request.POST)
        if form.is_valid():
            Login.objects.create(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            )

            return HttpResponseRedirect('/company')

    # common to both get and post
        context = {
        'form' : form
            }
        return render(request,'sidd/newhtml.html', context)    


    @method_decorator(login_required) # we can use multiple decorators here
    def dispatch(self, request):
        return super().dispatch(request)
 

def login_view(request):
    login_error = ""

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == "GET":
            loginForm = LoginForm()
    elif request.method == "POST":
            loginForm = LoginForm(request.POST)
    if loginForm.is_valid():
        username = loginForm.cleaned_data['username']
        password = loginForm.cleaned_data['password']

            # authenticate here
        user = authenticate(username = username, password = password)

        if user is not None:
                # user authenticated
            login(request, user)
            try:
                next_page = request.GET['next']
                return HttpResponseRedirect(next_page)
            except:
                return HttpResponseRedirect('/')
            else:
                # wrong credentials
                login_error = "Username/Password incorrect"
    
    context = {
    'loginForm' : loginForm,
    'login_error' : login_error
    }
    return render(request, 'company.html', context)

class EmployeeView(TemplateView):
    template_name = 'mainemployee.html'

class CompanyView(TemplateView):
    template_name = 'newhtml.html'

class ProfessView(TemplateView):
    template_name = 'profess.html'
