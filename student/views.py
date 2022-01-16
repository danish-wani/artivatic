from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializer
from .models import ContactInfo, Student


class CreateStudentAPI(CreateAPIView):
    serializer_class = StudentSerializer


class RetrieveUpdateDestroyStudentAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def perform_destroy(self, instance):
        ContactInfo.objects.filter(student=instance).delete()
        instance.delete()
