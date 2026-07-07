# funtion to calculate simple interest
def calculate_simple_interest(principal,rate,time):
    return(principal*rate*time)/100
#-----____------------------------------____-------------------------------------------------
# main program
pricipal = float(input("enter principle(in RS)"))
rate = float(input("enter rate(in %)"))
time = int(input("enter principle(in year):"))
print("simple interest :RS",calculate_simple_interest(pricipal,rate,time))