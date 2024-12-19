print('Enter number to check leap year')
input_number=int(input())
if(input_number%4==0 and input_number%100!=0 or input_number%400==0):
    print(input_number,'is a leap year')
else:
    print(input_number,'is not leap year')