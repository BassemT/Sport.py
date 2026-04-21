print("Welcome to the Hospital Management System")
print("Hospital contact number: 56565656")
print("Contact Ambulance: 56565656")

while True:
    welcome = input("What would you like to do? (1) Book an appointment (2) Visit a doctor or the patient (3) Exit: ")

    
    if welcome == "1":
            
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        user_id = input("Please enter your ID: ")
        appoint = input("Please enter your prefferd time: ")
        if age < 18:
            print("Sorry, you must be at least 18 years old to book an appointment. Please get your parent or guardian.")
        else:
            print("Your appointment has been successfully booked. Your appointment time will be at",appoint, "PM. It would be 5 BHD for the consultation fee. You can pay at the hospital or online.")
            print("Name: ", name)
            print("Age: ", age)
            print("ID: ", user_id)
        
    elif welcome == "2":
        
            visit = input("Would you like to visit a doctor or a patient: ").lower()
            if visit == "doctor":
                which = input("Which doctor would you like to visit? (1) Neurologist (2) Cardiologist (3) Dermatologist (4) Psychiatrist: ").lower()
                if which == "1":
                    name2 = input("Please enter your name: ")
                    age2 = input("please enter your age: ")
                    user_id2 = input("Please enter your ID: ")
                    available_time = input("Please enter the time you would like to visit the doctor: ")
                    print("🔄 Checking Neurologist availibility in our hospital.....")
                    print("We have 5 docters availavle at", available_time, "today. We have Dr. Smith available from 10 AM to 5 PM.")
                    print("For more information, please contact Dr. Smith at 12345678.")

                elif which == "2":
                    name3 = input("Please enter your name: ")
                    age3 = input("Please enter your age: ")
                    user_id3 = input("Please enter your ID: ")
                    available_time2 = input("Please enter the time you would like to visit the doctor: ")
                    print("🔄 Checking Cardiologist availibility in our hospital.....")
                    print("We have 3 docters availavle at", available_time, "today. We have Dr. Mohammed available from 12 PM to 9 PM.")
                    print("For more information, please contact Dr. Mohammed at 87654321.")

                elif which == "3":
                    name4 = input("Please enter your name: ")
                    age4 = input("Please enter your age: ")
                    user_id4 = input("Please enter your ID: ")
                    available_time4 = input("Please enter the time you would like to visit the doctor: ")
                    print("🔄 Checking Dermatologist availibility in our hospital.....")
                    print("We have 6 docters availavle at", available_time, "today. We have Dr. Sarah available from 10 AM to 5 PM.")
                    print("For more information, please contact Dr. Sarah at 00000000.")

                elif which == "4":
                    name5 = input("Please enter your name: ")
                    age5 = input("Please enter your age: ")
                    user_id5 = input("Please enter your ID: ")
                    available_time5 = input("Please enter the time you would like to visit the doctor: ")
                    print("🔄 Checking Psychiatrist availibility in our hospital.....")
                    print("We have 5 docters availavle at", available_time, "today. We have Dr. Jhon available from 10 AM to 5 PM.")
                    print("For more information, please contact Dr. Jhon at 11111111.")

                else: 
                    print("Invalid input. Please try again")

            elif visit == "patient":
                name6 = input("Please enter your name: ")
                age6 = input("Please enter your age: ")
                user_id6 = input("Please enter your ID: ")
                patient_name = input("Please enter the name of the patient you would like to visit: ")
                time6 = input("Please enter your preferred appointment time: ")
                print("Your time with", patient_name,"has been successfully booked. Your appointment time will be at ", time6, ". For more information, please contact the hospital at 56565656.")
            else:
                print("Invalid input. Please try again:/")
    
    elif welcome == "3":
        print("Thank you for visiting our web site. We hope to see you again soon! Have a great day!")
        break
    else:
        print("Invalid input. Please try again.")
        break
