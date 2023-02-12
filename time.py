seconds = input("Please  enter seconds as integer number:")
        while (not seconds.isnumeric() ):
           seconds = input("Enter a number:")

           seconds = int(seconds)
           seconds_in_hour = 3600
           seconds_in_minute = 60

           # Calculare hours and leftover seconds
           hours = seconds // seconds_in_hour
           seconds = seconds % seconds_in_hour

           # Calculare minutes and leftover seconds
           minutes = seconds // seconds_in_minute
           seconds = seconds % seconds_in_minute

           print ("%d hours, %d minutes, %d seconds \n" % (hours, minutes, seconds))

