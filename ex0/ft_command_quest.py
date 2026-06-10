import sys


print("=== Command Quest ===")
print("Program name:", sys.argv[0])
if len(sys.argv) < 2:
    print("No arguments provided!")
else:
    print("Arguments recieved:", len(sys.argv) - 1)
    i = 1
    for arg in sys.argv[1:]:
        print(f"Argument {i}:", arg)
        i += 1
print("Total arguments:", len(sys.argv))
print()
