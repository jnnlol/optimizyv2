try:
    import random
    import time
    import os
    import string
    import fade
    import colorama
    from colorama import Fore
    import socket
    import shutil
    import webbrowser
    import platform
except ModuleNotFoundError:
    os.system("pip install fade")
    os.system("pip install colorama")
    os.system("python optimizyv2.py")

colorama.init(autoreset=True)

processor = platform.processor()
#i cant set as OS because of import
#could just use OS for this but who cares
if platform.system()!= "Windows":
    print(Fore.RED+"This is a WINDOWS Only program. Please try OPTIMIZY V2 On a windows platform.")
    input(Fore.RED+"Press ENTER To quit...")
    quit()

#Set all vars
pcname = os.getlogin()
desktop_name = socket.gethostname()
version = "V.Beta"
os.system("title @jnnlol on yt")
placeholder_alphabet = string.digits + string.ascii_letters
key = "".join(random.choices(placeholder_alphabet, k=5))
title = fade.purpleblue("""
\t\t\t\t\t     ██╗███╗   ██╗███╗   ██╗
\t\t\t\t\t     ██║████╗  ██║████╗  ██║
\t\t\t\t\t     ██║██╔██╗ ██║██╔██╗ ██║
\t\t\t\t\t██   ██║██║╚██╗██║██║╚██╗██║
\t\t\t\t\t╚█████╔╝██║ ╚████║██║ ╚████║
\t\t\t\t\t ╚════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝
                                                  .gg/jnn
""")
special_thanks = fade.fire("""
\t\t\t\t\t\t   🎆300🎆
\t\t\t\t\t\t   🎆Sub🎆
\t\t\t\t\t         🎆Special🎆
""")
placeholder_table = """
\t\t\t\t\t      ╔═══════════════╗
\t\t\t\t\t      ║ OPTIMIZATIONS ║
\t\t\t\t\t      ╚═══════════════╝
\t\t\t[1] Internet Commands [2] Clear Temp Files [3] Internet Speed Test
\t\t\t[4] Find and fix corrupt files [5] Show system info [6] Fps Unlocker (ROBLOX)
\t\t\t                    [10] ALL OPTIMIZATIONS
\t\t\t------------------------------------------------------------------
\t\t\t                      [69] Restart PC
\t\t\tChoose Here:
"""

#TITLE PLACEHOLDER, WHEN PRINT TITLE PRINT: fade.purpleblue(ptitle)
#-----------


def loading():
    for x in range(1,8):
        loading_catphrases = (
    "Compiling quantum code snippets",
    "Optimizing multi-threaded logic loops",
    "Initializing neural network connections",
    "Debugging the quantum entanglement protocol",
    "Calibrating cryptographic key matrices",
    "Synchronizing cloud server clusters",
    "Accelerating GPU warp drives",
    "Decrypting the core encryption algorithm",
    "Loading terabytes of cyber-essence",
    "Refactoring nanobot swarm control",
    "Syncing up with interstellar data arrays",
    "Initializing time-traveling algorithms",
    "Defragmenting quantum memory arrays",
    "Syncing up with the metaverse mainframe",
    "Rendering holographic user interfaces"
)
        loading_catchprase_randomized = random.choice(loading_catphrases)
        print(fade.random("[Loading] "+loading_catchprase_randomized))
        time.sleep(1.4)
        os.system("cls")
loading()
print(Fore.GREEN+"Found OS!: "+platform.system())#always gonna be windows bc of OS check but its automated so it works
time.sleep(2)
#Real code
print(title)

def write_settings_to_file(content, path):
    with open(os.path.join(path, 'ClientAppSettings.json'), 'w') as file:
        file.write(content)
        print(Fore.GREEN + "Succesfully uncapped fps (this took me 3 minutes to code)" + Fore.RESET)


def internetopti():
    print("Starting internet optimization now...")
    time.sleep(3)
    os.system("cls")

    print(title)
    os.system("ipconfig /flushdns")
    os.system("cls")
    print(title)
    
    os.system("ipconfig /registerdns")
    os.system("cls")
    print(title)

    os.system("ipconfig /release")
    os.system("cls")
    print(title)

    os.system("ipconfig /renew")
    os.system("cls")
    print(title)

    os.system("netsh winsock reset")
    os.system("cls")
    print(title)
    print(Fore.GREEN+"All done! Going back to main menu...")
    os.system("cls")
    print(title)


