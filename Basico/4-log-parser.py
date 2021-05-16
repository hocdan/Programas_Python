"""

Log Parser (logparse.py)

Accepts a filename on the command line. The file is a Linux-like log file from a
system you are debugging. Mixed in among the various statements are messages
indicating the state of the device. They look like this:

    Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON

The device state message has many possible values, but this program cares about
only three: ON, OFF, and ERR.

Your program will parse the given log file and print out a report giving how
long the device was ON and the timestamp of any ERR conditions.

Note that the provided skeleton code doesn’t include unit tests. This was
omitted since the exact format of the report is up to you. Think about and
write your own during the process.

A test.log file is included, which provides you with an example. The solution
you’ll examine produces the following output:

$ ./logparse.py test.log
Device was on for 7 seconds
Timestamps of error events:
   Jul 11 16:11:54:661
   Jul 11 16:11:56:067

"""

def log_parser(log):
    
