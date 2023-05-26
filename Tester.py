import requests
import threading
import ctypes
import datetime
import os

# Load the shared library
# try:
lib = ctypes.CDLL("URL_Creator.so")
# except:
#     path = os.getcwd()
#     path += "\\URL_Creator"
#     lib = ctypes.CDLL(path)


# Define the function signature
lib.makeURL.restype = ctypes.c_char_p

def createURL():
    return lib.makeURL().decode('utf-8')

    
f = open("working_urls.txt", "a")

attempts = 0
lock = threading.Lock()

def Test():
    global attempts
    while True:
        link = createURL()
        x = requests.get(link)

        if "This video isn't available any more" not in x.text:
            print("\n\n\n\n\n",link, startTime - datetime.datetime.now(), "\n\n\n\n\n\n")
            with lock:
                f.write(link)
                attempts += 1
        else:
            with lock:
                attempts += 1
                print(attempts, "Attempts. Time since starting", datetime.datetime.now()-s, end='\r')

# Create and start multiple threads
num_threads = int(input("Type in the thread amount (Recccomended is 15)\n"))
s = datetime.datetime.now()
print(s)
threads = []

for _ in range(num_threads):
    t = threading.Thread(target=Test)
    t.start()
    threads.append(t)

# Wait for all threads to complete
for t in threads:
    t.join()

f.close()
