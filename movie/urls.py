from django.urls import path
from . import views
urlpatterns = [
    path('movie/',views.movie_view.as_view(),name='movie'),
    path('add-movie/',views.add_movie_view.as_view(),name='add_movie'),
    path('update-movie/<int:pk>/',views.update_movie.as_view(),name='update_movie'),
    path('delete-movie/<int:pk>/',views.delete_movie.as_view(),name='delete_movie'),
    path('delete-review/<int:pk>/',views.delete_review.as_view(),name='delete_review'),
    path('detail-movie/<int:id>/',views.movie_details,name='detail_movie'),
    path('review/<int:movieId>/',views.submit_review,name='review'),
    path('update_review/<int:pk>/',views.update_review.as_view(),name='update_review'),
    path('category/<slug:category>/',views.category_filter,name='category'),
]
