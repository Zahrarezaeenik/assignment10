class Date:
    def __init__(self,year=1,month=1,day=1):
        self.year=year
        self.month=month
        self.day=day
        if not self.IsValidDate():
            print("Date in not valid!")
            exit(0)

    def IsValidDate(self):
        valid_Day=30
        valid_month=12
        valid_year=9999
        if self.year not in range(1,valid_year+1):
            return False
        if self.month not in range(1,valid_month+1):
            return False
        if self.day not in range(1,valid_Day+1):
            return False
        return True
    
    def Show(self):
        print(f"{self.year}/{self.month}/{self.day}",end="")

    def add(self,date2):
        date_result=Date()
        date_result.day=self.day+date2.day
        temp=0
        if date_result.day>30:
            temp=1
            date_result.day%=31
            date_result.day+=1

        date_result.month=self.month+date2.month+temp
        temp=0
        if date_result.month>12:
            temp=1
            date_result.month%=13
            date_result.month+=1
        date_result.year=self.year+date2.year+temp

        if date_result.year>9999:
            print("Can not add this times! (year > 9999)")
            return None
        return date_result

def main():
    print("Date 1")
    y=int(input("Enter year: "))
    m=int(input("Enter month: "))
    d=int(input("Enter day: "))
    date1=Date(y,m,d)

    print("Date 2")
    y=int(input("Enter year: "))
    m=int(input("Enter month: "))
    d=int(input("Enter day: "))
    date2=Date(y,m,d)
    date1.Show()
    print(" + ",end='')
    date2.Show()
    print(" = ",end='')
    date1.add(date2).Show()



if __name__ == "__main__":
    main() 


