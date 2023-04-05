'''
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it
expressed in hours:minutes:seconds.

Input

The input file contains an integer N.

Output

Print the read time in the input file (seconds) converted in hours:minutes:seconds like the 
following example.

556
	
0:9:16


1
	
0:0:1


140153
	
38:55:53

'''
time_seconds = int(input())

horas = int(time_seconds / 3600)
minutos = int((time_seconds%3600) / 60)
segundos = int((time_seconds%3600) % 60)

print("{}:{}:{}".format(horas, minutos, segundos))
