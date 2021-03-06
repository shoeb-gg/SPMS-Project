from django.db import connection


def getStudentWisePLO(student_id):
    row = []
    for i in range(12):
        ploNum = f'PLO0{i + 1}'
        if i + 1 >= 10:
            ploNum = f'PLO{i + 1}'
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT AVG(TotalPlo.PLOpercentage) AS ActualPlo
                FROM (
                SELECT (PLO / TotalComark * 100) AS PLOpercentage
                FROM (
                        SELECT SUM(DISTINCT e.obtainedMarks) AS PLO, SUM(DISTINCT a.marks) AS TotalCoMark
                        FROM performance_monitor_enrollment_t en,
                            performance_monitor_evaluation_t e,
                            performance_monitor_assessment_t a,
                            performance_monitor_co_t c,
                            performance_monitor_plo_t p
                        WHERE en.student_id = '{}'
                            AND en.enrollmentID = e.enrollment_id
                            AND e.assessment_id = a.assessmentID
                            AND a.co_id = c.coID
                            AND c.plo_id = '{}'
                        GROUP BY en.section_id
                    ) ploPer
                ) TotalPlo;
            '''.format(student_id, ploNum))
            temp = cursor.fetchone()
            if temp is not None:
                row.append((temp[0], ploNum))
    return row

def getDepartmentWisePLO(departmentID):
    row = []
    for i in range(12):
        ploNum = f'PLO0{i + 1}'
        if i + 1 >= 10:
            ploNum = f'PLO{i + 1}'
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT AVG(TotalPlo.PLOpercentage) AS ActualPlo
                FROM (
                    SELECT (PLO / TotalComark * 100) AS PLOpercentage
                        FROM (
                            SELECT SUM(e.obtainedMarks) AS PLO, SUM(a.marks) AS TotalCoMark
                            FROM performance_monitor_enrollment_t en,
                                performance_monitor_evaluation_t e,
                                performance_monitor_assessment_t a,
                                performance_monitor_co_t c,
                                performance_monitor_plo_t p,
                                performance_monitor_student_t st
                            WHERE st.department_id = '{}'
                            AND st.studentID = en.student_id
                            AND en.enrollmentID = e.enrollment_id
                            AND e.assessment_id = a.assessmentID
                            AND a.co_id = c.coID
                            AND c.plo_id = '{}'
                            GROUP BY en.sectionID
                        ) ploPer
                    ) TotalPlo;
            '''.format(departmentID, ploNum))
            temp = cursor.fetchone()
            if temp is not None:
                row.append((deptID, ploNum, temp[0]))
    return row  

def getSchoolWisePLO(schoolID):
    row = []
    for i in range(12):
        ploNum = f'PLO0{i + 1}'
        if i + 1 >= 10:
            ploNum = f'PLO{i + 1}'
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT AVG(TotalPlo.PLOpercentage) AS ActualPlo
                FROM (
                    SELECT (PLO / TotalComark * 100) AS PLOpercentage
                        FROM (
                            SELECT SUM(e.obtainedMarks) AS PLO, SUM(a.marks) AS TotalCoMark
                            FROM performance_monitor_enrollment_t en,
                                performance_monitor_evaluation_t e,
                                performance_monitor_assessment_t a,
                                performance_monitor_co_t c,
                                performance_monitor_plo_t p,
                                performance_monitor_student_t st,
                                performance_monitor_school_t s,
                                performance_monitor_department_t d
                            WHERE s.schoolID= '{}'
                            AND s.schoolID = d.school_id
                            AND d.departmentID = st.department_id 
                            AND st.studentID = en.student_id
                            AND en.enrollmentID = e.enrollment-id
                            AND e.assessment_id = a.assessmentID
                            AND a.co_id = c.coID
                            AND c.plo_id = '{}'
                            GROUP BY en.sectionID
                        ) ploPer
                    ) TotalPlo;
            '''.format(departmentID, ploNum))
            temp = cursor.fetchone()
            if temp is not None:
                row.append((schoolID, ploNum, temp[0]))
    return row


def getUniversityWisePLO(UniversitytName):
    row = []
    for i in range(12):
        ploNum = f'PLO0{i + 1}'
        if i + 1 >= 10:
            ploNum = f'PLO{i + 1}'
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT AVG(TotalPlo.PLOpercentage) AS ActualPlo
                FROM (
                    SELECT (PLO / TotalComark * 100) AS PLOpercentage
                        FROM (
                            SELECT SUM(e.obtainedMarks) AS PLO, SUM(a.marks) AS TotalCoMark
                            FROM performance_monitor_enrollment_t en,
                                performance_monitor_evaluation_t e,
                                performance_monitor_assessment_t a,
                                performance_monitor_co_t c,
                                performance_monitor_University_t u,
                                performance_monitor_plo_t p,
                                performance_monitor_student_t st
                            WHERE st.university_name = '{}'
                            AND st.studentID = en.student_id
                            AND en.enrollmentID = e.enrollment_id
                            AND e.assessmentID = a.assessmentID
                            AND a.co_id = c.co_id
                            AND c.plo_id = '{}'
                            GROUP BY u.universityName
                        ) ploPer
                    ) TotalPlo;
            '''.format(UniversitytName, ploNum))
            temp = cursor.fetchone()
            if temp is not None:
                row.append((UniversitytName, ploNum, temp[0]))
    return row   

    
