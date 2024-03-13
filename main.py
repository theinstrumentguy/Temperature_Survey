"""
For a project at work, I had four days worth of temperatures recorded on 5 
different probes every 10 seconds.  This ammounted to over 200,000 data points
that I wanted to present graphically to the customer.  I found that my graph 
displayed the data well if I paired it down to only one data point per minute. 
I also found that there were long idle periods where the ovens we were monitoring
were not running, so I exluded any times where the average of the 5 probes was 
85F or less.  I also exluded any times where the average of the probes was 1000F 
or greater.  During the process of setting up the data recorder or moving it from
one oven to the next, if a probe was disconnected there would be an erroneously 
high reading.  After exluding these points, I got down to about 35,000 data
points.  This was plenty to show to the customer graphically what was going on
but was much lighter on processing power in Excel to creat the graph.  
"""


def process():
    """This is the function that will open the file and process some data"""
    header = True
    line_count = 0 
    with open('cumulative.csv', 'r') as file: #raw data file
        with open('new_file.csv', 'w') as new_file: #output file
            for line in file.readlines():
                if header:
                    new_file.write(line) # write the header on the new file
                    header = False
                    continue
                line_data = line.split(',') #Comma separated values
                temp_1 = float(line_data[2]) #Get temperature values
                temp_2 = float(line_data[3])
                temp_3 = float(line_data[4])
                temp_4 = float(line_data[5])
                temp_5 = float(line_data[6])
                sum_temps = temp_1 + temp_2 + temp_3 + temp_4 + temp_5
                if sum_temps <= 425: #Average temperature less than 85 Excluded
                    continue
                if sum_temps >= 5000: # erroneous Large (such as changing probe connections)
                    continue
                if line_count % 6 == 0: #Only include one data point per minute
                    new_file.write(line)
                line_count += 1
if __name__ == 'main':                
    process()
