import random

def generate_string(firstname):
    firstname_backwards = firstname[::-1]
    random_integer = random.randint(1, 1000000000)
    generated_string = f"{firstname}_{firstname_backwards}_{random_integer}"
    return generated_string

firstname = "susan"
result = generate_string(firstname)
print(result)
