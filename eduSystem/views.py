from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import*
from .models import Student, Teacher ,Subject
from django.views.generic.list import ListView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]



class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]

class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    model = Teacher
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    #permission_classes = [permissions.IsAuthenticated]


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    model = Subject
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    #permission_classes = [permissions.IsAuthenticated]



class StudentDataList(ListView):
    model = Student
    template_name = 'student_list.html'
    #context_object_name = 'object_list'
    
    
    def dispatch(self, request, *args, **kwargs):
        return super(StudentDataList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(StudentDataList,self).get_queryset()
        queryset = Student.objects.all()
        return queryset


