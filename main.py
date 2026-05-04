 #Project Title: Time2StudyMate!
 #Group Members: Aevery Kye F. Montenegro, Valther Gabriel D. Rosario, Dianne Pauline B. Solonia
 #Description: Time2StudyMate aims to help students users mange their time wisely by collecting inputs, validates of data, and conditional statements. To evaluate and guide users, and also to gain feedback about it's performance.

def get_name():
    fname = str(input("Enter first name: "))
    lname = str(input("Enter last name: "))
    if fname == "" or lname == "":
        print("Invalid input: Name cannot be empty!")
        return get_name()
        
    return fname, lname
    
def get_study_details():
        sub = str(input("Enter subject: "))
        time = int(input("Enter time (minutes): "))
        return sub, time
            
def evaluate_reminder(time):
    if time <= 0:
        print("Error, maybe a mispell?")
        
    elif time < 30:
        return "Short review!"
    elif time <= 60:
        return "Good study time!"
    elif time <= 61 or time <= 1000:
        return "Outstanding study session!"
    else:
        return "Invalid Input! Take a break!"
        
fname, lname = get_name()
print("Hello", fname, lname)
for i in range(2):
    print("\nReminder", i + 1)
    
    sub, time = get_study_details()
    result = evaluate_reminder(time)
    
    print (result)
print("Study", sub, "for", time, "minutes")

print("\nGoodluck on studying!")
print("\n----End of program----")
        

        
        
        
    

