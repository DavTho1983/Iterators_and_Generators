nums = [88, 73, 92, 72, 40, 38, 25, 20, 90, 72]

# def evens(stream):
#     them = []
#     for n in stream:
#         if n % 2 == 0:
#             them.append(x)
#         return them
#
# for n in evens(nums):
#     do_something(n)

#Generators
def hello_world():
    yield "Hello"
    yield "world"

for x in hello_world():
    print(x)

def evens(stream):
    for n in stream:
        if n % 2 == 0:
            yield n

for n in evens(nums):
    print(n + 1)
