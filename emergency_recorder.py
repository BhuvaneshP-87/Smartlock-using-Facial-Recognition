import cv2
import timeit
import datetime

async def emergency_recording():
    
    cap = cv2.VideoCapture(0)
    
    filename='emergency-recordings/VID-'
    time=datetime.datetime.now()
    filename += time.strftime("%m-%d-%Y-%H.%M.%S")+".avi"
    codec = cv2.VideoWriter_fourcc(*'MJPG')
    framerate = 20
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    size = (frame_width, frame_height)
    
    VideoFileOutput = cv2.VideoWriter(filename, codec,framerate, size)
    start = timeit.default_timer()
    
    while True:
        
        ret, frame = cap.read()
        VideoFileOutput.write(frame)     
        cv2.imshow("Emergency Capture", frame)
        if timeit.default_timer()-start>=12:
            break
            
    cv2.destroyAllWindows()
    VideoFileOutput.release() 
    cap.release()
    return (filename,time.strftime("%m/%d/%Y-%H:%M:%S"))