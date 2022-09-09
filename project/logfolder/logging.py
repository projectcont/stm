import datetime
from datetime import datetime
from paths import *



def log_txt (*args):
    total=''
    for arg in args:
        if  (str(arg)) != '0':
            total = total + str(arg)

    fileOut=open(pathlog, 'a')
    fileOut.write(total + '\n')
    fileOut.close()



def log_date ():
    now = datetime.now()
    fileOut=open(pathlog, 'w')
    fileOut.write(now.strftime("%m/%d/%Y, %H:%M:%S") + '\n')
    fileOut.close()