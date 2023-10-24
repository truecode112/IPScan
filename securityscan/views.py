from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View, FormView, UpdateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authtoken.models import Token

class BaseView( TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_logged_in'] = self.request.user.is_authenticated
        return context
    
class HomeView(BaseView):
    template_name = 'home.html'

class TargetView(BaseView):
    template_name = 'targets.html'

class ScanView(BaseView):
    template_name = 'scan.html'

class PricingView(BaseView):
    template_name = 'price.html'

class DashboardView(BaseView):
    template_name = 'dashboard.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class SignupView(TemplateView):
    template_name = 'signup.html'

def google_logout(request):
    logout(request)
    return redirect('home')
