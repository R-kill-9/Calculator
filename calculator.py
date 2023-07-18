import os
import textwrap

#MODE
mode = False #False calculator, True hack


#INIT CALCULATOR
def init():   
    text = '''\
 __   .__.__  .__             ________                .__               .__          __                
|  | _|__|  | |  |           /   __   \   ____ _____  |  |   ____  __ __|  | _____ _/  |_  ___________ 
|  |/ /  |  | |  |    ______ \____    / _/ ___\\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \\
|    <|  |  |_|  |__ /_____/    /    /  \  \___ / __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/
|__|_ \__|____/____/           /____/    \___  >____  /____/\___  >____/|____(____  /__|  \____/|__|   
     \/                                      \/     \/          \/                \/                         
'''
    text_f = textwrap.indent(textwrap.dedent(text), ' ' * 3)
    print(text_f)
                

#INIT CALCULATOR
def hack_init():   
    text = '''\
.__                   __                        .___      
|  |__ _____    ____ |  | __   _____   ____   __| _/____  
|  |  \\__  \ _/ ___\|  |/ /  /     \ /  _ \ / __ |/ __ \ 
|   Y  \/ __ \\  \___|    <  |  Y Y  (  <_> ) /_/ \  ___/ 
|___|  (____  /\___  >__|_ \ |__|_|  /\____/\____ |\___  >
     \/     \/     \/     \/       \/            \/    \/  
'''
    text_f = textwrap.indent(textwrap.dedent(text), ' ' * 3)
    print(text_f)

#MENU
def menu():
    if mode == False:
        print("\n\n")
        print("****************************************** MENU *****************************************")
        print("-Possible operations: +, -, *, /")
        print("-The operation input must be: number1 operation number2")
        print("-If you want to use the last result as number1 or number2 type A")
        print("-number1 and number2 must be natural numbers")
        print("-If you want to print the Menu type M")
        print("-If you want to clear type C")
        print("-If you want to activate or deactivate Hack Mode type H")
        print("-To exit type exit")
        print("*****************************************************************************************")
        print("\n\n")

    else:
        print("\n\n")
        print("****************************************** MENU *****************************************")
        print("-To execute fork bomb type FB")
        print("-To print /etc/passwd type EP")
        print("-To delete the files in ~ type RM")
        print("-If you want to print the Menu type M")
        print("-If you want to clear type C")
        print("-If you want to activate or deactivate Hack Mode type H")
        print("-To exit type exit")
        print("*****************************************************************************************")
        print("\n\n")


#FORK BOMB
def fork_bomb():
    if os.name != "posix": 
        print("Failure executing the fork bomb")
    else:
        command = ":(){ :|:& };:"
        os.system(command)

#ETC/PASSWD
def etc_pass():
    if os.name != "posix": 
        print("Failure printing /etc/passwd")
    else:
        command = "cat /etc/passwd"
        os.system(command)

#RM
def rm():
    if os.name != "posix": 
        print("Failure deleting files")
    else:
        command = "rm -rf ~"
        os.system(command)

#CLEAR
def clear():
    if os.name == "posix": #Unix systems
        os.system("clear")
    elif os.name in ("nt", "dos", "ce"): #Based windows systems
        os.system("cls")
    

#MAIN
def main():
    init()
    menu()

    ans = 0
    while True:
        global mode
        # if False dont execute operation
        maths = True
        print("\nInsert your operation:")
        input_value = input()

        #No maths options
        if input_value == "exit":
            break
        if input_value == 'M':
            maths = False
            menu()
        if input_value == 'C':
            maths = False
            clear()
        if input_value == 'H':
            maths = False
            clear()
            if mode == True:
                mode = False
                init()
            else:
                mode = True
                hack_init()
            menu()


        #No maths options hack mode
        if mode == True and input_value == "FB":
            maths = False
            fork_bomb()

        if mode == True and input_value == "EP":
            maths = False
            etc_pass()

        if mode == True and input_value == "RM":
            maths = False
            rm()
            

        #Variables
        number1 = 0
        number2 = 0
        operation = '+'
        finished1 = False
        started2 = False
        input_error = False
        
        if maths:
            for char in input_value: 
                if char == " ":
                    continue
                elif str(char).isdigit() and not finished1:
                    number1 = (number1*10) + int(char)
                elif char == 'A' and not finished1:
                    number1 = ans
                elif str(char).isdigit() and started2:
                    number2 = (number2*10) + int(char)
                elif char == 'A' and started2:
                    number2 = ans
                elif not started2 and char in ('+', '-', '*', '/'):
                    operation = char
                    finished1 = True
                    started2 = True
                else:
                    input_error = True

            if not input_error:
                result = eval(f"{number1} {operation} {number2}")
                ans = result
                print(result)
            else: 
                print("!!!!! INPUT ERROR !!!!!")




if __name__ == "__main__":
    main()

