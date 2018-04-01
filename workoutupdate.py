#Take WOD and add it to list of workouts done

read_from_wod = open('WOD.txt','r')
wod_copied = read_from_wod.read()

wr_to_history = open('workouthistory.txt','a')
wr_to_history.write('\n' + wod_copied) 
wr_to_history.close()