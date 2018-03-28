import random
import re

whitespace = ' \t\n\r\v\f'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = lowercase + uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + letters + punctuation + whitespace
pattern = re.compile(r'random\([dmc]{1},\d+\)')


def generate_random_string(length=10, random_range=printable):
    return ''.join([random.choice(random_range) for x in xrange(length)])


def insert_character_random_position(character, string):
    position = random.randint(0, len(string))
    string = string[:position] + character + string[position:]
    return string


def generate_random_email_address():
    domain = random.choice(['com', 'org', 'net', 'edu', 'gov', 'mil', 'com.cn', 'cn'])
    username = generate_random_string(length=random.randint(5, 20), random_range=letters)
    corporation = generate_random_string(length=random.randint(5, 20), random_range=lowercase)
    return '{username}@{corporation}.{domain}'.format(username=username, corporation=corporation,
                                                      domain=domain)


def generate_random_phone_number():
    start = random.choice(
        ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
         '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189'])
    end = ''.join(random.sample(digits, 8))
    return start + end


def print_dict(d):
    print ''
    for key in d:
        print '%-15s:%s' % (key, d.get(key))
    return d


def convet_random(s):
    for a in re.search(pattern, s).group():
        print a
    return 's'


def convert_dict(d):
    print ''
    for key in d:
        value = d.get(key)
        if isinstance(value, str):
            if re.search(pattern, value):
                d[key] = convet_random(value)
        print '%-15s:%s' % (key, d.get(key))
    return d


if __name__ == '__main__':
    print convert_dict({
        'Password': 'random(d,999)',
        'Username': 'Admin',

    })