# Student

# Number of PLOs achieved by students
def getNoOfPLOAchieved(studentID):
    number = 0
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(TotalPlo.PLOpercentage) AS Acheive
            FROM (
                    SELECT   studentID,(PLO / TotalComark * 100) AS PLOpercentage
                    FROM performance_monitor_plo_t p,
                         performance_monitor_co_t c,
                        (
                            SELECT en.studentID,c.plo_id,SUM(DISTINCT e.obtainedMarks) AS PLO,SUM(DISTINCT a.marks)AS TotalCoMark
                            FROM performance_monitor_enrollment_t en,
                                performance_monitor_evaluation_t e,
                                performance_monitor_assessment_t a,
                                performance_monitor_co_t c,
                                performance_monitor_plo_t p,
                                performance_monitor_section_t s
                            WHERE en.studentID = '{}'
                            AND en.enrollmentID = e.enrollment_id
                                AND e.assessmentID = a.assessmentID
                                AND a.co_id = c.co_id
                                AND c.plo_id = p.ploID
                            GROUP BY  studentID,p.ploID
                        ) ploPer
                    WHERE p.ploID = ploPer.ploID

                GROUP BY studentID,ploID
                HAVING PLOpercentage >=40
                ) TotalPlo

            GROUP BY studentID
        '''.format(studentID))
        number = cursor.fetchone()[0]
        if number is None:
            number = 0
            
    return number
    
# PLO Attempted
def getNoOfPLOAttempted(studentID):
    number = 0
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(TotalPlo.PLOpercentage) AS Acheive
            FROM (
                    SELECT   studentID,(PLO / TotalComark * 100) AS PLOpercentage
                    FROM performance_monitor_plo_t p,
                        performance_monitor_co_t c,
                        (
                            SELECT en.studentID,c.plo_id,SUM(DISTINCT e.obtainedMarks) AS PLO,SUM(DISTINCT a.marks)AS TotalCoMark
                            FROM performance_monitor_enrollment_t en,
                                performance_monitor_evaluation_t e,
                                performance_monitor_assessment_t a,
                                performance_monitor_co_t c,
                                performance_monitor_plo_t p,
                                performance_monitor_section_t s
                            WHERE en.student_id = '{}'
                            AND en.enrollmentID = e.enrollment_id
                                AND e.assessmentID = a.assessmentID
                                AND a.co_id = c.coID
                                AND c.plo_id = p.ploID
                            GROUP BY  studentID,p.ploID
                        ) ploPer
                    WHERE p.ploID = ploPer.ploID

                GROUP BY studentID,ploID
            
                ) TotalPlo
        '''.format(studentID))
        number = cursor.fetchone()[0]
        if number is None:
            number = 0
            
    return number
    
