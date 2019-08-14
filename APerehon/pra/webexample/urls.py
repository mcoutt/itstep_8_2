from django.urls import path
from . import views

urlpatterns = [
# path('postfix  url',views.name_func_for_answer_postfix_url )
path('', views.hello),
path('webexample/', views.webexample, )
]
