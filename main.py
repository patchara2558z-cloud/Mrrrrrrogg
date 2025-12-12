#-------------------------------------------------#
#             BEST GUI TOOL BY HYPER              #
#-------------------------------------------------#
#          dont touch code and color              #
#-------------------------------------------------#








import os
import sys
import time
import getpass
import webbrowser
import subprocess
from datetime import datetime
from colorama import init, Fore, Style




username_pc = getpass.getuser()

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear') 
os.system(                        '               title                                      RedTiger 6.6 - Menu1           ' if os.name == 'nt' else '')  




def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rgb_color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

start_color = (168, 5, 5)
end_color = (255, 118, 118)
steps = 30
colors = []
for i in range(steps):
    r = start_color[0] + (end_color[0] - start_color[0]) * i // (steps - 1)
    g = start_color[1] + (end_color[1] - start_color[1]) * i // (steps - 1)
    b = start_color[2] + (end_color[2] - start_color[2]) * i // (steps - 1)
    colors.append((r, g, b))
colors += list(reversed(colors[:-1]))

white = Fore.WHITE

title_lines = [
    "", 
    "                              โ–โ–โ–€โ–โ–โ–  โ–“โ–โ–โ–โ–โ– โ–“โ–โ–โ–โ–โ–โ–    โ–โ–โ–โ–โ–โ–โ–โ–โ–“ โ–โ–โ–“  โ–โ–โ–โ–โ– โ–“โ–โ–โ–โ–โ–  โ–โ–โ–€โ–โ–โ–",
    "                             โ–“โ–โ– โ–’ โ–โ–โ–’โ–“โ–   โ–€ โ–’โ–โ–โ–€ โ–โ–โ–   โ–“  โ–โ–โ–’ โ–“โ–’โ–“โ–โ–โ–’ โ–โ–โ–’ โ–€โ–โ–’โ–“โ–   โ–€ โ–“โ–โ– โ–’ โ–โ–โ–’",
    "                             โ–“โ–โ– โ–‘โ–โ– โ–’โ–’โ–โ–โ–   โ–‘โ–โ–   โ–โ–   โ–’ โ–“โ–โ–โ–‘ โ–’โ–‘โ–’โ–โ–โ–’โ–’โ–โ–โ–‘โ–โ–โ–โ–‘โ–’โ–โ–โ–   โ–“โ–โ– โ–‘โ–โ– โ–’",
    "                             โ–’โ–โ–โ–€โ–€โ–โ–  โ–’โ–“โ–  โ– โ–‘โ–“โ–โ–   โ–   โ–‘ โ–“โ–โ–โ–“ โ–‘ โ–‘โ–โ–โ–‘โ–‘โ–“โ–  โ–โ–โ–“โ–’โ–“โ–  โ– โ–’โ–โ–โ–€โ–€โ–โ–",
    "                             โ–‘โ–โ–โ–“ โ–’โ–โ–โ–’โ–‘โ–’โ–โ–โ–โ–โ–’โ–‘โ–’โ–โ–โ–โ–โ–“      โ–’โ–โ–โ–’ โ–‘ โ–‘โ–โ–โ–‘โ–‘โ–’โ–“โ–โ–โ–โ–€โ–’โ–‘โ–’โ–โ–โ–โ–โ–’โ–‘โ–โ–โ–“ โ–’โ–โ–โ–’",
    "                             โ–‘ โ–’โ–“ โ–‘โ–’โ–“โ–‘โ–‘โ–‘ โ–’โ–‘ โ–‘ โ–’โ–’โ–“  โ–’      โ–’ โ–‘โ–‘   โ–‘โ–“   โ–‘โ–’   โ–’ โ–‘โ–‘ โ–’โ–‘ โ–‘โ–‘ โ–’โ–“ โ–‘โ–’โ–“โ–‘",
    "                              โ–‘โ–’ โ–‘ โ–’โ–‘ โ–‘ โ–‘  โ–‘ โ–‘ โ–’  โ–’        โ–‘     โ–’ โ–‘  โ–‘   โ–‘  โ–‘ โ–‘  โ–‘  โ–‘โ–’ โ–‘ โ–’โ–‘",
    "                              โ–‘โ–‘   โ–‘    โ–‘    โ–‘ โ–‘  โ–‘      โ–‘       โ–’ โ–‘โ–‘ โ–‘   โ–‘    โ–‘     โ–‘โ–‘   โ–‘",
    "                              โ–‘        โ–‘  โ–‘   โ–‘                 โ–‘        โ–‘    โ–‘  โ–‘   โ–‘      ",  
]

