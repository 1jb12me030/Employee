from rest_framework import serializers
from .models import Employee, AddressDetails, WorkExperience, Qualification, Project

class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    addressDetails = AddressDetailsSerializer()
    workExperience = WorkExperienceSerializer()
    qualifications = QualificationSerializer()
    projects = ProjectSerializer()

    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1
