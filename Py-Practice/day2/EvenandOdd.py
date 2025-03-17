num=int(input('Enter a random decimal number:'))
#use of ternary operator
print('{} is an even number!!'.format(num)) if num%2==0 else print('{} is an odd number!!'.format(num))#single statement
{print('{} is an even number!!'.format(num)),print('{} is an even number!!'.format(num))} if num%2==0 else print('{} is an odd number!!'.format(num))#multiple statement
