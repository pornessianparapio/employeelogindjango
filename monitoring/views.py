from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Activity
from .serializers import EmployeeSerializer, ActivitySerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView

class LoginView(APIView):
    def post(self, request):
        # e_id = None
        email = request.data.get('email')
        password = request.data.get('password')
        print(f'{email}  {password}')
        user = Employee.objects.get(email=email)
        print(user.email)
        print(user.password)
        print(user.pk)
        if user.password == password:
            return Response(data=user.pk, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)





        # if e_id is not None:
        #     return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        # else:
        #     return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST','PUT'])
def activity_list(request):
    if request.method == 'GET':
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    # elif request.method == 'PUT':
    #     serializer = ActivitySerializer(activities, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = ActivitySerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def activity_detail(request, pk):
    try:
        activity = Activity.objects.get(pk=pk)
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActivitySerializer(activity, data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
