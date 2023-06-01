def user_inputs():
    student_details = {}
    stud_no = int(input("Enter total students:"))
    for i in range(stud_no):
        print("\nEnter Details for student ",i+1,":")
        name = input("Enter name:")
        marks = int(input("Enter marks:"))
        student_details[name] = marks
    return student_details
#students that passes should register units
def register():
    units_list = []
    print("Select only 3 units\n1.Computing\n2.ICT\n3.Management Information\
          \n4.Networking\n5.Machine Learning")
    for i in range(3):
        print("Selection ",i+1,":")
        unit_number = int(input())
        if unit_number == 1:
            units_list.append("Computing")
        elif unit_number == 2:
            units_list.append("ICT")
        elif unit_number == 3:
            units_list.append("Management Information")
        elif unit_number == 4:
            units_list.append("Networking")
        elif unit_number == 5:
            units_list.append("Machine Learning")
        else:
            units_list.append("None")
    return units_list

#if a student fails
def options():
    print("Do you choose to:\n1.Repeat the Units?\n2.Quit the School?:")
    stud_option = int(input())
    if stud_option == 1:
        print("Successfully Registered for the new year class!,See you there!")
    elif stud_option == 2:
        print("GoodBye!, we will miss you so much!")
    else:
        print("Invalid! option,Kinldy try Again!")
        options()

#check the user marks
def check_results():
    dictionary = user_inputs()
    for keys in dictionary.keys():
        if dictionary[keys] >= 250:
            print("\nCongratulations! ", keys," Kindly choose the units to study:")
            result = register()
            print("Successful registration of ", result," Units.")
        else:
            print("\nDear! ", keys,":")
            options()

try:
    check_results()
except ValueError:
    print("Error!,value error occured,try again")
except:
    print("An error occured!")

