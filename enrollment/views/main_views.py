# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Course, Student, StudentToCourse
from ..serializers import CourseSerializer, StudentSerializer, StudentToCourseSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

class ViewSwitch():
    # TODO: add in results stats at top of response, eg. results_count,

    @staticmethod
    @csrf_exempt
    @api_view(['GET', 'POST'])
    def view_list(request, object_type, serializer):
        if request.method == 'GET':
            results = object_type.objects.all().order_by('id')
            serialized_data = serializer(results, many=True)
            return Response(serialized_data.data)

        elif request.method == 'POST':
            serialized_data = serializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serialized_data.data, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @csrf_exempt
    @api_view(['GET','DELETE', 'PUT'])
    def view_detail(request, pk, object_type, serializer):
        try:
            # student_to_course = StudentToCourse.objects.get(pk=pk)
            results = object_type.objects.get(pk=pk)
        except:
            return Response({"error":"Bad Request: The enrollment you requested, doesn't exist."}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serialized_data = serializer(results)
            return Response(serialized_data.data)

        elif request.method == 'DELETE':
            results.delete()
            return Response({'success':"Enrollment {0} was destroyed.".format(pk)}, status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            serialized_data = serializer(results, data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data)
            else:
                return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @csrf_exempt
    def type_handler(request, pk=False):
        if pk != False:
            # With IDs
            if request.path.find('course') != -1:
                return __class__.view_detail(request, pk, Course, CourseSerializer)
            elif request.path.find('student') != -1:
                return __class__.view_detail(request, pk, Student, StudentSerializer)
            elif request.path.find('enroll') != -1:
                return __class__.view_detail(request, pk, StudentToCourse, StudentToCourseSerializer)
            else:
                return Response({'error':'Invalid Request'}, status=status.HTTP_404_NOT_FOUND)
        else:
            if request.path == '/course/':
                return __class__.view_list(request, Course, CourseSerializer)
            elif request.path == '/student/':
                return __class__.view_list(request, Student, StudentSerializer)
            elif request.path == '/enroll/':
                return __class__.view_list(request, StudentToCourse, StudentToCourseSerializer)
            else:
                return Response({'error':'Invalid Request'}, status=status.HTTP_404_NOT_FOUND)
