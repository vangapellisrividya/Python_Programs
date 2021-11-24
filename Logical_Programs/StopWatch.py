'''	
    @Author: Srividya
    @Date:  2021-11-18 
    @Title: StopWatch
    '''

import time
try:
    def time_convert(sec):
        """
            Description: Calculating the timeelapse between start
            and stop time
            Parameter: sec
            Return: 

            """
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
        return sec
    
except Exception as e:
    print(e)
    
if __name__=='__main__':
    input("Press Enter to start")
    start_time = time.time()
    input("Press Enter to stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
   
