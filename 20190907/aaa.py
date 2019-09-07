def print_args(argc, * argv):
    for i in range(argc) :
        print(argc[i])

print_args(3, "argc1", "argc2", "argv3")