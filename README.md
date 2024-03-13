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

main.py is the python code to process the data
cumulative.csv is the raw data before processing
new_file.csv is the output data
ovens.pdf is the chart that was created using excel on the output data
