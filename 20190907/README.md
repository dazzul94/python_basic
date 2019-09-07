# 2019-09-07

### - maria db 설치
https://downloads.mariadb.org  > mariadb-10.4.7-winx64.msi  
root/root 꼭 설정, UTF-8 꼭 설정, 포트번호:3309 / mysql이 3306쓰고있어서

### - 데이터베이스 SQL (에스큐엘, 시퀄)
1. 오라클사의 Oracle
2. 마이크로소프트사의 MSSQL
3. MySQL => MariaDB => MongoDB

### - 디비종류
1. RDBMS : 설치형 데이터베이스
2. NoSQL : 설치안하는 내장형 데이터베이스

### - 파이썬에는 sqlite3가 내장되어있다. -> 인스타그램과 페이스북

### - cmd에서 mariadb 설정 
~~~
    mysql -u root -p
~~~

### - employees.sql 불러오기 
~~~
    source employees.sql
    SHOW DATABASES;
    use employees
    SHOW TABLES;
~~~

### - sample.dump 불러오기
~~~
    mysql -u root-p < sample.dump
~~~



