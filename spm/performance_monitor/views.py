from django.http import HttpResponse
from django.shortcuts import render

from performance_monitor.graphquery import *
from performance_monitor.models import Cse303ObeMarkSheetMarks


# Create your views here.
def showFacultyDataEntry(request): 
    return render(request, 'facultyDataEntry.html')

def showFaculty(request):
    return render(request, 'facultyDashboard.html')
     
def showLogIn(request):
    return render(request, 'logIn.html')

def showFacultyStudentReport(request):
    return render(request, 'facultyStudentReport.html')



# Student Dashboard
@allowedUsers(allowedRoles=['Student'])
def studentDashboard(request):
    chartName = []
    chartLabel = []
    chartDataSet = []
    
    chartN = 'Student-wise PLO'
    chartL = []
    chartD = []
    
    # student_id = '1930038'
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
    chartL = [] 
    chartD = [] 
    
    row = getDepartmentWisePLO('CSE')
    
    for i in row:
        chartL.append(i[1])
        chartD.append(i[2])
    
    chartName.append(chartN)
    chartLabel.append(chartL)
    chartDataSet.append(chartD)
    
    numberOfGraphs = len(chartName)
    
    # Stacked PLO Chart
    (plo, courses, table) = getCourseWisePLOChart(student_id)

    # getStudentProgressView
    (semester, semesterActual, semesterAttempted) = getStudentProgressView(student_id, 2019)
    

    #Heading 
    a = getNoOfPLOAchieved(student_id)
    b = getNoOfPLOAttempted(student_id)
    c = getMinLowestPLO(student_id)
    d = ploSuccessRate(student_id)
    
    return render(request, 'performance_monitor/(studentdashboard.html) will be here', {
        'userfullname': f'{request.user.first_name} {request.user.last_name}',
        'usertype': request.user.groups.all()[0].name,
        'numberOfGraphs': numberOfGraphs,
        'chartName': chartName,
        'chartLabel': chartLabel,
        'chartDataSet': chartDataSet,
        
        # Stacked PLO Chart
        'plo': plo,
        'courses': courses,
        'table': table,
        'ploWiseChartName': 'Course-wise PLO analysis',
        
        # getStudentProgressView
        'semester': semester,
        'semesterActual': semesterActual,
        'semesterAttempted': semesterAttempted,
        'studentProgressView': 'Student Progress View (Semester-wise)',
        
        # Heading
        'a': a,
        'b': b,
        'c': c,
        'd': d,
    })

#................................FacultyDashboard..................................................
#..................................................................................


    @allowedUsers(allowedRoles=['Faculty'])
    def facultyDashboard(request):
        faculty_id = request.user.username
    chartName = []
    chartLabel = []
    chartDataSet = []
    
    chartN = 'Department-wise PLO'
    chartL = [] 
    chartD = []
    
    row = getDepartmentWisePLO('CSE')
    
    for i in row:
        chartL.append(i[1])
        chartD.append(i[2])
    
    chartName.append(chartN)
    chartLabel.append(chartL)
    chartDataSet.append(chartD)
    
    numberOfGraphs = len(chartName)  

# getCourseProgressView
    (semester2, semesterActualCourse, semesterAttemptedCourse) = getCourseProgressView('CSE303', '2019')
    
    # print(semester2)
    # print(semesterActualCourse)
    # print(semesterAttemptedCourse)
    
    # Heading
    a = getNumOfCoursesHead(faculty_id)
    b = getNumOfSections(faculty_id)
    c = getAverageSuccessRate(faculty_id)
    d = getNumOfPLOsTaught(faculty_id)
    
    return render(request, 'performance_monitor/facultydashboard.html', {
        'userfullname': f'{request.user.first_name} {request.user.last_name}',
        'usertype': request.user.groups.all()[0].name,
        'numberOfGraphs': numberOfGraphs,
        'chartName': chartName,
        'chartLabel': chartLabel,
        'chartDataSet': chartDataSet,
        
        # getCourseProgressView
        'semester2': semester2,
        'semesterActualCourse': semesterActualCourse,
        'semesterAttemptedCourse': semesterAttemptedCourse,
        'courseProgressView': 'Course Progress View',
        
        # Heading
        'a': a,
        'b': b,
        'c': c,
        'd': d,
    })







