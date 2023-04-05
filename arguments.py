def year_of_birth(name, age):
    year =2023 -age
    print(f"Hello {name}, you were born in {year}")


def my_country(country = "Kenya"):
    print(f"Hello you are from {country}")

def hello(*names):
    for name in names:
        print (f"Hello {name}")

def sum (*nums):
    answer = 0
    for num in nums:
        answer += num
    return answer

def multiply_many (**kwargs):
    answer =1
    for num in kwargs.values( ):
        answer*= num


    return answer


# A function named concatenate_args that takes any number of string arguments 
# in positional arguments format 
# and concatenates them into a single string

def concatenate_args (*names):
    str = ''
    for name in names:
        str  += name
    return str

# A function named concatenate_kwargs that takes any number of string arguments 
# in keyword arguments  format and concatenates them into a single string
def concatenate_aargs (**kwargs):
    str = ''
    for kwarg in kwargs.values():
        str  += kwarg
    return str




