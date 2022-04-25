from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    # home
    path('', include('app_top_keyword.urls')),
    # top keywords
    path('topword/', include('app_top_keyword.urls')),
    # app top persons
    path('topperson/', include('app_top_person.urls')),
    # top ner
    path('topner/', include('app_top_ner.urls')),
]
