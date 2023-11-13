from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import SignUpForm,SignInForm,UpdatePassForm
from django.views.generic.edit import FormView,UpdateView
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout

class SignUpView(FormView):
    template_name='signup.html'
    form_class=SignUpForm
    success_url=reverse_lazy('movie')
    
    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully')
        user=form.save()
        login(self.request, user)
        return super().form_valid(form)

class SignInView(View):
    def get(self,request):
        return render(request, 'SignIn.html',{'form':SignInForm})
    
    def post(self,request):
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user: 
            login(request, user)
            return redirect('movie')
        else:
            return render(request, 'SignIn.html',{'form':SignInForm,'error':'Invalid username or password'})

class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class change_password(View):
    def get(self, request):
        form=UpdatePassForm(request.user)
        return render(request, 'pass_change.html', {'form': form})
    
    def post(self, request):
        form=UpdatePassForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'password changed successfully')
        else:
            form=UpdatePassForm(request.user)
            return render(request, 'pass_change.html', {'form': form,'error':"Password didn't matched."})
        return render(request, 'pass_change.html', {'form': form})

class update_profile(UpdateView):
    model=User
    fields=['username', 'first_name', 'last_name', 'email']
    template_name='profile.html'
    success_url= reverse_lazy('home')
    