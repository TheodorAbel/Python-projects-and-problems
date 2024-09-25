import re
def main():
    print(convert(time := input("time: ")))


def convert(s):
    pattern = r"(?P<time1>[1-9]|1[0-2]):?(?P<minute1>[0-5][0-9])? (?P<format1>AM|PM) to (?P<time2>[1-9]|1[0-2]):?(?P<minute2>[0-5][0-9])? (?P<format2>AM|PM)"
    match = re.search(pattern, s)

    if not match:
        print(f"Pattern did not match for input: {s}")  # Debug print
        raise ValueError("ValueError")

    time1 = int(match.group("time1"))
    minute1 = match.group("minute1") or "00"
    format1 = match.group("format1")

    time2 = int(match.group("time2"))
    minute2 = match.group("minute2") or "00"
    format2 = match.group("format2")

    if int(minute1) > 59 or int(minute2) > 59:
        print(f"Invalid minutes detected: {minute1}, {minute2}")  # Debug print
        raise ValueError("ValueError")
    if time1 < 1 or time1 > 12 or time2 < 1 or time2 > 12:
        print(f"Invalid hours detected: {time1}, {time2}")  # Debug print
        raise ValueError("ValueError")

    time1_24 = convert_to_24_hour(time1, minute1, format1)
    time2_24 = convert_to_24_hour(time2, minute2, format2)

    return f"{time1_24} to {time2_24}"

def convert_to_24_hour(hour, minute, period):
    if period == "AM":
        if hour == 12:
            return f"00:{minute}"
        return f"{hour:02}:{minute}"
    else:  # PM
        if hour == 12:
            return f"12:{minute}"
        return f"{hour + 12:02}:{minute}"
if __name__=="__main__":
    main()
