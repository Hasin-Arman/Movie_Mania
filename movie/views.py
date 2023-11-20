from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView,DeleteView,DetailView
from .models import movieModel,ReviewModel
from .forms import MovieForm,ReviewForm
from django.views.generic import FormView
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class movie_view(ListView):
    model= movieModel
    template_name='movies.html'
    
    def get_context_data(self, **kwargs):
        searched = self.request.GET.get('search')
        context = super().get_context_data(**kwargs)
        if searched:
            context["movie"] = movieModel.objects.filter(title__icontains=searched)
        else:
            context["movie"] = movieModel.objects.all()
        return context
    
    def get_template_names(self):
        if self.request.user.is_staff:
            return ["movie_staff.html"]
        else:
            return [self.template_name]
        return super().get_template_names()

class add_movie_view(LoginRequiredMixin,FormView):
    login_url = 'signin'
    form_class = MovieForm
    template_name = "add_movie.html"
    success_url= reverse_lazy('movie')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class update_movie(LoginRequiredMixin,UpdateView):
    login_url = 'signin'
    model=movieModel
    template_name='add_movie.html'
    form_class=MovieForm
    success_url=reverse_lazy('movie')

class delete_movie(LoginRequiredMixin,DeleteView):
    login_url = 'signin'
    model=movieModel
    template_name='del_confirm.html'
    success_url=reverse_lazy('movie')

def movie_details(request,id):
    movie=movieModel.objects.get(id=id)
    reviews=ReviewModel.objects.filter(movie=movie)
    if request.user.is_authenticated:
        user_review=ReviewModel.objects.filter(user=request.user)
        return render(request,'movie_details.html',{'movie':movie,'reviews':reviews,'user_review':user_review})
    else:
        return render(request,'movie_details.html',{'movie':movie,'reviews':reviews})

def submit_review(request,movieId):
    movie=movieModel.objects.get(id=movieId)
    if request.method == 'POST':	
        if request.user.is_authenticated:
            review=ReviewModel()
            review.user=request.user
            review.movie=movie
            review.text=request.POST.get('review')
            review.rating=request.POST.get('rating')
            review.save()
            return HttpResponseRedirect(reverse('detail_movie', kwargs={'id': movie.id}))
        else:
            messages.error(request, 'please login first')
    return HttpResponseRedirect(reverse('detail_movie', kwargs={'id': movie.id}))

class update_review(LoginRequiredMixin,UpdateView):
    login_url = 'signin'
    model=ReviewModel
    template_name='update_review.html'
    form_class=ReviewForm
    success_url=reverse_lazy('movie')
    
class delete_review(LoginRequiredMixin,DeleteView):
    login_url = 'signin'
    model=ReviewModel
    template_name='del_confirm.html'
    success_url=reverse_lazy('movie')

def category_filter(request, category):
    if category:
        movies=movieModel.objects.filter(category=category)
    else:
        movies=movieModel.objects.all()
        
    if request.user.is_staff:
        return render(request,'movie_staff.html',{'movie':movies})
    
    return render(request,'movies.html',{'movie':movies})