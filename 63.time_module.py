import time

print(time.ctime(0))    #convert a time expressed in seconds since epoch to a redeable string

print(time.time())      #return current seconds since epoch

print(time.ctime(time.time()))  # will get current time

time_object = time.localtime()
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
print(local_time)

time_string = "20 April, 2020"
new_time_object = time.strptime(time_string, "%d %B, %Y")
print(new_time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string2 = time.asctime(time_tuple)
print(time_string2)