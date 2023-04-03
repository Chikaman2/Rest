from rest_framework import serializers
from .models import Course

class CourseSerializers (serializers.HyperlinkedModelSerializer):
      class Meta:
            model = Course
            fields = ('id', 'url','name','language','price')