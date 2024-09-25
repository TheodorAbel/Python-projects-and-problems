months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
month_map={}

for index,month in enumerate(months,start=1):
    month_map[index]=month

def convert_to_iso(date):
    #handles date in MM-DD-YYYY format
    if '/' in date:
        parts=date.split('/')
        if len(parts)==3:
            month,day,year=parts
            try:
                if 1<=int(month)<=12 and 1<=int(day)<=31 and len(year)==4:
                    month=f"{int(month):02}"
                    day=f"{int(day):02}"
                    if year.isdigit():
                        return f"{year}-{month}-{day}"

            except ValueError:
                pass
    #handles date in Month Day,Year format
    elif ',' in date:
        parts=date.replace(',','').split()
        if len(parts)==3:
            month_name,day,year=parts
            month=None
            for index,value in month_map.items():
                if month_name in value:
                    month=f"{int(index):02}"
                    break
            try:
                if month is not None and 1<=int(day)<=31 and year.isdigit() and len(year)==4:
                    day=f"{int(day):02}"
                    return f'{year}-{month}-{day}'
            except ValueError:
                return None

    return None



def main():
    while True:
        date=input("Date: ").strip().capitalize()
        converted_date=convert_to_iso(date)
        if converted_date:
            print(converted_date)
            break



if __name__ == "__main__":
    main()
