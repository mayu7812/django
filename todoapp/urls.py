from django.urls import path
from . import views

#urlの設定
urlpattaerns = [
  path("",views.taskList)
]