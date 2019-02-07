from rest_framework import serializers
from .models import Student, Course, StudentToCourse

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)

    def create(self, data):
        return Student.objects.create(**data)

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.save()
        return instance


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=100)
    start_date = serializers.DateField(required=True)

    def create(self, data):
        return Course.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.start_date = data.get('start_date', instance.start_date)
        instance.save()
        return instance
        
class StudentToCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    student_id = serializers.IntegerField(required=True)
    course_id = serializers.IntegerField(required=True)

    def create(self, data):
        return StudentToCourse.objects.create(**data)

    def update(self, instance, data):
        instance.student_id = data.get('student_id', instance.student_id)
        instance.course_id = data.get('course_id', instance.course_id)
        instance.save()
        return instance