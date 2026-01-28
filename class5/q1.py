def calculate_bill(*args, **kwargs):
    print(f"Percentage discount is {kwargs["discount"]}")
    print(f"Percentage tax is {kwargs["tax"]}")
    print("Total price is: ")
    print(f"Prices are{args}")
    print(f"Final price is: ")

    for i in args:
        print(i-((kwargs["discount"]/100)*i)+((kwargs["tax"]/100)*i))

calculate_bill(100,200,300, discount=12, tax=7)
#  key_value = kwargs.get('key', 'default_value')------check