medical_cause=input("Do you have a medical cause? Y or N: ")
attendance=int(input("ENTER YOUR ATTENDANCE: "))
if medical_cause=="Y":
    print("You are allowed to write the exam")
else:
    if attendance>75:
        print("You are allowed to write the exam")
    else:
        print("You are not allowed to write the exam")