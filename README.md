# Задания тренировки к Ugra CTF 2017

## Тренировочная платформа Keva
Решения почти всех тасков с training.keva.su доступны [на Гитхабе команды Ufologists](https://github.com/ufologists/ufoctf-school-2016/)

Три таска были не с UFO CTF School 2016, идеи решения у них следующие:

1. *(Stegano, 50)* Find — в папке с ресурсами находим файл background.png, в котором написан флаг азбукой Морзе
2. *(Misc, 100)* Hear — в папке со звуками появился новый файл, флаг написан на спектрограмме
3. *(Misc, 300)* Scream — декомпилируем игру (а именно один из DLL-файлов) или прогоняем его через утилиту strings (ищет utf-8 строки в бинарном файле). И тот, и другой способ помогает получить base64 от флага.

Интересно, что флаг от Scream мог быть получен в любом другом из этих трёх тасков.

## Первая тренировка от Никиты

### PPC
1. [Maze](maze/)
2. [Game](airplane/)
3. [New Maze](newmaze/)

### Admin
1. [Easy bash](bash/)

### SQL
Решения всех 10 заданий доступны [на Хабрахабре](https://habrahabr.ru/post/253885/).

### Web
1. [See inside](seeinside/)
2. [Give me flag](givemeflag/)
3. [Cooking](cooking/)
4. [Feed the pet](feedthepet/)
5. [Invisible](invisible/)
6. [Easy pass](easypass/)
7. [Humanized](humanized/)
8. [Manual](manual/)
9. [PentaHide](pentahide/)
10. [Rotalive](rotalive/)
11. [Ping](ping/)
12. [RegExp](regexp/)

## Вторая тренировка от Никиты

### Admin

1. [Find me](findme/)

### Crypto

1. [PIN](pin/)
2. [Only two](https://github.com/ugractf/upmlctf-2016/tree/master/crypto100) — с UPML CTF 2016
3. [Not so easy](https://github.com/ugractf/upmlctf-2016/tree/master/crypto150) — с UPML CTF 2016
4. [Как интересно](sudoku/)
5. Keith Bostic
6. [One more cipher](https://github.com/ugractf/upmlctf-2016/blob/master/crypto300) — с UPML CTF 2016
7. [Сложное шифрование](cxor/)
8. [FLAG](flag/)

### Joy

1. [Очень плохой таск](tethering/)

### Recon

1. [Explore world map](https://github.com/ugractf/upmlctf-2016/blob/master/joy200) — с UPML CTF 2016

### Stegano

1. [EXIF](exif/)
2. [Друг человека](https://github.com/ugractf/upmlctf-2016/blob/master/stegano150) — с UPML CTF 2016
3. [Пакет Яровой](https://github.com/ugractf/upmlctf-2016/blob/master/stegano100) — с UPML CTF 2016
4. [Logotype](logotype/)
5. [Illuminati](illuminati/)
6. [Select your way](qrs/)
7. [Beautiful sound](https://github.com/ugractf/upmlctf-2016/blob/master/stegano400) — с UPML CTF 2016

### Web

1. [Web designer](design/)
2. [One more PHP](php/)

## Команда

* Таски с UFO CTF School 2016 разработала команда [Ufologists](https://github.com/ufologists), тренировку подготовила команда [Keva](https://ctftime.org/team/2980)
* Категорию SQL сделал [Александр Берсенев](https://github.com/alexbers)
* Тренировки от Никиты сделал [Никита Сычев](https://t.me/nsychev)

## Лицензия

Материалы соревнования можно использовать для тренировок, сборов и других личных целей, но запрещено использовать на своих соревнованиях. Подробнее — [в лицензии](LICENSE)

