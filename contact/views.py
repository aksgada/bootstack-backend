from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings
from django.core.mail import send_mail

from .models import ProjectEnquiry
from .serializers import ProjectEnquirySerializer


class ProjectEnquiryCreateView(generics.CreateAPIView):

    queryset = ProjectEnquiry.objects.all()
    serializer_class = ProjectEnquirySerializer

    def create(self, request, *args, **kwargs):

        # Validate form data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save enquiry
        enquiry = serializer.save()

        email_sent = False
        email_error = None

        try:

            send_mail(
                subject=f"New Project Enquiry - {enquiry.name}",

                message=f"""
You have received a new project enquiry.

--------------------------------
PROJECT ENQUIRY
--------------------------------

Name:
{enquiry.name}

Email:
{enquiry.email}

Phone:
{enquiry.phone}

Requirement:
{enquiry.requirement}

Submitted:
{enquiry.created_at}

--------------------------------
Bootstack Website
--------------------------------
""",

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[
                    settings.PROJECT_ENQUIRY_EMAIL
                ],

                fail_silently=False,
            )

            email_sent = True

            print("EMAIL SENT SUCCESSFULLY")

        except Exception as e:

            email_error = str(e)

            print("====================================")
            print("EMAIL ERROR:")
            print(repr(e))
            print("====================================")

        return Response(
            {
                "message": "Enquiry submitted successfully.",

                "email_sent": email_sent,

                "email_error": email_error,

                "data": serializer.data,
            },

            status=status.HTTP_201_CREATED,
        )