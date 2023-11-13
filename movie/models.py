from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
movie_category =(
    ('Thriller','Thriller'),
    ('Sci-fi','Sci-fi'),
    ('Action','Action'),
    ('Horror','Horror'),
    ('Romance','Romance'),
    ('Comedy','Comedy')    
)
class movieModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    category=models.SlugField(max_length=100,choices=movie_category,default='Action')
    image=models.ImageField(upload_to='movie/images')
    
    def __str__(self):
        return self.title
    

    
class ReviewModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(movieModel,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    rating=models.PositiveIntegerField(default=0)
    text=models.CharField(max_length=250)
    
    def __str__(self):
        return self.movie.title
    