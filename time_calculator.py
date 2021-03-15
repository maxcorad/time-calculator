def add_time(start, duration, dow=""):
    # get hours, minutes and daytime from start and duration
    start_time, daytime = start.split()
    start_hour, start_min = start_time.split(":")
    dur_hour, dur_min = duration.split(":")
    # calculate finish time
    finish_hour = int(start_hour) + int(dur_hour)
    finish_min = int(start_min) + int(dur_min)
    # adjust for finish times of 60 minutes or longer
    if finish_min > 59:
        finish_min -= 60    # substract 60 minutes
        finish_hour += 1    # add 1 hour
    # format minutes as 'mm'
    finish_min = f"0{finish_min}" if finish_min < 10 else finish_min
    # adjust for finish times of 12 hours or longer
    if finish_hour < 12:
        days_later = 0
    else:
        half_days = finish_hour // 12
        days_later = finish_hour // 24
        finish_hour %= 12
        # switch from AM to PM and viceversa when appropriate
        if (half_days % 2 == 1) & (int(start_hour) != 12):
            daytime = "AM" if daytime == "PM" else "PM"
            days_later += 1 if daytime == "AM" else 0
        # make sure hours range from 1 to 12
        finish_hour = 12 if finish_hour == 0 else finish_hour
    # format finish time
    finish_time = f"{finish_hour}:{finish_min}"
    # calculate day of the week when required
    if dow != "":
        days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
        "Saturday", "Sunday"
        ]
        # transform input dow to numeral
        dow = days.index(dow.lower().capitalize())
        # calculate output dow, format to ', Day'
        dow += days_later
        dow = ", " + days[dow % 7]
    # format output to deal with times in future days when needed
    if days_later == 0:
        days_later = ""
    elif days_later == 1:
        days_later = " (next day)"
    else:
        days_later = f" ({days_later} days later)"
    # format output to 'time period [day of week] [num days later]'
    new_time = f"{finish_time} {daytime}{dow}{days_later}"    
    return new_time
