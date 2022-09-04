class Student:
    """Represents a student enrolled in a course
    attibutes First name, Last name, Postcode (protected), phone number (protected)"""
    #protected class attribute
    _course_name = "Python programming"   

student1 = Student()

#public attibutes
student1.first_name = "Aaron"
student1.surname = "Willis"
#protected attributes
student1._postcode = "AA1 1AA"
student1._phone_no = "00000001"

print(student1._course_name)
print(student1.first_name)
print(student1._postcode)