import time
epoch_time = time.time()
current_time = time.ctime(epoch_time)
task_name = input("Please enter task name \n <note> timer will start when you enter the task name: ")

#Setting a start time
start_time = time.time()
last_time = start_time
value = " "

print("Press ENTER for each lap.\nType Q and press ENTER to stop.")

# turn the input value into lower case
# while the input is not stop, 
while value.lower() != "q":
    # input to start
    value = input()
    # total time elapsed since the timer started
    total_time = round((time.time() - last_time), 2)

    # printing the lap number, lap time and total time
    print("Total Time: " + str(total_time))

    print("*" * 20)

    last_time = time.time()

print("complete")