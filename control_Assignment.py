# Write a function that uses while, if and continue statements to 
# print all the even numbers between 0 and 50. 
def while_if_continue():
    x = 0
    while x <= 50:
        x+=1
        if x % 2 !=0:
            continue
        print(x)


# Write a function that takes an integer argument 
# and prints "Prime" if the number is prime, 
# and "Not prime" if the number is not prime.
def prime ():
       interger1 = 10
       interger2 = 30
       for interger in range(interger1, interger2+1):
            if interger ==1:
                     print(interger, "is not prime ")
            elif interger>1:
                for i in range(2, interger):
                    if (interger% i)==0:
                          print (interger, "Is not prime") 
                          break
                else:
                    print(interger, "Is prime") 
       else:
             print(interger,"Is not prime")
                            


# Write a function that takes a list of integers as input 
# and prints the sum of all the even numbers in the list.
def sum_even():
     interger = 20
     sum = 0
     for i in range(1, interger+1):
          if i % 2 == 0:
               sum = sum +i
               print(sum)

# Write a function that takes any two integers as input, 
# and prints the sum of all the numbers 
# between the two integers (inclusive) that are divisible by 3.
def divisible_by_3(int1,int2):
     sum = 0
     for i in range(int1, int2+1):
          if i % 3 == 0:
               sum = sum + i
               print(sum)