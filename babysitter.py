# Sharon Mizrahi
# babysitter.py: this program computes the total time worked 
# and the total amount earned by the babysitter



#STEP 1
hr = int(input("Enter the hourly rate in dollars: "))
st = input("Enter the start time: ")
et = input("Enter the start time: ")

#STEP 2
split_st = st.split(' ') #splitting in spaces

start_hour = int(split_st[0]) #index 0 is the time

start_period = split_st[1].upper() #index 1 is the period
#making period upper so it matches loop condition

#STEP 3
split_et = et.split(' ')

end_hour = int(split_et[0])

end_period = split_et[1].upper()

#STEP 4

if start_period == 'PM': #when period is PM add 12 to the number
    start_hour += 12    #ex. 3 PM should be 15 hours

if end_period == 'PM':
    end_hour += 12
    
#STEP 5
total_hours = end_hour - start_hour # computing hours worked
total_earnings = total_hours * hr # computing earnings

print()
print('The babysitter worked', total_hours, 'hours and earned $', total_earnings,'.')