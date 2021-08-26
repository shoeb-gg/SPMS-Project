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
                            AND e.assessment_id = a.assessmentNo
                            AND a.co_id = c.id
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
                            AND en.enrollmentID = e.enrollmentID
                            AND e.assessmentID = a.assessmentNo
                            AND a.coID = c.coID
                            AND c.ploID = '{}'
                            GROUP BY en.sectionID
                        ) ploPer
                    ) TotalPlo;
            '''.format(departmentID, ploNum))
            temp = cursor.fetchone()
            if temp is not None:
                row.append((deptID, ploNum, temp[0]))
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
                                performance_monitor_plo_t p,
                                performance_monitor_student_t st
                            WHERE st.university_name = '{}'
                            AND st.studentID = en.studentID
                            AND en.enrollmentID = e.enrollmentID
                            AND e.assessmentID = a.assessmentNo
                            AND a.coID = c.coID
                            AND c.ploID = '{}'
                            GROUP BY en.sectionID
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
                            AND en.enrollmentID = e.enrollmentID
                                AND e.assessmentID = a.assessmentNo
                                AND a.coID = c.coID
                                AND c.ploID = p.ploNo
                            GROUP BY  studentID,p.ploNo
                        ) ploPer
                    WHERE p.ploNo = ploPer.ploID

                GROUP BY studentID,ploNo
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
                            AND en.enrollmentID = e.enrollmentID
                                AND e.assessmentID = a.assessmentNo
                                AND a.coID = c.id
                                AND c.ploID = p.ploNo
                            GROUP BY  studentID,p.ploNo
                        ) ploPer
                    WHERE p.ploNo = ploPer.ploID

                GROUP BY studentID,ploNo
            
                ) TotalPlo
        '''.format(studentID))
        number = cursor.fetchone()[0]
        if number is None:
            number = 0
            
    return number
    


# PLO Success Rate
def ploSuccessRate(studentID):
    return np.round(getNoOfPLOAchieved(studentID) / getNoOfPLOAttempted(studentID) * 100, 1)


