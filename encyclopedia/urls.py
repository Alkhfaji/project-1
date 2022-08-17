from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>/', views.entry, name="entry"),
    path('random/', views.randomEntry, name="random"),
    path('new/', views.new, name="new"),
    path('new/save/', views.entrySave, name="new_save"),
    path('edit/save/', views.entryEdit, name="edit_save"),
    path('edit/<str:title>/', views.edit, name="edit"),
    path('search/', views.search, name="search"),
    # path('searchResults/', views.searchResults, name="searchResults"),
]
