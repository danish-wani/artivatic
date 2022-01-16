from django.urls import path
from .views import CreateStudentAPI, RetrieveUpdateDestroyStudentAPI


urlpatterns = [

    path('students', CreateStudentAPI.as_view(), name='create_student_api'),
    path('students/<int:pk>', RetrieveUpdateDestroyStudentAPI.as_view(), name='retrieve_update_delete_student_api'),

]
