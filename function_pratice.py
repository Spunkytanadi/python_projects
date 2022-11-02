def hello():
    print("Hello User!")

def pack(a,b,c):
    print[a,b,c]

def eat_lunch(my_lst):
    if len(my_lst) == 0:
        print("My lunch is coffee!")
    else:
        for i in range(len(my_lst)):
            if i == 0:
                print(f"First I eat{my_lst[0]}")
            else:
                print(f"Next I eat{my_lst[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwhich"])
eat_lunch(["apple","banana","sandwhich","cookie"])
