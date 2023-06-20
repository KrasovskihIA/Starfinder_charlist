from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required


# Представление для входа на аккаунт
class Login(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('character_list'), request)
        print(form.cleaned_data)
        return render(request, self.template_name, context={'form': form})

# Выход из системы
@login_required
def logout_views(request):
    logout(request)
    return redirect(reverse('character_list'))


# Представление для регистрации
class CreateView(View):
    template_name = ''
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form':self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        registered = False
        context = {}
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data['email']
            user.save()
            registered = True
        else:
            context.update({'form':form})
        context.update({'registered':registered})
        return render(request, self.template_name, context=context)