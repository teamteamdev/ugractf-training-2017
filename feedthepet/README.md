# Feed the pet

## Write-up

Данный сайт предлагает покормить обезьяну.

На выбор нам дают огурец, две картофелины и упаковку вискаса. Удивительно, но обезьяна не хочет есть ничего из предложенных вариантов.

Посмотрим, как происходит кормление:

```html
<label for="food">Food kind:</label>
<select id="food">
    <option disabled selected value="">Select one option</option>
    <option value="a cucumber">Cucumber</option>
    <option value="two potatoes">Potato (2)</option>
    <option value="a whiskas">Whiskas Pack</option>
</select>
```

```js
$.get('/feedthepet/api/monkey/', {
    "food": data
}, function(response) {
    $('#response').text(response);
});
```

Попробуем заменить одну из опций на `a banana` и посмотреть, что будет:

```html
    <option value="a banana">Banana</option>
```

Уже что-то новое:

> It's very few for me, I'm big monkey.

Увеличиваем число бананов, при пяти получаем флаг:

```html
    <option value="5 bananas">5 bananas</options>
```

Флаг: **uctfhungryanimalsknowflags**

