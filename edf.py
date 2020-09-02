#!/usr/bin/env python
import sys
import csv
import os
from datetime import datetime, timedelta;

def get_nearest_deadline():
    lowest_deadline = 99999999;
    lowest_deadline_task = "";
    with open('/var/tmp/deadlines.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            deadline = date_to_deadline(row[' date']);
            if(deadline < lowest_deadline):
                lowest_deadline_task = row['task'];
                lowest_deadline = deadline;
    print("Task to complete: ", lowest_deadline_task)
    print("Deadline (in days): ", lowest_deadline);

def add_deadline(task, deadline_days):
    with open('/var/tmp/deadlines.csv', 'a') as csvfile:
        s =task + "," + deadline_to_date(deadline_days).strftime("%Y-%m-%d") + "\n";
        csvfile.write(s)

def deadline_to_date(d1):
    current_date = datetime.today()
    deadline_date = (datetime.today() + timedelta(int(d1)))
    return deadline_date;
                
def date_to_deadline(d1):
    deadline_date = datetime.strptime(d1, "%Y-%m-%d");
    return abs((deadline_date - datetime.today()).days);


if(len(sys.argv) < 2):
    print("Here are the commands")

#check if pop
elif('pop' in sys.argv[1]) :
    exit();

#check if add
elif('add' in sys.argv[1]) :
    add_deadline(sys.argv[2], sys.argv[3]);

#check if ask
elif('ask' in sys.argv[1]) :
    get_nearest_deadline(); 
