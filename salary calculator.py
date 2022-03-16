
hour = int(input("Enter the amount of hours you work "))
rate = int(input("Enter your rate of pay "))
pay = hour * rate
spay = str(pay)

if hour > 40:
    otr = (hour - 40) * (rate * 1.5)
    otp = otr + (40 * rate)
    print("You worked over 40 hours, Your Overtime pay is " + str(otp))
else:
    print("You worked a regular pay of $" + spay)

input("Press key to close")

d


