# Web designer

*Таск взят с [FHQ](https://freehackquest.com/)*

## Write-up

Дан HTML-файл с очень большой таблицей стилей.

Замечаем, что большая часть CSS-кода дублируется — при этом `position: relative;` меняется на `position: absolute`. 

Удаляем повторяющиеся объявления, и видим флаг, нарисованный CSS-псевдографикой.

Флаг: **fhq(ilovectf)**

