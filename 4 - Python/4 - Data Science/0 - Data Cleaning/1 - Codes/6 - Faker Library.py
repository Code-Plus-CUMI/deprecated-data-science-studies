"""
2 - Faker

- Description:
	Library to generate fake datas

- Install:
	!pip install faker

- Documentation:
	https://faker.readthedocs.io/en/master/
"""

from faker import Faker
fake = Faker(['ko_KR', 'pt_BR']) # with region
fake = Faker() # without region
fake.seed(2000)

# Generating fake datas
fake.color()
fake.job()
fake.email()
fake.adress()
fake.unique.adress()
fake.name()
fake.text()