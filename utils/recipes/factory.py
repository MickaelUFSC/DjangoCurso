# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_speed():
    sp = randint(0, 10)
    speed_indicator = ''
    if (sp >= 7):
        speed_indicator = 'High'
    elif (sp >= 4 and sp < 7):
        speed_indicator = 'Medium'
    else:
        speed_indicator = 'Low'

    return speed_indicator


def make_recipe():
    return {
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'types': fake.word(),
        'preparation_time_unit': 'Minutos',
        'speed': make_speed(),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/terror, medo' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
