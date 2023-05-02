# write a function that checks is a word is a palidrom
# returns true if is and false if it is not
# ex of palidrom words: noon, madam, civic, radar
# def min_and_max(numbers):
#     sort_list=[]
    # highest = 0
    # for num in numbers:
    #     if num > highest:
    #         highest = num
    #         sort_list.append(num)
    #         smallest =sort_list[0]
    #         largest = sort_list[-1]
    #         print(smallest)
    #         print(largest)
    #         min_and_max (numbers)

# def maximum_and_minumum(nums):
#     num = nums(max)
#     num2 =nums(min)
#     print(num)
#     print(num2)

# # nums=[2,8,3,1,6,4]
# maximum_and_minumum(nums)
# nums=[2,8,3,1,6,4]

# write a python function that inputs a list of integers and outputs the odd numbers doubled
def my_list(numbers):
    empty_list = []
    for num in numbers:
        if num%2 !=0:
            double = num*2
                
        
            empty_list.append(double)
        # i+=1
    return(empty_list)
print(my_list([1, 5, 4, 2]))


# returning duplicates
def removeduplicates(numbers):
    x = []
    for i in numbers:
        if i not in x:
            x.append(i)  
    return x  
# numbers = [2, 4, 2, 3, 3, 2, 4, 5, 3] 
print(removeduplicates([2, 4, 2, 3, 3, 2, 4, 5, 3]))

# a function that prints all the numbers between 1 and 10
def digits():
   num = 1
   while num<10:      
       num+=1
       print(num)
digits()
    
              

