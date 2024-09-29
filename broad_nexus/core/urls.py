from django.urls import path
from .views import HomeView,job_apply,JobDetailView,MyJobView,ContactView

urlpatterns = [
    path("job-apply/<str:uuid>/", job_apply, name='job_apply'),
    path("job-detail/<str:uuid>/", JobDetailView.as_view(), name="job_detail"),
    path('my-jobs/', MyJobView.as_view(), name="my_job"),
    path('contact/', ContactView.as_view(), name='contact'),
    path("", HomeView.as_view(), name='home')

]