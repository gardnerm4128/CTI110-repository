#CTI - 110
#M5T2: Bug Collector
#Matthew Gardner
#10-9-17

#7 days [Range]
#num of bugs
#todays bugs
#total bugs
def main():
    TotalBugs = 0;
    week = range(1,8)
    for day in week:
        #ask for todays bgs
        TodaysBugs = int(input("Number of today's bugs? "))
        #add tdys to total
        TotalBugs = TotalBugs + TodaysBugs
    print("total number of bugs ", TotalBugs)
#strt prgrm
main()
