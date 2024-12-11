import sys

# print(sys.argv)

# args = sys.argv[1:]
# print(args)

# print(int(sys.argv[1])+int(sys.argv[2]))

args = sys.argv[1:]
# sum = 0

# for i in args:
#     sum += int(i)
# print(sum)

if len(sys.argv) <= 2 or len(sys.argv) > 4:
    print("오류")
else:
    if sys.argv[1] == "mul":
        print(int(sys.argv[2]) * int(sys.argv[3]))
    elif sys.argv[1] == "add":
        print(int(sys.argv[2]) + int(sys.argv[3]))
