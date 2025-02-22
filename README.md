Это веб-приложение позволяет пользователю вводить название города и получать прогноз
погоды на ближайшее время: температура, вероятность осадков, влажность, скорость ветра.

## Использованные технологии

- Веб-фреймворк: Flask
- API погоды: [Open Meteo](https://open-meteo.com/)
- База данных: PostgreSQL (синхронная библиотека)
- Стиль: CSS, фирменный стиль
- Контейнеризация: Docker

## Дополнительный функционал

- Подсказки при вводе города
- Запоминание последнего просмотренного города
- Сохранение истории поиска по каждому пользователю
- API для получения статистики по количеству запросов на каждый город
- Приложение помещено в докер контейнер
- От себя добавил немного своего фирменного стиля, в котором я делаю все
графические элементы, в том числе и сайты

## Запуск приложения

1. Запуск приложения: 
   Запустите `app.py` для локальной работы.

2. Доступ к приложению с другого устройства:
   Используйте публичный адрес ngrok для доступа.

3. Получение статистики:  
   Отправьте GET-запрос на `/history`. Например: `http://127.0.0.1:5000/history`  
   Вы можете использовать Postman для выполнения запросов.


## Примечания
1) Статистика сохраняется в базе данных без использования ORM, с применением чистых SQL запросов
2) Из дополнительного функционала не сделаны лишь тесты, потому, что я не совсем понимаю
как это должно выглядеть и не вижу в них смысла