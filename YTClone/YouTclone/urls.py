from django import views
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name="YTHome"),
    path('video/',views.video,name="YTVideo"),
    path('explore/',views.explore,name="YTexplore"),
    path('subscription/',views.subscription,name="YTsubscription"),
    path('originals/',views.originals,name="YToriginals"),
    path('music/',views.music,name="YTmusic"),
    path('library/',views.library,name="YTlibrary"),
    path('search/',views.search,name="YTsearch"),
    path('create/',views.create,name="YTcreate"),
    path('menu/',views.menu,name="YTmenu"),
    path('notifications/',views.notifications,name="YTnotifications"),
    path('userprofile/',views.userprofile,name="YTuserprofile"),
]