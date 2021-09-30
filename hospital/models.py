from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    m_name=models.CharField(max_length=100,null=True)
    h_name=models.CharField(max_length=100,null=True)
    add = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return self.h_name

class Stats(models.Model):
    stats_name = models.CharField(max_length=30, null=True)
    stats_image = models.FileField(null=True)
    stats_num = models.IntegerField(null=True)

    def __str__(self):
        return self.stats_name

class Purpose(models.Model):
    purpose = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.purpose
class Doctor(models.Model):
    #stats = models.ForeignKey(Stats, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    o_time = models.CharField(max_length=50, null=True)
    o_days = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(null=True)
    special = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Gender(models.Model):
    type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.type

class Patient(models.Model):
    #stats = models.ForeignKey(Stats, on_delete=models.CASCADE, null=True)
    disease=models.CharField(max_length=50, null=True)
    rel=models.CharField(max_length=50, null=True)
    cnic=models.CharField(max_length=50, null=True)
    purpose = models.ForeignKey(Purpose,on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(null=True)
    payment = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    #stats = models.ForeignKey(Stats, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    date1 = models.DateField(null=True)
    time1 = models.TimeField(null=True)

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name

class Discharge(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    date1=models.DateField(null=True)
    time1=models.TimeField(null=True)
    payment_status=models.CharField(max_length=30,null=True)
    remaining = models.IntegerField(null=True)
    disease = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.patient.name

class Test(models.Model):
    test=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.test



class Testing(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    test = models.ForeignKey(Test,on_delete=models.CASCADE,null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    b_group = models.CharField(max_length=10,null=True)
    date1=models.DateField(null=True)
    delivery_date=models.DateField(null=True)
    payment=models.IntegerField(max_length=30,null=True)
    def __str__(self):
        return self.patient.name

