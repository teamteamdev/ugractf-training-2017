# Find me

> `ssh game.nsychev.ru:5003, admin:admin`

## Write-up

Заходим на сервер, видим директории. Внутри директорий — другие директории.

Знаем, что в флаге есть `uctf`, поэтому запускаем `grep -R "UCTF" .` и получаем флаг.

Флаг: **uctfbashexpert**

