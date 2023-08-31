# yoshni aniqlab beradigan dastur

from datetime import datetime

t_yil = int(input('Tug`ulgan yilingizni kiriting: '))

guess_age = f'Siznig yoshingiz: {str(datetime.now().year - t_yil)} da'

print(guess_age)