from django.urls import path
from pokemon_app.views import HomePageView, TrainerList
from pokemon_app import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list/', TrainerList.as_view(), name='trainer-list'),
    ]
