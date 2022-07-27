from django.db import models

# Create your models here.
class UsersInformation(models.Model):
    UserName = models.CharField(max_length=500)
    EmailAddress = models.CharField(max_length=500)
    PhoneNumber = models.IntegerField(primary_key=False)
    password = models.CharField(max_length=500)
    UserId = models.AutoField(primary_key=True)

class Organization(models.Model):
    OrganizationName = models.CharField(max_length=500)
    OrganizationId = models.AutoField(primary_key=True)

class Job(models.Model):
    JobTitle = models.CharField(max_length=500)
    JobId = models.AutoField(primary_key=True)
    OrganizationId = models.ForeignKey(Organization, on_delete=models.CASCADE)
    #Salary = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    Location = models.CharField(max_length=500)
    Experience_required = models.IntegerField(primary_key=False)
    Skills_required = models.CharField(max_length=3000)
    EmployerId = models.ForeignKey(UsersInformation, on_delete=models.CASCADE)

class Experience(models.Model):
    UserId = models.ForeignKey(UsersInformation, on_delete=models.CASCADE)
    ExperienceId = models.AutoField(primary_key=True)
    OrganizationId = models.ForeignKey(Organization, on_delete=models.CASCADE)
    Title = models.CharField(max_length=500)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    work_or_education = models.BooleanField()
    

class Application(models.Model):
    JobId = models.ForeignKey(Job, on_delete=models.CASCADE)
    ApplicationId = models.AutoField(primary_key=True)
    ApplicantId = models.ForeignKey(UsersInformation, on_delete=models.CASCADE)
    Status = models.CharField(max_length=500)