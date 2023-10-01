def main():
    months =[
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
    while True:
        inp=input("DATE: ")
        month,day,year=inp.split("/")
        if 1<=int(month)<=12 and 1<=int(day)<=31:
                print(f"{int(year)}-{int(month):02}-{int(day):02}")
                break
            
                
        else:
                try:
                    omonth,oday,oyear=inp.split(" ")
                    nday=oday.replace(",","")                    
                    for i,month in enumerate(months):
                        if month.lower()==omonth.lower() and 1<=int(nday)<=31:
                            monthnum=month[i]+1
                            print(f"{int(oyear):04}-{monthnum:02}-{int(nday):02}")
                            break
                except:
                    print()
                    break
            
                        
main()