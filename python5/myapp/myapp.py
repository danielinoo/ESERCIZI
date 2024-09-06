
import time
import sys
while True:
    time.sleep(5)

    #da docker "stdout" file che punta i print da default dentro un file
    #senza "flush" manda i print dopo na certa
    sys.stdout.flush()
    print("ciao a tutti da my app")

    