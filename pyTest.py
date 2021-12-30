import time
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = list() 
y1 = list()
y2 = list()

line = None

ser = serial.Serial(
 port='/dev/ttyACM0',
 baudrate = 115200,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)
        
def read_serial():
    
    global line
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line) 
    
def animate(i):

    global x
    global y1
    global y2
    
    read_serial()
    
    if line != '':
        data = line.split(' ')
    
    try:   

        ## Create empty list !!
            x.append(data[0])
            y1.append(data[1])
            y2.append(data[2])
            
            ax.plot(x, y1, label="Abs")
            ax.plot(x, y2, label="Inc")
            
    except Exception as e:
        pass
    
    plt.title("Motion Graph")
    ## Label x-axis !!
    plt.xlabel('Time/Second')
    ## Label y-axis !!
    plt.ylabel('Absolute Vs Incremental Angle')
    ## Draw legend !!
    #plt.legend()
    ##grid
    plt.grid()
    ## Show plot !! 
   
try:
    anim = animation.FuncAnimation(fig, animate, interval=100)
        #writervideo = animation.FFMpegWriter(fps=30) 
        #anim.save(video, writer=writervideo)
    plt.show()
        
except KeyboardInterrupt:
        log_file.close()
        sys.exit()
