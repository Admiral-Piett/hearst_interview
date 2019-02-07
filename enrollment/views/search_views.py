import re

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Course, Student, StudentToCourse
from ..serializers import CourseSerializer, StudentSerializer, StudentToCourseSerializer


class ViewSwitch():

    @staticmethod
    @csrf_exempt
    @api_view(['GET'])
    def view_search(request, search_type, search_values, object_type, serializer):
        # Student
        if search_type == 'name':
            # results = object_type.objects.all().order_by('id')
            results = object_type.objects.filter(name__in=search_values)
            serialized_data = serializer(results, many=True)
            return Response(serialized_data.data)
        # Course
        elif search_type == 'title':
            results = object_type.objects.filter(title__in=search_values)
            serialized_data = serializer(results, many=True)
            return Response(serialized_data.data)
        elif search_type == 'start_date':
            results = object_type.objects.filter(start_date__in=search_values)
            serialized_data = serializer(results, many=True)
            return Response(serialized_data.data)
        # Enrollment
        # TODO: Add in title/name values to response
        elif search_type == 'student':
            results = object_type.objects.filter(student__in=search_values)
            serialized_data = serializer(results, many=True)
            return Response(serialized_data.data)
        elif search_type == 'course':
            results = object_type.objects.filter(course__in=search_values)
            serialized_data = serializer(results, many=True)
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.data, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @csrf_exempt
    def type_handler(request):
        params = dict(request.GET)
        # This searches for matching params to what's configured in the db, if it finds a match it searches on it through the view_search method
        # TODO: make this all configurable and not hardcoded
        r = [re.search('title|start_date|name|enrollment|student|course', v) for v in params.keys()]
        
        try:
            matched_key = r[0].string
        except:
            return JsonResponse({'error':'Invalid Request - No Search Parameters Provided'}, status=status.HTTP_404_NOT_FOUND)

        if matched_key == None:
            return JsonResponse({'error':'Invalid Request - No Search Parameters Provided'}, status=status.HTTP_404_NOT_FOUND)
        elif request.path.find('course') != -1:
            return __class__.view_search(request, matched_key, params[matched_key], Course, CourseSerializer)
        elif request.path.find('student') != -1:
            return __class__.view_search(request, matched_key, params[matched_key], Student, StudentSerializer)
        elif request.path.find('enroll') != -1:
            return __class__.view_search(request, matched_key, params[matched_key], StudentToCourse, StudentToCourseSerializer)
        else:
            return JsonResponse({'error':'Invalid Request'}, status=status.HTTP_404_NOT_FOUND)

        