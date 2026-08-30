from rest_framework import serializers
from .models import ProjectEnquiry


class ProjectEnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectEnquiry
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'requirement',
            'created_at',
        ]

    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                "Name must contain at least 2 characters."
            )

        return value

    def validate_phone(self, value):
        phone = value.strip()

        if len(phone) < 10:
            raise serializers.ValidationError(
                "Please enter a valid phone number."
            )

        return phone