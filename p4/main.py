from datetime import datetime

def convert_24hrs(time_12hrs):
    time_object = datetime.strptime(time_12hrs, "%I:%M %p")
    time_24hrs = time_object.strftime("%H:%M")
    return time_24hrs

time_12hrs = input("enter the time in 12 hours format hh:mm am/pm \n")

time_24hrs = convert_24hrs(time_12hrs)
print(f"Converted time is {time_24hrs}")