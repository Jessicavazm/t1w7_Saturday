def personal_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}--->{value}")

personal_details(name="Jess", age="30", address="Melbourne")

## Example using *args and **kwargs

def my_function(*onestar, **twostars):
    print("args:", onestar)
    print("kwargs:", twostars)

my_function("I", "Love", "Coding", first = "I", second = "Love", third = "Coding")