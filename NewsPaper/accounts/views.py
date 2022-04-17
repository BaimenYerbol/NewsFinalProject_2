from django.views.generic import UpdateView, DetailView
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account.html'
    context_object_name = 'account'
    login_url = '/login/'
    success_url = '/account/'

    def get_object(self, **kwargs):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'account_edit.html'
    form_class = UserForm
    login_url = '/login/'
    success_url = '/account/'

    def get_object(self, **kwargs):
        return self.request.user