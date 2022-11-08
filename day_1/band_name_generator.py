from faker import Faker

fake = Faker()
pet_name = fake.first_name()
band_name = f'{fake.city()} {pet_name}'
print(band_name)