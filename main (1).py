 #Project Title: Time2StudyMate!
 #Group Members: Aevery Kye F. Montenegro, Valther Gabriel D. Rosario, Dianne Pauline B. Solonia
 #Description: Time2StudyMate aims to help students users mange their time wisely by collecting inputs, validates of data, and conditional statements. To evaluate and guide users, and also to gain feedback about it's performance.

def get_name():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    if fname == "" or lname == "":
        print("Invalid input: Name cannot be empty!")
        return get_name()
    return fname, lname
    
def get_study_deta():
        sub = input("Enter subject: ")
        remainder = int(input("Enter time (minutes): "))
        return sub, remainder
            
def evaluate_remainder(reminder):
    if remainder < 30:
        return "Short review!"
    elif remainder <= 60:
        return "Good study time!"
    else:
        return "Outstanding study session!"
        
fname, lname = get_name()

print("Hello", fname, lname)

sub, time = get_study_deta()
result = evaluate_remainder(reminder)

print (result)
print("Study", subject, "for", reminder, "minutes")
        

        
        
        
    

