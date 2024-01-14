from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about/', views.aboutPage, name='aboutPage'),
    path('lessons/', views.lessonsPage, name='lessonsPage'),
    path('lesson/view/<int:pk>/', views.lessonDetail, name='lessonDetail'),
    path('video-materials/', views.videoPage, name='videoPage'),
    path('video/view/<int:pk>/', views.videoDetails, name='videoDetails'),
    path('presentations/', views.presentations, name='presentations'),
    path('presentation/view/<int:pk>/', views.presentationDetail, name='presentationDetail'),
    path('homeworks/', views.homeWorks, name='homeWorks'),
    path('homework/view/<int:pk>', views.homeWorkDetail, name='homeWorkDetail'),
    path('system/sign-up/', views.signUp, name='signUp'),
    path('system/login/', views.logIn, name='logIn'),
    path('system/logout/', views.logoutUser, name='logoutUser'),
]