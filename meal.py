def main():
    check=input("Time: ")
    if 7<=convert(check)<=8:
        print("breakfast")
    elif 12<=convert(check)<=13:
        print("lunch")
    elif 18<=convert(check)<=19:
        print("Dinner")
def convert(time):
    hour,minute=time.split(":")
    hour,minute=float(hour),float(minute)
    min=minute/60
    return hour+min
main()