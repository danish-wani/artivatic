from rest_framework import serializers
from .models import Student, ContactInfo, Subject


class ContactInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactInfo
        fields = ('phone_number', 'address', 'email')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    subject = SubjectSerializer(write_only=True)
    contact_info = ContactInfoSerializer(write_only=True)

    class Meta:
        model = Student
        fields = ('id','name', 'reg_no', 'subject', 'contact_info')

    def create(self, validated_data):
        contact_info = validated_data.pop('contact_info')

        subject = validated_data.pop('subject')

        subject_instance = Subject.objects.create(**subject)
        student, created = Student.objects.get_or_create(**validated_data)

        student.subjects.add(subject_instance)
        contact_serializer = ContactInfoSerializer(data=contact_info)
        contact_serializer.is_valid()

        ContactInfo.objects.get_or_create(
            phone_number=contact_serializer.validated_data['phone_number'],
            address=contact_serializer.validated_data['address'],
            email=contact_serializer.validated_data['email'],
            student=student
        )

        return student