def getProgramAchievement(prog):
    plo = ['PLO01', 'PLO02', 'PLO03', 'PLO04', 'PLO05', 'PLO06', 'PLO07', 'PLO08', 'PLO09', 'PLO10', 'PLO11', 'PLO12']
    semesterActual = []
    semesterAttempted = []
    row = []
    # for i in range(3):
    #     counterActual = 0
    #     counterAttempted = 0
    for j in plo:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT COUNT(Acheived.ActualPlo)
                FROM (
                        SELECT AVG(TotalPlo.PLOpercentage) AS ActualPlo
                        FROM (
                                SELECT student_id,(PLO / TotalComark * 100) AS PLOpercentage
                                FROM (
                                        SELECT  en.student_id,SUM(DISTINCT e.obtainedMarks) AS PLO, SUM(DISTINCT a.marks) AS TotalCoMark
                                        FROM performance_monitor_enrollment_t en,
                                                performance_monitor_evaluation_t e,
                                                performance_monitor_assessment_t a,
                                                performance_monitor_co_t c,
                                                performance_monitor_plo_t p,
                                                performance_monitor_program_t pr
                                        WHERE pr.programID = '{}'
                                            AND p.program_id = pr.programID
                                            AND en.enrollmentID = e.enrollment_id
                                            AND e.assessment_id = a.assessmentID
                                            AND a.co_id = c.coID
                                            AND c.plo_id = '{}'
                                        GROUP BY en.student_id
                                    ) ploPer
                            GROUP BY student_id
                            ) TotalPlo
                GROUP BY student_id
                    ) Acheived
                WHERE Acheived.ActualPlo >= 40;
            '''.format(prog, j))
            row = cursor.fetchall()
            if row is None:
                row = []
            semesterActual.append(row[0][0])



# PLO Success Rate
def ploSuccessRate(student_id): return np.round(getNoOfPLOAchieved(student-id) / getNoOfPLOAttempted(student_id) * 100, 1)

# Higher Management Dashboard

# Number of Students
def getNumOfStudents(department_id):
    number = 0
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(studentID) AS NoOfStudent
            FROM performance_monitor_student_t
            WHERE department_id = '{}'
        '''.format(department_id))
        number = cursor.fetchone()[0]
        if number is None:
            number = 0
            
    return number

# Number of Faculties
def getNumOfFaculties(department_id):
    number = 0
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT (DISTINCT facultyID ) AS NoFaculty
            FROM performance_monitor_faculty_t
            WHERE department_id = '{}'
        '''.format(department_id))
        number = cursor.fetchone()[0]
        if number is None:
            number = 0
            
    return number

# Number of courses in a department
def getNumOfCourses():
    number = 0
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(courseID) AS NoOfcourses
            FROM performance_monitor_course_t
        '''.format())
        number = cursor.fetchone()[0]
        if number is None:
            number = 0
            
    return number



# Faculty

# Num of Courses
def getNumOfCoursesHead(faculty_id):
    number = 0
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(DISTINCT course_id) AS NoOfCourses
            FROM performance_monitor_section_t
            WHERE faculty_id = '{}';
        '''.format(faculty_id))
        number = cursor.fetchone()[0]
        if number is None:
            number = 0
            
    return number
    

# Total Number of PLOs Taught by a faculty
def getNumOfPLOsTaught(faculty_id):
    number = 0
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(ploID) AS TotalNoPlotaught
            FROM (
                    SELECT course_id, coNo, ploID, COUNT(TotalPlo.PLOpercentage) AS Acheive
                    FROM (
                            SELECT co.course_id, co.coNo, p.ploID, (PLO / TotalComark * 100) AS PLOpercentage
                            FROM performance_monitor_plo_t p,
                                performance_monitor_co_t co,
                                (
                                    SELECT en.student_id,
                                            c.course_id,
                                            c.coNo,
                                            c.plo_id,
                                            SUM(DISTINCT e.obtainedMarks) AS PLO,
                                            SUM(DISTINCT a.marks)         AS TotalCoMark
                                    FROM performance_monitor_enrollment_t en,
                                            performance_monitor_section_t sec,
                                            performance_monitor_evaluation_t e,
                                            performance_monitor_assessment_t a,
                                            performance_monitor_co_t c,
                                            performance_monitor_plo_t p
                                    WHERE en.enrollmentID = e.enrollment_id
                                        AND en.section_id = sec.coID
                                        AND faculty_id = '{}'
                                        AND e.assessment_id = a.assessmentID
                                        AND a.co_id = c.coID
                                        AND c.plo_id = p.ploID
                                    GROUP BY student_id, c.course_id, c.coNo, p.ploID
                                ) ploPer
                            WHERE co.coNo = ploPer.coNo
                                AND p.ploID = ploPer.plo_id
                                AND co.course_id = ploPer.course_id
                            GROUP BY student_id, co.course_id, co.coNo, ploID

                        ) TotalPlo

                    GROUP BY course_id, coNo, ploID
                )
        '''.format(faculty_id))
        number = cursor.fetchone()[0]
        if number is None:
            number = 0
            
    return number

