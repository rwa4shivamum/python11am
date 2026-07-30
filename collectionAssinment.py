# student1 = {
#     'name':'sd',
#     'age':82
# }

# #list of dictionary
# lst = [{
#     'name':'sd',
#     'age':82
# },
# {
#     'name':'sd',
#     'age':82
# }]

listOfStudent = []

while(True):
    print("Wlcome to the Student Data Organizer!")
    print('''Select an Option:
    1.Add Student
    2.Display All Students
    3.Update Student Information
    4.Delete Student
    5.Display Subject Offered 
    6.Exit''')
    selectOption = int(input("Enter A number:"))
    if(selectOption == 1):
        print("Enter a Student Details: ")
        studentId = int(input("Enter a Studnet Id: "))
        name =input("Enter a Name of Studnet: ")
        age  = int(input("Enter age of studnet: "))
        Grade = input("Entera  grade of students: ")
        dob = input("Enter a Date of Birth(YYYY-MM-DD): ")
        subject = input("Enter the subject by using comma: ").split(",")

        studentInfoTUple = (studentId,dob)
        uniqueSubjectSet = set(subject)
        dictionaryOfStudent = {
            'studentOfTuple':studentInfoTUple,
            'id':studentId,
            'name':name,
            'age':age,
            'Grade':Grade,
            'subject':uniqueSubjectSet
        }

        listOfStudent.append(dictionaryOfStudent)
    elif selectOption == 2:
        print('----Display All Student---')
        for i in range(0,len(listOfStudent)):
            print(f"StudentID:{listOfStudent[i]['studentOfTuple'][0]} | Name:{listOfStudent[i]['name']} | Age:{listOfStudent[i]['age'] | Grade:{listOfStudent[i]['Grade']}} | subject: {listOfStudent[i]['subject']}")
    elif selectOption == 3:
        studentIdToUpdate = int(input("Entera a Student ID: "))
        isMatch = False
        for i in range(0,len(listOfStudent)):
            if(listOfStudent[i]['id'] == studentIdToUpdate):
                isMatch = True
                enterSubjectToUpdate = input("Enter a Subject To Update: ")
                enterAnewSubject = input("Enter a New Subject")
                listOfSubject = list(listOfSubject[i]['subject'])
                indexOfSubject = listOfSubject.index(enterSubjectToUpdate)
                listOfSubject[indexOfSubject] = enterAnewSubject
                listOfStudent[i]['subject'] = set(listOfSubject)
                break
            else:
                print("Student ID not Found")
    elif selectOption == 4:
        studentIdToDelete = int(input("Enter a Student Id: "))
        isMatch = False
        for i in range(0,len(listOfStudent)):
            if(listOfStudent[i]['id'] == studentIdToDelete):
                isMatch = True
                del listOfStudent[i]
                break
            else:
                print("Student Not Found")
    elif selectOption == 6:
        break
