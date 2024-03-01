import hashlib, glob, os, subprocess, json, requests, threading, psutil
from pydub import AudioSegment
from pydub.playback import play

sus = AudioSegment.from_wav("suspicious.wav")
mal = AudioSegment.from_wav("malicious.wav")

#args = sys.argv[1:]



def calculate_md5(filename):
    with open(filename, 'rb') as file:
        file_hash = hashlib.md5()
        while chunk := file.read(8192):
            file_hash.update(chunk)
        return file_hash.hexdigest()

folder_path = json.load(open("config.json", "r"))["path"].replace("<un>", os.getlogin())
list_of_files = glob.glob(f'{folder_path}/*')
latest_file = max(list_of_files, key=os.path.getctime)

file_name = latest_file
filehash = calculate_md5(file_name)

analysis = subprocess.check_output(["vt", "file", f"{filehash}"])

result = analysis.decode('utf-8')

result = result.split('"')

def analyze(result):
    undetected = 0
    malicious = 0
    suspicious = 0
    harmless = 0
    for i in result:
        if i.lower() == "undetected":
            undetected += 1
        elif i.lower() == "suspicious":
            suspicious += 1
        elif i.lower() == "harmless":
            harmless += 1
        elif i.lower() == "malicious":
            malicious += 1
    
    return undetected, suspicious, harmless, malicious

undetected, suspicious, harmless, malicious = analyze(result)

print(f"File: {file_name}\nFile hash: {filehash}\n\nClean: {harmless}\nSuspicious: {suspicious}\nMalicious: {malicious}\nUndetected: {undetected}")

if malicious > 0:
    play(mal)
elif suspicious > 0:
    play(sus)