# Average PLO Success Rate
def getAverageSuccessRate(faculty_id):
    achieved = 0
    attempted = 0
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT AVG(Acheive) AS AVGPloacheivedbyastudent
            FROM (
                    SELECT course_id, coNo, ploID, COUNT(TotalPlo.PLOpercentage) AS Acheive
                    FROM (
                            SELECT co.course_id, co.coNo, p.ploID, (PLO / TotalComark * 100) AS PLOpercentage
                            FROM performance_monitor_plo_t p,
                                performance_monitor_co_t co,
                                (
                                    SELECT en.student_id,
                                            c.course_id,
                                            c.coNo,
                                            c.plo_id,
                                            SUM(DISTINCT e.obtainedMarks) AS PLO,
                                            SUM(DISTINCT a.marks)         AS TotalCoMark
                                    FROM performance_monitor_enrollment_t en,
                                            performance_monitor_section_t sec,
                                            performance_monitor_evaluation_t e,
                                            performance_monitor_assessment_t a,
                                            performance_monitor_co_t c,
                                            performance_monitor_plo_t p
                                    WHERE en.enrollmentID = e.enrollment_id
                                        AND en.section_id = sec.id
                                        AND faculty_id = '{}'
                                        AND e.assessment_id = a.assessmentID
                                        AND a.co_id = c.id
                                        AND c.plo_id = p.ploID
                                    GROUP BY student_id, c.course_id, c.coNo, p.ploID
                                ) ploPer
                            WHERE co.coNo = ploPer.coNo
                                AND p.ploID = ploPer.plo_id
                                AND co.course_id = ploPer.course_id
                            GROUP BY student_id, co.course_id, co.coNo, ploID
                            HAVING PLOpercentage >= 40
                        ) TotalPlo

                    GROUP BY course_id, coNo, ploID
                )
        '''.format(faculty_id))
        achieved = cursor.fetchone()[0]
        if achieved is None:
            achieved = 0
            
        cursor.execute('''
            SELECT AVG(Acheive) AS AVGPloacheivedbyastudent
            FROM (
                    SELECT course_id, coNo, ploID, COUNT(TotalPlo.PLOpercentage) AS Acheive
                    FROM (
                            SELECT co.course_id, co.coNo, p.ploID, (PLO / TotalComark * 100) AS PLOpercentage
                            FROM performance_monitor_plo_t p,
                                performance_monitor_co_t co,
                                (
                                    SELECT en.student_id,
                                            c.course_id,
                                            c.coNo,
                                            c.plo_id,
                                            SUM(DISTINCT e.obtainedMarks) AS PLO,
                                            SUM(DISTINCT a.marks)         AS TotalCoMark
                                    FROM performance_monitor_enrollment_t en,
                                            performance_monitor_section_t sec,
                                            performance_monitor_evaluation_t e,
                                            performance_monitor_assessment_t a,
                                            performance_monitor_co_t c,
                                            performance_monitor_plo_t p
                                    WHERE en.enrollmentID = e.enrollment_id
                                        AND en.section_id = sec.id
                                        AND faculty_id = '{}'
                                        AND e.assessment_id = a.assessmentID
                                        AND a.co_id = c.id
                                        AND c.plo_id = p.ploID
                                    GROUP BY student_id, c.course_id, c.coNo, p.ploID
                                ) ploPer
                            WHERE co.coNo = ploPer.coNo
                                AND p.ploID = ploPer.plo_id
                                AND co.course_id = ploPer.course_id
                            GROUP BY student_id, co.course_id, co.coNo, ploID
                        ) TotalPlo

                    GROUP BY course_id, coNo, ploID
                )
        '''.format(faculty_id))
        attempted = cursor.fetchone()[0]
        if attempted is None:
            attempted = 0
            
    return np.round(achieved / attempted * 100, 1)

# Num of Sections faculty Taking
def getNumOfSections(faculty_id):
    number = 0
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(id) AS NoOfSection
            FROM performance_monitor_section_t
            WHERE faculty_id = '{}';
        '''.format(faculty_id))
        number = cursor.fetchone()[0]
        if number is None:
            number = 0
            
    return number 
    
    

