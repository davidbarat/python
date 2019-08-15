def main(argv):                          
    grammar = "kant.xml"                
    try:                                
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
    except getopt.GetoptError:          
        usage()                         
        sys.exit(2)                     
    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            usage()                    
            sys.exit()                  
        elif opt == '-d':                
            global _debug               
            _debug = 1                  
        elif opt in ("-g", "--grammar"): 
            grammar = arg               

    source = "".join(args)               

    k = KantGenerator(grammar, source)
    print k.output()
    
import ftplib
session = ftplib.FTP('server.address.com','USERNAME','PASSWORD')
file = open('kitten.jpg','rb')                  # file to send
session.storbinary('STOR kitten.jpg', file)     # send the file
file.close()                                    # close file and FTP
session.quit()

Use ftplib.FTP_TLS instead if you FTP host requires TLS

fig, axes = plt.subplots(ncols=2)
for ax, markers in zip(axes, split_list(Line2D.filled_markers)):
    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **text_style)
        ax.plot(y * points, marker=marker, **marker_style)
    format_axes(ax)
fig.suptitle('filled markers', fontsize=14)

plt.show()

import pycron
import time

while True:
    if pycron.is_now('0 2 * * 0'):   # True Every Sunday at 02:00
        print('running backup')
    time.sleep(60)
 
import matplotlib
import matplotlib.pyplot as plt
import csv
with open('MaxMin.txt','r') as f_input:
    csv_input = csv.reader(f_input, delimiter=' ', skipinitialspace=True)
    x = []
    y = []
    for cols in csv_input:
        x.append(matplotlib.dates.datestr2num(cols[0]))
        y.append(float(cols[1]))
# naming the x axis 
plt.xlabel('Real-Time') 
# naming the y axis 
plt.ylabel('Acceleration (m/s2)') 
# giving a title to my graph 
plt.title('Accelerometer reading graph!')
# plotting the points 
plt.plot_date(x, y)
# beautify the x-labels
plt.gcf().autofmt_xdate()
# function to show the plot 
plt.show()



Alternate method of launching Java Control Panel

    Click Windows Start button.
    In the Start Search box, type:
    Windows 32-bit OS: c:\Program Files\Java\jre7\bin\javacpl.exe
    Windows 64-bit OS: c:\Program Files (x86)\Java\jre7\bin\javacpl.exe

<User Application Data Folder>\Sun\Java\Deployment\log on Windows
