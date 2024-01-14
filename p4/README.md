# Program to Convert Time from 12-Hour Format to 24-Hour Format

## Introduction

This documentation provides a solution in Python for converting time from the 12-hour format to the 24-hour format. Two approaches are presented: one utilizing the `datetime` module, and the other using a custom approach.

### Datetime Approach

The first approach employs the `datetime` module, a powerful library in Python for working with dates and times.

```python
from datetime import datetime

def convert_24hrs(time_12hrs):
    time_object = datetime.strptime(time_12hrs, "%I:%M %p")
    time_24hrs = time_object.strftime("%H:%M")
    return time_24hrs

time_12hrs = input("Enter the time in 12-hour format (hh:mm am/pm): \n")

time_24hrs = convert_24hrs(time_12hrs)
print(f"Converted time is {time_24hrs}")
```

#### Walkthrough:

1. **Importing the `datetime` Module:**
   The code begins by importing the `datetime` module, which provides classes for working with dates and times.

2. **Function Definition:**
   The `convert_24hrs` function takes a time string in the 12-hour format as input, converts it to a `datetime` object, and then formats it to the 24-hour format using the `strftime` method.

3. **User Input:**
   The user is prompted to enter a time in the 12-hour format.

4. **Conversion and Output:**
   The input time is passed to the `convert_24hrs` function, and the converted time in the 24-hour format is printed.

### Custom Approach

The second approach is a custom implementation without relying on external modules.

```python
def convert_24hrs(time_12hrs):
    hrs, min_ampm = time_12hrs.split(":")
    min, am_pm = min_ampm[:2], min_ampm[2:]
    hrs = int(hrs)

    if am_pm.lower() == "pm" and hrs != 12:
        hrs += 12
    elif am_pm.lower() == "am" and hrs == 12:
        hrs = 0

    time_24hrs = f"{hrs:02d}:{int(min):02d}"
    return time_24hrs

time_12hrs = input("Enter the time in 12-hour format (hh:mm am/pm): \n")

time_24hrs = convert_24hrs(time_12hrs)
print(f"Converted time is {time_24hrs}")
```

#### Walkthrough:

1. **Function Definition:**
   The `convert_24hrs` function takes a time string in the 12-hour format as input and performs a manual conversion to the 24-hour format.

2. **Input Parsing:**
   The input time is split into hours, minutes, and AM/PM components.

3. **Conversion Logic:**
   The function adjusts the hours based on the AM/PM component, ensuring correct conversion to the 24-hour format.

4. **Output:**
   The converted time in the 24-hour format is printed.

## Conclusion

Both approaches provide reliable solutions to convert time from the 12-hour format to the 24-hour format. The choice between them may depend on specific project requirements or personal coding preferences.