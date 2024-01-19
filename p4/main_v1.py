
def convert_24hrs(time_12hrs):
    hrs, min_ampm = time_12hrs.split(":")
    min, am_pm = min_ampm[:2], min_ampm[2:]
    hrs = int(hrs)

    if am_pm.lower() == "pm" and hrs !=  12:
        hrs += 12
    elif am_pm.lower() == "am" and hrs == 12:
        hrs = 0

    time_24hrs = f"{hrs:02d}:{int(min):02d}"
    return time_24hrs
    

time_12hrs = input("enter the time in 12 hours format hh:mm am/pm \n")

time_24hrs = convert_24hrs(time_12hrs)
print(f"Converted time is {time_24hrs}")


