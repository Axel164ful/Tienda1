from django.urls import path, include

from . import views


app_name = 'citas'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('loger', views.LogeView.as_view(), name='logeador'),

    path('edicion', views.EdicionFormView.as_view(), name='edicion' ),

    path('edicion_2', views.EdicionFormView2.as_view(), name='edicion_2'),

    path('<review>', views.ResenaView.as_view(), name='resena'),

    

   
]


