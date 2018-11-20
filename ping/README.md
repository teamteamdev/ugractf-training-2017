# Ping

## Write-up

Дан сайт, который умеет пинговать по IP. Вывод очень похож на вывод линуксовой команды ping с аргументом `-c 4`.

Делаем предположение, что именно она там и используется. Однако, это нам не помогает — ничего, кроме IP, в поле ввести не получается: он валидируется.

Однако, валидация происходит только на клиенте. Попробуем в обход страницы отправить POST-запрос, например, с доменом:

```
POST /ping/ HTTP/1.1
Host: ctf.upml.tech

ip=google.com
```

В ответ получаем вывод команды `ping`! Значит, на сервере нет никакой валидации.

Пробуем сделать RCE: `ip=google.com; ls`. Видим список файлов в директории, в их числе — `flag.txt`.

Наконец, делаем `ip=google.com; cat flag.txt` и получаем флаг.

Флаг: **uctfdonotgiveconsoleaccesstoanyone**
