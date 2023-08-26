from django.contrib import admin
from django.urls import path
from ru import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about-us/', views.aboutUs),
    path('course/',views.Course),
    path('course/<courseid>', views.courseDetails),
]
