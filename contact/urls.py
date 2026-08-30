from django.urls import path
from .views import ProjectEnquiryCreateView


urlpatterns = [
    path(
        'project-enquiry/',
        ProjectEnquiryCreateView.as_view(),
        name='project-enquiry'
    ),
]