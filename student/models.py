from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=20)
    subjects = models.ManyToManyField('Subject')

    class Meta:
        db_table = "Student"

    def __str__(self):
        return str(self.name)


class ContactInfo(models.Model):

    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        db_table = "ContactInfo"

    def __str__(self):
        """

        """
        return str(self.address)


class Subject(models.Model):

    name = models.CharField(max_length=15)
    marks = models.FloatField()

    class Meta:
        db_table = "Subject"

    def __str__(self):
        """

        """
        return str(self.name)
