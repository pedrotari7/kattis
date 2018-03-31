import sys

for line in sys.stdin:
    month, day, year, sunrise, sunset = line.strip().split()

    sunrise_hours, sunrise_minutes = sunrise.split(':')
    sunset_hours, sunset_minutes = sunset.split(':')

    sun_minutes = int(sunset_minutes) - int(sunrise_minutes) 
    sun_hours = int(sunset_hours) - int(sunrise_hours) - (sun_minutes < 0)
    sun_minutes %= 60 
    
    print ' '.join([month, day, year, str(sun_hours), 'hours', str(sun_minutes), 'minutes'])
