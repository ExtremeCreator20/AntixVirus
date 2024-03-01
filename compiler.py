from cx_Freeze import setup, Executable

base = None

executables = [Executable("AxV-installer.py", base=base)]

packages = ["idna", "os", "webbrowser", "shutil"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "AntixVirus Installer",
    options = options,
    version = "1.0.0",
    description = 'AntixVirus Installer',
    executables = executables
)