from django.urls import path 
from .views import JobListPost , ApplicationList , JobDetails , ApplicationPost 

urlpatterns = [
    path('', JobListPost.as_view()),
    path('<int:pk>/', JobDetails.as_view()),
    path('<int:id>/apply/', ApplicationPost.as_view()),
    path('applications/', ApplicationList.as_view()),
    # path('TestRelated/', TestRelated.as_view()),
]