import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# student validity checker
def get_add_student_details_check(student_id,student_name,student_age,student_standard,student_gender,student_email,student_contact):
    try:
        int_student_id = int(student_id)
    except:
        return False

    check_name = student_name.isalpha()
    if(check_name == False):
        return False
    
    try:
        int_student_age = int(student_age)
    except:
        return False

    try:
        int_student_standard = int(student_standard)
    except:
        return False
    
    if(student_gender!="M" and student_gender!="F"):
        return False
    
    if(re.fullmatch(regex, student_email)==False):
        return False
    
    if(student_contact.isdecimal()==False and len(student_contact)!=10):
        return False

    return True


# teacher validity checker
def get_add_teacher_details_check(teacher_id,teacher_name,teacher_age,teacher_gender,teacher_email,teacher_contact):
    try:
        int_teacher_id = int(teacher_id)
    except:
        return False    

    check_name = teacher_name.isalpha()
    if(check_name == False):
        return False

    try:
        int_teacher_age = int(teacher_age)
    except:
        return False

    if(teacher_gender!="M" and teacher_gender!="F"):
        return False

    if(re.fullmatch(regex, teacher_email)==False):
        return False

    if(teacher_contact.isdecimal()==False and len(teacher_contact)!=10):
        return False
    
    return True

#Course validity checker
def get_add_course_details_check(course_id,course_name):
    try:
        int_course_id = int(course_id)
    except:
        return False
    
    check_name = course_name.isalpha()
    if(check_name == False):
        return False
    
    return True