def deletetempfile():
    folder = 'C:/Users/' + os.getlogin() + '/AppData/Local/Temp'
    deleteFileCount = 0
    deleteFolderCount = 0

    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo + 1:]
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print('%s file deleted' % Fore.GREEN + itemName)
                deleteFileCount = deleteFileCount + 1
            elif os.path.isdir(file_path):
                if 'chocolatey' in file_path:
                    continue
                shutil.rmtree(file_path)
                print('%s folder deleted' % itemName)
                deleteFolderCount = deleteFolderCount + 1
        except Exception as e:
            print(Fore.RED + "")

    print(Fore.GREEN+'Deleting...')
    print(Fore.GREEN + "Deleted ALL deletable temp files!")
    time.sleep(1)
    os.system("cls")
    print(title)


def internetspeedtest():
    print(Fore.GREEN+"Opening Okla Speed Test...")
    webbrowser.open("https://www.speedtest.net/")
    print(Fore.GREEN+"Opened...")
    time.sleep(3)
    os.system("cls")
    print(title)

def pc_specs():
    print(Fore.RED+"Getting CPU Parts")
    processor = platform.processor()
    machine = platform.machine()
    system = platform.system()
    version = platform.version()
    print(Fore.GREEN+"Found machine info!")
    print(f"""
Processor: {processor}
Machine: {machine}
OS: {system}
Version: {version}
""")
    input(Fore.GREEN+"Press ENTER To go back to main menu...")

def fix_corrupt_file():
    print(Fore.GREEN+"Finding and FIXING Corrupt system files...")
    os.system("sfc /scannow")
    print(Fore.GREEN+"Fixed ALL Corrupted system files.")
    print("Press ENTER To go back to main menu...")
    os.system('cls')

def all_optimizations():
    print(Fore.GREEN+"Starting ALL OPTIMIZATIONS!")
    internetopti()
    deletetempfile()
    fix_corrupt_file()
    os.system("cls")
    print(title)
    all_optimizations_restart = input(Fore.RED+"Finished ALL OPTIMIZATIONS! Would you like to restart pc? (Y/N): ")
    if all_optimizations_restart == "y":
        os.system("shutdown /r /f /t 0")
    else:
        pass

def fpsunlocker():

    fps_cap = input("Enter FPS Cap (60-360)")
    fps_fflags = """
{
    "DFIntTaskSchedulerTargetFps": """+fps_cap+""",
    "FFlagDebugDisplayFPS": false,
    "FFlagDebugSkyGray": true,
    "FIntCameraFarZPlane": 600
}
"""
    path = input("Please enter ClientAppSettings path: ")
    if os.path.exists(path):
        print(Fore.YELLOW+"Checking path...")
        time.sleep(0.3)
        print(Fore.GREEN+"Path exists!")
    else:
        print(Fore.RED+"Invalid path...")
        input("Press ENTER To go back to main menu...")
    
    if "ClientSettings" in path:
        print(Fore.GREEN+"ClientSettings checked!")
    else:
        print("Invalid ClientSettings but correct path...")
        input("Press ENTER To go back to main menu..")
    write_settings_to_file(fps_fflags, path)



while True:
    os.system("cls")
    print(special_thanks)
    print(title)
    table = input(fade.purplepink(placeholder_table))

    if table == "1":
        internetopti()
    elif table == "2":
        deletetempfile()
    elif table == "3":
        internetspeedtest()
    elif table == "4":
        fix_corrupt_file()
    elif table == "5":
        pc_specs()
    elif table == "6":
        fpsunlocker()
    elif table == "69":
        os.system("shutdown /r /f /t 0")
    elif table == "10":
        all_optimizations()
    else:
        os.system("cls")
        print(Fore.RED+"Invalid option... Going back to main menu in 3 seconds")
        time.sleep(1)
        os.system("cls")
        print(Fore.RED+"Invalid option... Going back to main menu in 2 seconds")
        time.sleep(1)
        os.system("cls")
        print(Fore.RED+"Invalid option... Going back to main menu in 1 seconds")
        time.sleep(1)
        os.system("cls")
        print(title)
