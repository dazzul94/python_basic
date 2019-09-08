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

### 설정
~~~
SHOW VARIABLES LIKE 'C%';
~~~

### 사용자 계정 생성하기 
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




