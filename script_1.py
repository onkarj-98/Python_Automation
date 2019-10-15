"""
@uther: Onkar Jaliminche
Task : When a file or script or any kind  directory created in this directory should be destroyed in some time after created.
"""


from watchdog.observers import Observer
from threading import Timer 
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
	def on_created(self,event):
		for filename in os.listdir(folder_to_track):
			experiment_folder = folder_to_track + "/"+ filename
			t = Timer(60 * 2,os.remove(folder_to_track + "/"+ filename) )  # testing
			t.start()
			t.join()  # wait for time completion
					

folder_to_track = '/home/onkar/RoughWork'  
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive = True)
observer.start()


try:
	while True:
		time.sleep(1)
except KeyBoardInterrupt:
	observer.stop()
observer.join()
		
																						
		


