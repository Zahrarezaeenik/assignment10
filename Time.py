class Time:
    def __init__(self,h=0,m=0,s=0):
        if h>=0:
            self.h=h
        else:
            print("Error in input of hour!")
            exit(0)

        if m in range(0,60):
            self.m=m
        else:
            print("Error in input of minute!")
            exit(0)

        if s in range(0,60):
            self.s=s
        else:
            print("Error in input of second!")
            exit(0)
        
       

    def add_times(self, time2):
        result = Time()
        result.s = self.s + time2.s
        if result.s//60 :
            result.s %= 60
            result.m += 1

        result.m += self.m + time2.m

        if result.m // 60:
            result.m %= 60
            result.h += 1

        result.h += self.h + time2.h
        return result

    def subtract_times(self, time2):
        result = Time()
        result.s=self.s-time2.s
        if result.s<0:
            result.s+=60
            result.m-=1

        result.m=self.m-time2.m+result.m

        if result.m<0:
            result.m+=60
            result.h-=1

        result.h=self.h-time2.h+result.h
        
        return result
    
    def time_to_sec(self):
        return self.h*3600 + self.m*60 + self.s
    
    def sec_to_time(self,sec):
        self.s=sec%60
        sec-=self.s
        self.h=sec//3600
        sec=sec%3600
        self.m=sec//60

    def __str__(self) -> str:
        return f"{self.h}:{self.m:02}:{self.s:02}"


def input_time(text):
    h,m,s=input(text).split(':')
    h,m,s=int(h),int(m),int(s)
    if m in range(0,60) and s in range(0,60):
        return [h,m,s]
    print("Input error! try again.")
    return input_time(text)   


def main():
    h,m,s=input_time("Enter Time 1 in format (HH:MM:SS): ")
    time1= Time(h,m,s)
    h,m,s=input_time("Enter Time 2 in format (HH:MM:SS): ")
    time2= Time(h,m,s)
    print(f"{time1.__str__()} + {time2.__str__()} = {time1.add_times(time2).__str__()}")
    print(f"{time1.__str__()} - {time2.__str__()} = {time1.subtract_times(time2).__str__()}")
    time3= Time()
    time3.sec_to_time(int(input("Enter second : ")))
    print(time3.__str__())
    print(f"{time3.__str__()} => {time3.time_to_sec()}")

if __name__ == "__main__":
    main()