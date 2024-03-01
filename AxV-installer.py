import os, webbrowser, shutil

print("AntixVirus Installer - for Version 1.0.0")

pathstartup = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
pathdled = f"C:\\Users\\{os.getlogin()}\\Downloads"
pathinstalled = "C:\\AxV"

webbrowser.open_new_tab("https://extremecreator20.github.io/files/AxV/AntixVirus.py")
webbrowser.open_new_tab("https://extremecreator20.github.io/files/AxV/AntixVirusService.py")
webbrowser.open_new_tab("https://extremecreator20.github.io/files/AxV/config.json")

os.makedirs("C:\\AxV", exist_ok=True)

shutil.move(f"{pathdled}\\AntixVirusService.py", f"{pathinstalled}\\AntixVirusService.py")
shutil.move(f"{pathdled}\\AntixVirus.py", f"{pathinstalled}\\AntixVirus.py")
shutil.move(f"{pathdled}\\config.json", f"{pathinstalled}\\config.json")

os.system("python3 -m pip3 install PyAudio")
os.system("python3 -m pip3 install pydub")

os.link(pathinstalled+"\\AntixVirusService.py",pathstartup+"\\AxVService.py")