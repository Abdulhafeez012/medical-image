from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    FormView
)


class BaseView(TemplateView):
    template_name = 'base.html'


class LogInView(FormView):
    form_class = AuthenticationForm
    template_name = 'logIn.html'
    success_url = reverse_lazy('main:user_home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


@login_required
def log_out(request):
    logout(request)
    return redirect('main:home')
