from perceptron import Perceptron
from random import choice


def get_label(sample):
        if (sample['unhappy'] or sample['left']) \
           and not (sample['is_associate'] or sample['is_edu']):
            return 1
        return -1


def gen_train_base(size=5000, add_label=True):

    samples = []
    for i in range(size):

        left = choice([-1, 1])
        unhappy = choice([-1, 1])
        is_edu = choice([-1, 1])
        is_associate = choice([-1, 1])

        current = {
            'left': left,
            'unhappy': unhappy,
            'is_edu': is_edu,
            'is_associate': is_associate,
            'raw': [left, unhappy, is_edu, is_associate]
        }

        if add_label:
            current['label'] = get_label(current)
        samples.append(current)

    return samples


def run(data=None):

    def get_input():

        name = input('Name: ')
        left = input('has left? ')
        unhappy = input('is unhappy? ')
        is_edu = input('is edu? ')
        is_associate = input('is associate? ')

        return {
            'left': left,
            'unhappy': unhappy,
            'is_edu': is_edu,
            'is_associate': is_associate,
            'raw': [left, unhappy, is_edu, is_associate]
        }, name

    if not data:
        data, name = get_input()
    else:
        name = data['name']

    if not data.get('raw'):
        data['raw'] = [
            data['left'], data['unhappy'], 
            data['is_edu'], data['is_associate']
        ]

    p = Perceptron()
    train = gen_train_base()
    for sample in train:
        p.train(sample['raw'], sample['label'])

    prediction = p.guess(data['raw'])
    test = get_label(data)
    guessed_right = prediction == test
    print('\nRaw prediction:', prediction)
    print('Defined label:', test)
    print('{} is {} to join to Assembléia\n'.format(
        name, 'able' if prediction == 1 else 'not able'
    ))

    return guessed_right


test = {
    'name': '*****',
    'unhappy': 1,
    'is_edu': -1,
    'is_associate': -1,
    'left': -1
}

everyone = [
    {
        'name': '*****',
        'left': False,
        'unhappy': False,
        'is_edu': False,
        'is_associate': True
    },
    {
        'name': '*****',
        'left': True,
        'unhappy': False,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': False,
        'unhappy': True,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': True,
        'unhappy': False,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': False,
        'unhappy': False,
        'is_edu': False,
        'is_associate': True
    },
    {
        'name': '*****',
        'left': True,
        'unhappy': True,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': True,
        'unhappy': False,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': False,
        'unhappy': False,
        'is_edu': False,
        'is_associate': True
    },
    {
        'name': '*****',
        'left': True,
        'unhappy': True,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': False,
        'unhappy': True,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': False,
        'unhappy': True,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': True,
        'unhappy': False,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': False,
        'unhappy': True,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': True,
        'unhappy': False,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': False,
        'unhappy': True,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': False,
        'unhappy': True,
        'is_edu': False,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': True,
        'unhappy': True,
        'is_edu': True,
        'is_associate': False
    },
    {
        'name': '*****',
        'left': False,
        'unhappy': True,
        'is_edu': True,
        'is_associate': False
    }
]

run(test)
ok = 0
failed = 0

for person in everyone:
    if run(person):
        ok += 1
    else:
        failed += 1

print('Finished running')
print('Score: OK [{}], FAILED [{}]'.format(ok, failed))