def print_gradient_line_centered_with_indent(line, offset=0):
    terminal_width = os.get_terminal_size().columns if os.name != 'nt' else 80
    line_stripped = line.lstrip(' ')
    indent = len(line) - len(line_stripped)
    line_length = len(line_stripped)
    padding = max((terminal_width - line_length) // 2 - indent, 0)

    colored_line = " " * (padding + indent)
    for i, char in enumerate(line_stripped):
        color_index = (i + offset) % len(colors)
        r, g, b = colors[color_index]
        colored_line += rgb_color(r, g, b) + char
    colored_line += Style.RESET_ALL
    print(colored_line)

def animated_title_cascade_centered(delay=0.05):
    offset = 0
    clear_screen()
    for line in title_lines:
        print_gradient_line_centered_with_indent(line, offset)
        offset += 1
        time.sleep(delay)


def MainColor(text):
    start_color = (168, 5, 5)  
    end_color = (255, 118, 118)

    num_steps = 9

    colors_local = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors_local.append((r, g, b))
    
    colors_local += list(reversed(colors_local[:-1]))  
    
    gradient_chars = '[]โ”ดโ”ผโ”โ”คโ””โ”โ”€โ”ฌโ”โ”โ””โ”โ–‘โ–’โ–‘โ–’โ–โ–“โ–โ–โ–€()'

    
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
       
    lines = text.split('\n')
    num_colors = len(colors_local)
    
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in gradient_chars:
                color_index = (i + j) % num_colors
                color = colors_local[color_index]
                result.append(text_color(*color) + char + "\033[0m")
            else:
                result.append(char)
        if i < len(lines) - 1:
            result.append('\n')
    
    return ''.join(result)

menu_border = '''
                                           github.com/loxy0dev/RedTiger-Tools
 โ”โ”€ [I] Info                                                                                               Next [N] โ”€โ”
 โ”โ”€ [S] Site โ”โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”                        โ”โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”                           โ”โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”            โ”
 โ””โ”€โ”ฌโ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”ค Network Scanner โ”โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”ฌโ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”ค Osint โ”โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”ฌโ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”ค Utilities โ”โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”ดโ”€
   โ”         โ””โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”         โ”              โ””โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”              โ”            โ””โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”€โ”
   โ”โ”€ [01] Website Vulnerability Scanner โ”โ”€ [10] D0x Create                    โ”โ”€ [20] Phishing Attack
   โ”โ”€ [02] Website Info Scanner          โ”โ”€ [11] D0x Tracker                   โ”โ”€ [21] Password Zip Cracked Attack
   โ”โ”€ [03] Website Url Scanner           โ”โ”€ [12] Get Image Exif                โ”โ”€ [22] Password Hash Decrypted Attack
   โ”โ”€ [04] Ip Scanner                    โ”โ”€ [13] Google Dorking                โ”โ”€ [23] Password Hash Encrypted
   โ”โ”€ [05] Ip Port Scanner               โ”โ”€ [14] Username Tracker              โ”โ”€ [24] Search In DataBase
   โ””โ”€ [06] Ip Pinger                     โ”โ”€ [15] Email Tracker                 โ”โ”€ [25] Dark Web Links
                                         โ”โ”€ [16] Email Lookup                  โ””โ”€ [26] Ip Generator
                                         โ”โ”€ [17] Phone Number Lookup
                                         โ”โ”€ [18] Ip Lookup
                                         โ””โ”€ [19] Instagram Account
'''



def print_menu():
    print(MainColor(menu_border))

def main():
    username = getpass.getuser()
    animated_title_cascade_centered(delay=0.03)

    while True:
        print_menu()
        print(f"{Fore.RED}โ”โ”€โ”€โ”€({Fore.WHITE}{username}@redtiger{Fore.RED}){Fore.RED}-[{Fore.WHITE}~/Windows/Menu-1{Fore.RED}] ")
        user_input = input(f"{Fore.RED}โ””โ”€{Fore.WHITE}$ ")
        if user_input.lower() in ['exit', 'quit', 'q']:
            break
        clear_screen()

        if user_input in ['0', 'exit', 'quit', 'q']:
           break 

        elif user_input == 's':
            option1()

       
        


           



import sys
import os
import webbrowser
import subprocess
from datetime import datetime
from colorama import Fore

def current_time_hour():
    
    return datetime.now().strftime('%H:%M:%S')

def find_redtiger_script():
    
    for root, dirs, files in os.walk('C:/'):  
        if 'RedTiger.py' in files:
            return os.path.join(root, 'RedTiger.py')
    return None  # 

def option1():
    banner = f"""{Fore.RED}
                                                         .+#%@@%#+.                                     
                                                    .#@@@@@@@@@@@@@@@@#.                                
                                                  +@@@@@@@@@@@@@@@@@@@@@@*                              
                                                .%@@@@@@@@@@@@@@@@@@@@@@@@%.                            
                                                %@@@@@@@@@@@@@@@@@@@@@@@@@@%                            

                                               %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                          
                                                -..........................-.                           
                                                %@@@@@@%%@@@@@@@@@@@%@@@@@@%                            
                                                %@@@#     .%@@@@%.     *@@@%                            
                                                . :+%%+--+%@#::#@%*--+%%+: .                            
                                                                           .                            
                                                 :                        :                             
                                                  -                      =                              
                                                    -                  -                                
                                                       -=          --                                   
                                               -+#%@@@@@@=        =@@@@@@%#+-                           
                                            *@@@@@@@@@@@@=        =@@@@@@@@@@@@*                        
                                          *@@@@@@@@@@@@@@+        +@@@@@@@@@@@@@@#                      
                                         *@@@@@@@@@@@@@@@@%=    -%@@@@@@@@@@@@@@@@#                     
                                        -@@@@@@@@@@@@@@@@@@@%#*%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-
"""
    print(banner)
    webbrowser.open("https://guns.lol/Hyperpr")
    input(f"{Fore.RED}[{Fore.WHITE}{current_time_hour()}{Fore.RED}] {Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.RED}Press To Continue Don't touch all ->")
   
    script_path = find_redtiger_script()
    if script_path:
      
        python = sys.executable  
      
        subprocess.Popen([python, script_path] + sys.argv[1:])
    else:
        
        print(f"{Fore.RED}[{Fore.WHITE}{current_time_hour()}{Fore.RED}] {Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.RED}Press To Continue Don't touch all ->")
        input(f"{Fore.RED}[{Fore.WHITE}{current_time_hour()}{Fore.RED}] {Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.RED}Errore: RedTiger.py non trovato!")









if __name__ == "__main__":
    main()
