from datetime import datetime
from time import sleep

while True:
    hora = datetime.now()
    print(hora.strftime('%H:%M:%S:%f'))
    sleep(.001)

# done
