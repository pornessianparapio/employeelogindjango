from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name

class Activity(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.employee.name} - {self.name}"

class TimeEntry(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    days = models.IntegerField()
    hours = models.IntegerField()
    minutes = models.IntegerField()
    seconds = models.IntegerField()

    def __str__(self):
        return f"{self.activity.name} - {self.start_time} to {self.end_time}"
