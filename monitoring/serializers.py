# from rest_framework import serializers
from datetime import datetime
from rest_framework import serializers
from .models import Employee, Activity, TimeEntry
class CustomDateTimeField(serializers.DateTimeField):
    def to_internal_value(self, value):
        try:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            self.fail('invalid', format='YYYY-MM-DD HH:MM:SS.ssssss', input=value)

    def to_representation(self, value):
        return value.strftime('%Y-%m-%d %H:%M:%S.%f')



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email']

class TimeEntrySerializer(serializers.ModelSerializer):
    start_time = CustomDateTimeField()
    end_time = CustomDateTimeField()

    class Meta:
        model = TimeEntry
        fields = ['id', 'start_time', 'end_time', 'days', 'hours', 'minutes', 'seconds']

class ActivitySerializer(serializers.ModelSerializer):
    start_time = CustomDateTimeField()
    end_time = CustomDateTimeField()
    time_entries = TimeEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        fields = '__all__'