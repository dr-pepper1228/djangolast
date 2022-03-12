from django.urls import path
from . import views

app_name="vote"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('detail/<bpk>',views.detail,name="detail"),
    path('vote/<bpk>',views.vote,name="vote"),
    path('creply/<bpk>',views.creply,name="creply"),
    path('dreply/<bpk>/<rpk>',views.dreply,name="dreply"),
]