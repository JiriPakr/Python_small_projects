import os

# Clear terminal
def clearConsole(): # Čistění konzole
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)


# BMI calculator
clearConsole()
weight = float(input("[INPUT] weight(kg): "))
height = float(input("[INPUT] height(m): "))
bmi = weight / height**2                                                # weight divided by height squared
if bmi < 18.5:
    print("[INFO] Your category is: UNDERWEIGHT\n[INFO] BMI value: ", bmi, "\n")
elif bmi >= 18.5 and bmi < 25:
    print("[INFO] Your category is: NORMAL\n[INFO] BMI value: ", bmi, "\n")
elif bmi >= 25 and bmi < 30:
    print("[INFO] Your category is: OVERWEIGHT\n[INFO] BMI value: ", bmi, "\n")
elif bmi >= 30:
    print("[INFO] Your category is: OBESITY\n[INFO] BMI value: ", bmi, "\n")