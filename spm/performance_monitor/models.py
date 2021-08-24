from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Cse303ObeMarkSheetAnalysis(models.Model):
    studentid = models.CharField(db_column='studentID', primary_key=True, max_length=7)  # Field name made lowercase.
    courseid = models.CharField(db_column='courseID', max_length=9, blank=True, null=True)  # Field name made lowercase.
    sectionid = models.CharField(db_column='sectionID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    semester = models.CharField(max_length=8, blank=True, null=True)
    totalobtainedmarks_100_field = models.CharField(db_column='totalObtainedMarks(100)', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    passorfail = models.CharField(db_column='passOrFail', max_length=3, blank=True, null=True)  # Field name made lowercase.
    co1percentage = models.CharField(db_column='co1Percentage', max_length=5, blank=True, null=True)  # Field name made lowercase.
    co2percentage = models.CharField(db_column='co2Percentage', max_length=7, blank=True, null=True)  # Field name made lowercase.
    co3percentage = models.CharField(db_column='co3Percentage', max_length=3, blank=True, null=True)  # Field name made lowercase.
    co4percentage = models.CharField(db_column='co4Percentage', max_length=7, blank=True, null=True)  # Field name made lowercase.
    co1achievement = models.CharField(max_length=5, blank=True, null=True)
    co2achievement = models.CharField(max_length=3, blank=True, null=True)
    co3achievement = models.CharField(max_length=3, blank=True, null=True)
    co4achievement = models.CharField(max_length=3, blank=True, null=True)
    plo2achievement = models.CharField(max_length=3, blank=True, null=True)
    plo3achievement = models.CharField(max_length=3, blank=True, null=True)
    plo4achievement = models.CharField(max_length=3, blank=True, null=True)
    plo6achievement = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        
        db_table = 'cse303_obe_mark_sheet__analysis_'


class Cse303ObeMarkSheetMarks(models.Model):
    studentid = models.CharField(db_column='studentID', primary_key=True, max_length=7)  # Field name made lowercase.
    courseid = models.CharField(db_column='courseID', max_length=9, blank=True, null=True)  # Field name made lowercase.
    sectionid = models.CharField(db_column='sectionID', max_length=1, blank=True, null=True)  # Field name made lowercase.
    semester = models.CharField(max_length=8, blank=True, null=True)
    co1_q1mid_25_field = models.CharField(db_column='co1_q1Mid(25)', max_length=7, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co1_q2mid_25_field = models.CharField(db_column='co1_q2Mid(25)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co1_q3mid_30_field = models.CharField(db_column='co1_q3Mid(30)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co2_q4mid_20_field = models.CharField(db_column='co2_q4Mid(20)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co1_q5mid_30_field = models.CharField(db_column='co1_q5Mid(30)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co1_q6mid_20_field = models.CharField(db_column='co1_q6Mid(20)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    midtermtotal_150_field = models.CharField(db_column='midtermTotal(150)', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    midtermtotalconverted_30_field = models.CharField(db_column='midtermTotalConverted(30)', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co1_q1final_20_field = models.CharField(db_column='co1_q1Final(20)', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co1_q2final_15_field = models.CharField(db_column='co1_q2Final(15)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co2_q3final_15_field = models.CharField(db_column='co2_q3Final(15)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co3_q4final_50_field = models.CharField(db_column='co3_q4Final(50)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    finaltotal_100_field = models.CharField(db_column='finalTotal(100)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    finaltotalconverted_40_field = models.CharField(db_column='finalTotalConverted(40)', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    projectworkmarks_30_field = models.CharField(db_column='projectWorkMarks(30)', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    totalobtainedmarks_100_field = models.CharField(db_column='totalObtainedMarks(100)', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co1totalobtained_165_field = models.CharField(db_column='co1TotalObtained(165)', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co2totalobtained_35_field = models.CharField(db_column='co2TotalObtained(35)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co3totalobtained_50_field = models.CharField(db_column='co3TotalObtained(50)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co4totalobtained_30_field = models.CharField(db_column='co4TotalObtained(30)', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'cse303_obe_mark_sheet__marks_'


class Cse303ObeMarkSheetVerdict(models.Model):
    totalstudents = models.CharField(db_column='totalStudents', max_length=2, blank=True, null=True)  # Field name made lowercase.
    outcome = models.CharField(primary_key=True, max_length=3)
    outcomeachievedby = models.CharField(db_column='outcomeAchievedBy', max_length=5, blank=True, null=True)  # Field name made lowercase.
    outcomeachievedby_field = models.CharField(db_column='outcomeAchievedBy(%)', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    outcomefailedtoachieve = models.CharField(db_column='outcomeFailedToAchieve', max_length=5, blank=True, null=True)  # Field name made lowercase.
    outcomefailedtoachieve_field = models.CharField(db_column='outcomeFailedToAchieve(%)', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

class Meta:
        managed = False
        db_table = 'cse303_obe_mark_sheet__verdict_'

class University_T(models.Model):
    universityName = models.CharField(max_length=50, primary_key=True)
    school = models.ForeignKey(School_T, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.universityName
        

class School_T(models.Model):
    schoolID = models.CharField(max_length=5, primary_key=True)
    schoolName = models.CharField(max_length=50)

    def __str__(self):
        return self.schoolID

class Department_T(models.Model):
    departmentID = models.CharField(max_length=5, primary_key=True)
    departmentName = models.CharField(max_length=50)
    school = models.ForeignKey(School_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.departmentID


class Program_T(models.Model):
    programID = models.AutoField(primary_key=True)
    programName = models.CharField(max_length=70)
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE, default='N/A')

    def __str__(self):
        return self.programName


class Student_T(models.Model):
    studentID = models.CharField(max_length=7, primary_key=True)
    studentName = models.CharField(max_length=50, null=True)
    dateOfBirth = models.DateField(null=True)
    gender = models.CharField(max_length=6, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=50, null=True)
    enrollmentDate = models.DateField(null=True)
    university = models.ForeignKey(University_T, on_delete=models.CASCADE)
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE, default='N/A')
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.studentID   

class Faculty_T(Employee_T):
    facultyID = models.IntegerField(primary_key=True)
    facultyName = models.CharField(max_length=50, null=True)
    dateOfBirth = models.DateField(null=True)
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=6, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
   
    def __str__(self):
        return self.facultyName


class Course_T(models.Model):
    courseID = models.CharField(max_length=7, primary_key=True)
    courseName = models.CharField(max_length=50, null=True)
    numOfCredits = models.DecimalField(max_digits=2, decimal_places=1)
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE)
    courseType = models.CharField(max_length=15)

    def __str__(self):
        return self.courseID


class PrereqCourse_T(models.Model):
    course = models.ForeignKey(Course_T, on_delete=models.CASCADE, related_name='Course')
    preReqCourse = models.ForeignKey(Course_T, on_delete=models.CASCADE, related_name='PreRequisite')


class PLO_T(models.Model):
    ploID = models.AutoField(primary_key=True)
    ploNum = models.CharField(max_length=5)
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE)
    details = models.CharField(max_length=50)

    def __str__(self):
        return self.ploNum


class Section_T(models.Model):
    sectionID = models.AutoField(primary_key=True)
    sectionNum = models.IntegerField()
    course = models.ForeignKey(Course_T, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty_T, on_delete=models.CASCADE)
    semester = models.CharField(max_length=15)


    def __str__(self):
        return str.sectionNum


class Enrollment_T(models.Model):
    enrollmentID = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student_T, on_delete=models.CASCADE)
    section = models.ForeignKey(Section_T, on_delete=models.CASCADE)
    semester = models.CharField(max_length=15)
    year = models.IntegerField(default=2020,null=True)

    def __str__(self):
        return str.registrationID



class CO_T(models.Model):
    coID = models.AutoField(primary_key=True)
    coNum = models.CharField(max_length=4)
    plo = models.ForeignKey(PLO_T, on_delete=models.CASCADE, default='N/A')
    course = models.ForeignKey(Course_T, on_delete=models.CASCADE, default='N/A')
    thresold = models.FloatField(default=40)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.coNum



class Assessment_T(models.Model):
    assessmentID = models.AutoField(primary_key=True)
    assessmentName = models.CharField(max_length=30)
    questionNum = models.IntegerField()
    totalMarks = models.FloatField()
    co = models.ForeignKey(CO_T, on_delete=models.CASCADE)
    section = models.ForeignKey(Section_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.assessmentName + " "+str(self.questionNum)



class Evaluation_T(models.Model):
    evaluationID = models.AutoField(primary_key=True)
    obtainedMarks = models.FloatField()
    assessment = models.ForeignKey(Assessment_T, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Registration_T, on_delete=models.CASCADE)

    def __str__(self):
        return str.evaluationID        
          

