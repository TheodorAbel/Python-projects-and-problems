def main():
    time=input("what time is it? ").strip()
    meal_time=convert(time)
    if 7.0<=meal_time<=8.0:
        print("breakfast time")
    elif 12.0<=meal_time<=13.0:
        print("lunch time")
    elif 18.0<=meal_time<=19.0:
        print("dinner time")
    else:
        print(None)





def convert(time):
    hour,minute=time.split(":")
    hour=int(hour)
    minute=int(minute)
    minute=(minute*100)/6000.0
    time_in_hour=hour+minute
    return  time_in_hour



if __name__ == "__main__":
    main()




