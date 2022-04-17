from django.views.generic import UpdateView, DetailView
from django.contrib.auth.models import User, Group
from .forms import UserForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/account/')
