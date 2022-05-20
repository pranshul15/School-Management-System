import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

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


