# input() => funktsiyasi foydalanuvchidan ma`lumot olish uchun ishlatiladi. 

# ikki sonni yig`indisini topish input() funktsiya orqali

# son1 = input('Son 1ni kiriting\n')
# son2 = input('Son 2ni kiriting\n')
# natija = 'natija:' +' '+ str(int(son1) + int(son2))
# print(natija)

# yoshni aniqlab beradigan dastur

from datetime import datetime

t_yil = int(input('Tug`ulgan yilingizni kiriting: '))

guess_age = 'Siznig yoshingiz:' + ' ' + str(datetime.now().year - t_yil) + ' ' + 'da'

print(guess_age)