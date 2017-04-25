# TODO: Add comments about what this script does
# TODO: Add names of authors and copyright

#TODO: import time and camera modules


import serial

# TODO: Write a function that returns a filename in the form of a timestamp.
# This should be guarenteed to be unique so we never overwrite any files.
# It also should not include any spaces. Hint: time.strftime()
# Example might be: 
# def timestamp_filename():
#     fname = <some code here>
#     return fname


# TODO: Comment on what is happening here:
ser = serial.Serial('/dev/ttyACM0')


# TODO: Comment on what is happening here:
while 1 :
    line = ser.readline()

#   TODO: Look at line and decide if we need to take a photo:


#   TODO: Take the photo and save it to a file




