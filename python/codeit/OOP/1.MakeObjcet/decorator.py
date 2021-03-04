def add_print_to(original):
    def wrapper():
        print("start")
        original()
        print("end")

    return wrapper


@add_print_to
def print_hello():
    print("hello!")
    

print_hello()
