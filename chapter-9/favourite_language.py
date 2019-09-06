# colllections是python的官方module，OrderedDict是带排列顺序的字典

from collections import OrderedDict

from random import randint

favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")


x = randint(1, 6)

print(x)