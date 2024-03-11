import time, json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, threading, psutil



def callAxV():
    os.system("python3 antixvirus.py")

class NewFileEvent(FileSystemEventHandler):
    def on_created(self, event):
        print(f"File created: {event.src_path}")

    def on_modified(self, event):
        print(f"File modified: {event.src_path}")
        if not (event.src_path.endswith(".tmp") or event.src_path.endswith(".crdownload")):
            callAxV()


while True:
    observer = Observer()
    eventhandler = NewFileEvent()
    observer.schedule(eventhandler, path=json.load(open("config.json", "r"))["path"].replace("<un>", os.getlogin()))
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()