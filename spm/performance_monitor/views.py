from django.shortcuts import render
from django.http import HttpResponse


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


    chartN = 'Department-wise PLO'
    chartL = [] # ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    chartD = [] # [2, 10, 5, 3, 20, 30, 45]
    
    row = getDepartmentWisePLO('CSE')
    
    for i in row:
        chartL.append(i[1])
        chartD.append(i[2])
    
    chartName.append(chartN)
    chartLabel.append(chartL)
    chartDataSet.append(chartD)
    
    numberOfGraphs = len(chartName)

