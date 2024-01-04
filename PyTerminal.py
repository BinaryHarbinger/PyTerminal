#PyTerminal Version 0.2 (Beta Version)

#This project developed by allah.

#Purpose is developing Terminal like cmd or Linux Terminal.

from os import system, listdir , remove , chdir
from time import sleep

#We'll need that function on detecting key input for y/n question or continue functions.
from keyboard import wait as WAITFORKEY

#This class takes inputs for important points.
class StopMarks () :
    # This function wait for Space key input
    @staticmethod
    def WAITFORSPACE (ERRORMESSAGE = None) : 
        if int (ERRORMESSAGE) == 1 : #If ERRORMESSAGE variable gets a value there is some messages for explain.
            print ('Press Space to Continue...')
        WAITFORKEY("space")
    @staticmethod
    def YorN(MESSAGE):
        while True:
            user_input = input(f"{MESSAGE} (Yes/No): ").strip().lower()
            if user_input in ['yes', 'y']:
                return True
            elif user_input in ['no', 'n']:
                return False
            else:
                print("Please enter Yes or No.")

##This class includes functions for Terminal .
#class Function () :

#This class is file system .
class filesystem () :
    @staticmethod
    def list(): #Writes a list of files in directory.
        files = listdir()
        print("Files in directory:", files)

    @staticmethod
    def create_file(filename):
        try:
            with open(filename, 'w') as file:
                file.write("")  # Creates a new file.
            print(f"File '{filename}' created successfully.")
        except Exception as e:
            print(f"Error creating '{filename}': {e}")

    @staticmethod
    #Deletes file.
    def delete_file(filename):
        try:
            remove(filename)
            print(f"File '{filename}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting '{filename}': {e}")
    @staticmethod
    def cd(path):
        try:
            chdir(path)
            print(f"Changed directory to '{path}'")
        except Exception as e:
            print(f"Error changing directory to '{path}': {e}")
    @staticmethod
    def show_content(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(f"Content of '{filename}':\n{content}")
        except Exception as e:
            print(f"Error displaying content of '{filename}': {e}")
    @staticmethod
    def create_edit(filename):
        try:
            content = input("Enter content for the file:\n")
            with open(filename, 'w') as file:
                file.write(content)
            print(f"File '{filename}' created or edited successfully.")
        except Exception as e:
            print(f"Error creating or editing '{filename}': {e}")

class PyTerminal () :
    #This function shows us current version of Terminal.
    @staticmethod
    def ver () : 
        print('PyTerminal Version 0.2 (Beta)')

    # To display the help menu:
    @staticmethod
    def help():
        print("""\
        Terminal Help Menu:

        - close/exit: Exits the Terminal.
        - system-terminal/s-t: Switches to the normal system terminal.
        - ver/version: Shows the version of the Terminal.
        - cls: Clears the console.

        File Operations:
        - list: Lists files in the current directory.
        - create_file [file_name]: Creates a new file.
        - delete_file [file_name]: Deletes the specified file.
        - cd [directory]: Changes the directory to the specified one.
        - show_content [file_name]: Shows the content of the specified file.
        - create_edit [file_name]: Creates or edits the specified file.

        Color and Theme Options:
        - color (color_code): Changes the text color. [Example: color (0A)]
        """)
        StopMarks.WAITFORSPACE()


    @staticmethod
    #Clears the all text on terminal history.
    def cls () :
        system('cls')

    #Set colors of text and background.
    @staticmethod
    def color (SELECTCOLOR) :
        COLORCOMMAND = 'color' + str(SELECTCOLOR)
        system (COLORCOMMAND)

#Main part of code.

#There is 3 mode for now :
#        
#Normal Terminal Mode (0)
#
#System Terminal Mode (1)
#
#File Manager Mode (2)
MODE = 0

PyTerminal.ver () #Shows the Version of Terminal.
#An infinite loop for terminal.
while True :
    try :
        #User input part and some if things.
        COMMAND0 = input(">>>")
        if MODE == 0 :
            if COMMAND0 == 'close' or COMMAND0 == 'exit' :
                exit ()
            elif COMMAND0 :
                pass
            elif COMMAND0 == 'f-m' or COMMAND0 == 'file-manager' :
                MODE = 2
            elif COMMAND0 == 'help' or COMMAND0 == '?' :
                help()
            elif COMMAND0 == 'system-terminal' or COMMAND0 == 's-t' :
                #If user want's to use normal system terminal this mode allows user to use system terminal on PyTerminal.
                PyTerminal.cls ()
                print ('Current System Terminal is running on PyTerminal.')
                MODE = 1
            elif COMMAND0 == 'ver' or COMMAND0 == 'version' :
                PyTerminal.ver ()
            elif COMMAND0 == 'cls' :
                PyTerminal.cls ()
            elif COMMAND0 == '' :
                pass
            else :
                try :
                    COMMAND = eval('PyTerminal.' + COMMAND0)
                    COMMAND
                except :
                    COMMANDFORCONSOLE = eval('PyTerminal.' + COMMAND0 + '()')
                    COMMANDFORCONSOLE
        elif MODE == 1 :
            #System terminal mode.
            if COMMAND0 == 'exit' :
                MODE = False
            else :
                COMMANDFORCONSOLE = eval("system('" + COMMAND0 + "')")
                COMMAND0
        elif MODE == 2 :
            try :
                COMMANDFORCONSOLE = eval('filesystem.' + COMMAND0)
                COMMANDFORCONSOLE
            except :
                COMMANDFORCONSOLE = eval('filesystem.' + COMMAND0 + '()')
                COMMANDFORCONSOLE
    except Exception as EXCEPTION :
        #If exception happens this part explains what is the problem.
        print ('ERROR: '+ EXCEPTION)