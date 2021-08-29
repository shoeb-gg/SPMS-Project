from django.shortcuts import render

from performance_monitor.graphquery import *
from performance_monitor.models import Cse303ObeMarkSheetMarks


# Create your views here.
def showFaculty(request):
    #students = Cse303ObeMarkSheetMarks.objects.raw("SELECT * FROM `cse303_obe_mark_sheet__marks_`")

    
    return render(request, 'facultyDataEntry.html')
     
def showLogIn(request):
    #students = Cse303ObeMarkSheetMarks.objects.raw("SELECT * FROM `cse303_obe_mark_sheet__marks_`")

    
    return render(request, 'logIn.html')

# Student Dashboard

def studentDashboard(request):
    chartName = []
    chartLabel = []
    chartDataSet = []
    
    chartN = 'Student-wise PLO'
    chartL = []
    chartD = []
    
    student_id = request.user.username
    print(str(student_id))
    
    row = getStudentWisePLO(student_id)
    
    for i in row:
        chartL.append(i[1])
        chartD.append(i[0])
    
    chartName.append(chartN)
    chartLabel.append(chartL)
    chartDataSet.append(chartD)
