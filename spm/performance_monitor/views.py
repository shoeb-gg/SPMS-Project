from django.shortcuts import render

from performance_monitor.models import Cse303ObeMarkSheetMarks


# Create your views here.
def showStudents(request):
    students = Cse303ObeMarkSheetMarks.objects.raw("SELECT * FROM `cse303_obe_mark_sheet__marks_`")

    
    return render(request, 'studentList.html', {'map': students})
     
