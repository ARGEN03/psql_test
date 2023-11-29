\c - подключение к бд

\l - показывает весь список бд

\du - показывает всех пользователей

\dt - показвает все таблицы внутри бд

\d <название таблицы> -  более подробная инфо-я о таблице

\q - выход из СУБД(quit) 

# ВСЕ КЛЮЧЕВЫЕ СЛОВА ДОЛЖНЫ ПИСАТЬ С БОЛЬШОЙ БУКВЫ

## sudo -u postgres psql - команда для захода через юзера  postgres



# ТИПЫ ДАННЫХ
## int:
    bigint - 8 байтовое число
    integer - 4 байтове число
    smallint - 2 байтове число
    serial - авто инкрементация

## str:
    char(число) - фиксированная длина ___H/W___
    varchar(число) - фиксированная длина ___H/W___
    text - без ограничений, длиная  строка

## date:
    date - дата и время
    time - время
    timestamp - дата


## boolean - true|false


CREATE USER <username> WITH PASSWORD 'password;

ALTER ROLE <username> <привелегии>;

CREATE DATABASE <username> WITH OWNER <usename>;



### NOT NULL = не должно быть пустым
### NULL 
### PRIMERY KEY
### FORIEGN KEY
### UNIQUE
### CHECK


# Создание базы данных

     DATABASE <название бд>;

# Удаление базы данных

    ATABASE <название бд>;

# Создание таблицы

    CREATE TABLE <название таблицы> (
        column {varchar}-тип  NOT NULL
);

# Удаление таблицы

    DROP TABLE <название таблицы>;


# Заполнeние таблицы

    insert into <название таблицы> (<столбец-1б>,<столбец-2>) values(<значение-1>,<значение-2>)

    insert into product (name,price) values ('Iphone 14', 24000);

    insert into product (name,price) values ('Iphone 14', 25600),('macbook',34000), ('Iphone 5', 45000);

    insert into product (name) values ('delete');

# Сорторовка таблицы 

    select * from product {ORDER BY} price; - по возрастанию 

    select * from product ORDER BY price {DESC}; - по убыванию

# Вывод данных из таблицы
 
    select * from <название таблицы>

    select * from product ORDER BY price {limit 2}; - выводит по лимиту (в данном случаи он выдаст только 2 строки)

    select * from product ORDER BY id;


# LIMIT - возвращает ограниченное кол-во данных

    select * from product ORDER BY price {limit 5};

    select * from product order by price offset 3; проспускает первые 3 записей

# DICTINCT - убирает дубликаты, возвращает уникальные значения 

    select distinct price from product; 

# WHERE - УСЛОВИЕ - это фильтрация по каким-то критериям
    <!-- <,>, >=, <=, = ,!= --> 

## операторы
or 
and 
not 
in  

    select * from product where name = 'Iphone 14';

    select * from product where price >= 20000 and price <= 300000;

    select * from product where (24000, 300000);

# BETWEEN - ДИАПОЗОН

# LIKE - ВЫВОДИТ РЕЗУЛЬТАТ КОТОРЫЙ ПОДХОДИТ ВВЕДНЕННОМУ ШАБЛОНУ(ЧУВСТВИТЕЛЕН К РЕГИСТРУ)

# iLIKE - НЕ ЧУВСТВИТЕЛЕНCREATE К РЕГИСТРУ

    where name like A% - имена нач. на А

    like '%@gmail.com'

# delete 
    delete from <название таблицы>

регекст - 

# update

    UPDATE product set name = <новое значение>;

    UPDATE product set name = <новое значение> where id = 3;

# Оператор AS ALIAS

elect name, price * 89 as dollars from product;

    name     | dollars  
    --------------+----------
    Iphone 14    |  2136000
    macbook      | 26700000
    Iphone 14    |  2278400
    macbook      |  3026000
    Iphone 5     |  4005000
    Redmi note 9 |  1335000
    (6 rows)

# GROUP BY -  это ключевое слово, которое позволяет выводить значение из колононок обьеденные в группы


    select * from product;
    id |     name     | price  
    ----+--------------+--------
    1 | Iphone 14    |  24000
    3 | macbook      | 300000
    5 | Iphone 14    |  25600
    6 | macbook      |  34000
    7 | Iphone 5     |  45000
    2 | Redmi note 9 |  15000
    8 | Nokia 5      | 230000
    (7 rows)



select name, sum(price) from product group by name;

        name     |  sum   
    --------------+--------
    Iphone 5     |  45000
    Redmi note 9 |  15000
    Nokia 5      | 230000
    Iphone 14    |  49600
    macbook      | 334000
    (5 rows)

# HAVING - точно такое же условие как WHERE но всегда используется с GOURP BY, выводить рез. условия  группю

# WHERE - выводит рез. условия для строк.

    select name, sum(price) from product where price < 15000 group by name having name = 'Iphone 14';

# СВЯЗИ 

## one to one 
    один чел - один мозг
    один ключ - один замок

## one to many 
    один книга - много страниц
    один куратор - много студентов


## many to many
    много аккунтов - много репозиториии
    много учеников - много предметов

### PRIMARY KEY - внешний ключ (с помощью него создаются связи) 

### FOREIGN KEY - первичный ключ (ссыляется на PRIMARY KEY)

### one to one  - к id другой таблицы даем уникальность 

### one to many - просто ссылаяемся на id другой таблицы

### many to many - создаем третью таблицн, в которой ссылаемя на две связные таблицы


# INDEXES - это спец. объекты предназначенные в основном для ускорения доступа к данных

## Типы индексов в postgres:
### 1) b-дерево - balanced tree
### 2) хеш
### 3) gist 
### 4) sp-gist
### 5) gin
### 6) brin

<!-- сreate index book_title on book (title); -->

# JOIN -  инструкция, которая позволяет в запросах select брать данные из нескольких таблиц

## ВИДЫ JOIN:

### INNER JOIN (JOIN):

    Достает только те записи у которых есть связ

### LEFT JOIN:

    Достает все записи с левой таблицы и соединает с правой таблицей

### RIGTH JOIN:

    Достает все записи с правиой таблицы и соединает с левой таблицей

### FULL JOIN:

    Достает все записи с обеих таблиц

### SELF JOIN:

    



