# Invisible

## Write-up

Видим обычную пустую страницу. Казалось бы, ничего непонятно, но в коде обнаруживаем картинку, которой на странице вроде бы нет:

```html
<img src="static/background.png" />
```

Или есть? [Скачиваем её](html/static/background.png), открываем в [StegSolve](http://www.caesum.com/handbook/Stegsolve.jar), в нулевом канале видим флаг.

Флаг: **uctf_very_visible**

