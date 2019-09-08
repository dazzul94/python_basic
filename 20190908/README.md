# 20190908

### - 도커 다운로드(가상화 프로그램)
window 10 pro 이상 -> 
https://docs.docker.com/toolbox/toolbox_install_windows/  
window 10 pro 미만 ->   
https://github.com/docker/toolbox/releases  
DockerToolbox-19.03.1.exe 다운로드

### - SQL 명령어
1. 데이터 정의어(DDL: Data Definition Langauge)
    * CAD
        + CREATE (생성)
        + ALTER (수정)
        + DROP (삭제)

2. 데이터 처리어(DML: Data Manipulation Language)
    * INSERT (하나 이상의 데이터 추가)
    * UPDATE (저장된 하나 이상의 데이터 수정)
    * DELETE (데이터 삭제)
    * SELECT (저장된 데이터 조회)

3. 데이터 제어어(DCL: Data Control Language)
    * GRANT (권한 설정)
    * BEGIN (트랜잭션 시작)
    * COMMIT (적용)
    * ROLLBACK (실행취소)

### - 설정
~~~
SHOW VARIABLES LIKE 'C%';
~~~

### - 사용자 계정 생성하기 
* user1(localhost), user2(%), user3(localhost), user4(%)

* 데이터베이스 서버에 접속할 수 있는 지역 설정  
    + localhost: 해당 컴퓨터에서만 접속이 가능(외부 접속 불가)
    + % : 네트워크 데이터베이스 서버로 원격 접속 허용
~~~
Mariadb> CREATE USER '계정'@'localhost' IDENTIFIED BY '암호';

Mariadb> CREATE USER 'user1'@'localhost' IDENTIFIED BY 'user1';
Mariadb> CREATE USER 'user2'@'%' IDENTIFIED BY 'user2';
Mariadb> CREATE USER 'user3'@'localhost' IDENTIFIED BY 'user3';
Mariadb> CREATE USER 'user4'@'%' IDENTIFIED BY 'user4';

Mariadb> DROP USER 'user4'@'%';

Mariadb> SELECT HOST, USER, PASSWORD FROM MYSQL.USER WHERE USER='user1'
~~~

### - 만들어진 사용자 계정에 권한주기
~~~
Mariadb> GRANT ALL PRIVILEGES ON sample.* to 'user1'@'localhost' IDENTIFIED BY 'user1';
Mariadb> GRANT ALL PRIVILEGES ON sample.* to 'user3'@'localhost' IDENTIFIED BY 'user3';

Mariadb> GRANT ALL PRIVILEGES ON employees.* to 'user2'@'localhost' IDENTIFIED BY 'user2';
Mariadb> GRANT ALL PRIVILEGES ON employees.* to 'user4'@'localhost' IDENTIFIED BY 'user4';
~~~

### - 클라이언트 프로그램으로 database 만들기
~~~
cmd> mysqladmin.exe -u root -p create white
cmd> mysqladmin.exe -u root -p drop white
~~~

### - 테이블생성, 테이블삭제
~~~
Mariadb> CREATE DATABASE shopdb;
Mariadb> DROP DATABASE shopdb;

Mariadb> use shopdb;
Mariadb> SHOW TABLES;
~~~

## - 쇼핑몰 DB
* 고객ID : 중복X
* 고객이름
* 고객전화
* 고객주소
~~~
Mariadb> CREATE TABLE memberTBL (
    memberID VARCHAR(8) NULL,
    memberName VARCHAR(6) NULL,
    memberPhone VARCHAR(13) NOT NULL,
    memberAddress VARCHAR(30) NOT NULL);

Mariadb> DROP TABLE memberTBL;
Mariadb> DESCRIBE memberTBL;
Mariadb> DESC memberTBL;
~~~

### - 데이터 입력

~~~
Mariadb> INSERT INTO memberTBL(memberID, memberName, memberPhone, memberAddress) VALUES('1000','KIM','010-1234-5678','SEOUL');
Mariadb> INSERT INTO memberTBL VALUES('1000','KIM','010-1234-5678','SEOUL');

Mariadb> SELECT * FROM memberTBL;
Mariadb> SELECT memberID, memberName, memberPhone FROM memberTBL;
~~~

### - 테이블 변경
~~~
Mariadb> ALTER TABLE memberTBL MODIFY memberID INT;
Mariadb> ALTER TABLE memberTBL MODIFY memberID VARCHAR(8);
~~~

### - csv 실습
1. 엑셀로 만들기 -> 저장할때 csv로 저장
2. 메모장으로 만들기 -> 모든 파일로 저장

* csv(콤마로), tsv(탭으로), ssv(스페이스바로) 

unresolved import 'sys'
### - mysql 접속
~~~
cmd> pip install mysqlclient

mariadb> CREATE DATABASE my_suppliers;
~~~





