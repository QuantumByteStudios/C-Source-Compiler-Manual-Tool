#Author & Developer
#	Quantum Dyte Studios
#		Visit: http://quantumbyteofficial.tech/
import os

os.system("title C Source Compiler Tool -- Quantum Byte Studios")

print('''


  /$$$$$$         /$$$$$$                                                           /$$$$$$                                    /$$ /$$                    
 /$$__  $$       /$$__  $$                                                         /$$__  $$                                  |__/| $$                    
| $$  \__/      | $$  \__/  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$$  /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$| $$  /$$$$$$   /$$$$$$ 
| $$            |  $$$$$$  /$$__  $$| $$  | $$ /$$__  $$ /$$_____/ /$$__  $$      | $$       /$$__  $$| $$_  $$_  $$ /$$__  $$| $$| $$ /$$__  $$ /$$__  $$
| $$             \____  $$| $$  \ $$| $$  | $$| $$  \__/| $$      | $$$$$$$$      | $$      | $$  \ $$| $$ \ $$ \ $$| $$  \ $$| $$| $$| $$$$$$$$| $$  \__/
| $$    $$       /$$  \ $$| $$  | $$| $$  | $$| $$      | $$      | $$_____/      | $$    $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$| $$| $$_____/| $$      
|  $$$$$$/      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$      |  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$$$$$$/| $$| $$|  $$$$$$$| $$      
 \______/        \______/  \______/  \______/ |__/       \_______/ \_______/       \______/  \______/ |__/ |__/ |__/| $$____/ |__/|__/ \_______/|__/      
                                                                                                                    | $$                                  
                                                                                                                    | $$                                  
                                                                                                                    |__/                                  
                 

Developed by: Quatum Byte Studios

	+ http://quantumbyteofficial.tech/

====================================================================
''')

sourceFileLocation = input("Enter the location of your C Source File with extension: ")
sourceFileName = input("Enter the name of your program: ")

command = (f'gcc "{sourceFileLocation}" -o "{sourceFileName}.exe"')
print(f"\n\nApplied Command: {command}")
os.system(command)

wait =  input("\n\nPress any key to Exit...")