# Cooking

## Write-up

Название таска намекает на cookie-файлы. Если мы откроем сайт, то увидим отсутствие доступа к Pentagon cafe. Посмотрев в заголовки, увидим появление куки: `is_staff=fcbcf165908dd18a9e49f7ff27810176db8e9f63b4352213741664245224f8aa`. Похоже на хеш.

Заходим на crackstation.net, вводим хеш, видим, что это `sha256(false)`. Меняем на `sha256(true) = b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b`, получаем флаг.

Флаг: **uctf_tastysha256**

