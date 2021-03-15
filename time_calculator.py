def add_time(start, duration, dow=""):
    # get hours, minutes and daytime from start and duration
    start_time, daytime = start.split()
    start_hour, start_min = [int(i) for i in start_time.split(":")]
    dur_hour, dur_min = [int(i) for i in duration.split(":")]

    # calculate hours in 24 hour clock
    start_hour_24 = 0 if start_hour == 12 else start_hour
    start_hour_24 += 12 if daytime == "PM" else 0
    # calculate times in minutes
    start_time_mins = 60 * start_hour_24 + start_min
    duration_mins = 60 * dur_hour + dur_min
    
    # calculate finish time in hours and minutes
    finish_time_mins = start_time_mins + duration_mins
    finish_hour = (finish_time_mins // 60)
    finish_min = finish_time_mins % 60
    
    # format finish time as '[h]h:mm AM|PM'
    finish_hour_12 = finish_hour % 12
    # make sure hours range from 1 to 12
    finish_hour_12 = 12 if finish_hour_12 == 0 else finish_hour_12    
    finish_min = f"0{finish_min}" if finish_min < 10 else finish_min
    finish_time = f"{finish_hour_12}:{finish_min}"

    # calculate finish daytime period
    finish_hour_24 = finish_hour % 24    
    daytime = "AM" if finish_hour_24 < 12 else "PM"

    # format output to deal with times in future days when needed
    days_later = finish_hour // 24
    if days_later == 0: days_later = ""
    elif days_later == 1: days_later = " (next day)"
    else: days_later = f" ({days_later} days later)"
    
    # calculate day of the week when required
    if dow != "":
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday", "Sunday"]
        # transform input dow to numeral
        dow = days.index(dow.lower().capitalize())
        # calculate output dow, format to ', Day'
        dow += days_later
        dow = ", " + days[dow % 7]

    # format output to 'time period [day of week] [num days later]'
    new_time = f"{finish_time} {daytime}{dow}{days_later}"    
    
    return new_time
