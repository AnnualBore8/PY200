import random


def fake_iphone():
    first_product_name = 'IPhone'
    number_of_product = ('13', '14', '11', '12')
    second_product_name = ('Pro', '', 'Pro Max')
    memory_capacity = ('128 Gb', '256 Gb', '512 Gb', '1 tb')

    group_iphone = "".join(first_product_name + " " + random.choice(number_of_product) + " "
                           + random.choice(second_product_name) + " " + random.choice(memory_capacity))
    return group_iphone


def fake_macbook():
    first_product_name = 'MacBook'
    number_of_product = ('Pro 13 inch', 'Pro 14 inch ', 'Pro 15 inch', 'Pro 16 inch', 'Air')
    second_product_name = ('M1 Pro', 'M1 Max', 'M2 Max', 'M2 Pro', 'M1', 'M2')
    ram_capacity = ('8 Gb', '16 Gb', '24 Gb' '32 Gb', '64 Gb')
    memory_capacity = ('256 Gb', '512 Gb', '1 tb', '2 tb', '4 tb')

    group_macbook = "".join(first_product_name + " " + random.choice(number_of_product) + " "
                            + random.choice(second_product_name) + " RAM " +
                            random.choice(ram_capacity) + " Unified Memory " + random.choice(memory_capacity))
    return group_macbook


def gen_product():
    while True:
        product = {'name': random.choice([fake_iphone(), fake_macbook()]),
                   'price': round(random.uniform(450, 3500), 2),
                   'rating': round(random.uniform(0, 10), 2)}
        yield product


if __name__ == "__main__":

    for i in range(10):
        print(next(gen_product()))
