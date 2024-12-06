from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('recipe:index')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'

    def get_success_url(self):
        user = self.object
        login(self.request, user)
        return reverse('recipe:index')