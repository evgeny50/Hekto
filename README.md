<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
<h1>Online shop Hekto</h1>
  <div><p>Установка (для пользователей операционных систем семейства MacOs/Linux):</p>
<p>Открыть терминал или консоль и перейти в нужную Вам директорию<br>
Прописать команду<br>
<pre><code>git clone https://github.com/evgeny50/Hekto.git</code></pre></p>
<p>Перейти в директорию Hekto</p>
<pre><code>cd Hekto
</code></pre>
<p>Прописать следующие команды:</p>
<pre><code>python3 -m venv env
</code></pre>
<p>Активировать виртуальное окружение</p>
<pre><code>source env/bin/activate
</code></pre>
<p>Установить необходимые библиотеки</p>
<pre><code>pip install -r requirements.txt
</code></pre>
<p>Создать файл .env в нем указать ключи от Braintree. Например:</p>
<pre><code>Merchant_ID=123
</code></pre>
<pre><code>Public_Key=123
</code></pre>
<pre><code>Private_Key=123
</code></pre>
<p>Создать и выполнить миграции</p>
<pre><code>python manage.py makemigrations
</code></pre>
<pre><code>python manage.py migrate
</code></pre>
<p>Установить и запустить RabbitMQ командой</p>
<pre><code>rabbitmq-server
</code></pre>
<p>Запустить Celery</p>
<pre><code>celery -A Hekto worker -l info
</code></pre>
<p>Запустить Flower</p>
<pre><code>celery -A Hekto flower
</code></pre>
<p>Запустить сервер</p>
<pre><code>python manage.py runserver
</code></pre>
</div>
</body>

</html>
