# 파일시스템: 폴더 또는 디렉토리로 데이터를 저장하는 방법
# 데이터베이스: 데이터를 효율적으로 저장하고 관리해주는 시스템(이론)

# 데이터베이스 관리 시스템(DBMS): 데이터베이스 제품!

# ** DBMS 종류
#  1. 관계형 데이터베이스(RDB) : 전통적인(스키마:명세서)
#    - ORACLE      (비쌈, 대기업의 프로젝트에 많이 사용, JAVA삼, 마소 안드로이드 = JAVA, 소송검, 안드로이드 JAVA에서 다른걸로 바꿈)
#    - MySQL       (개발자가 무료로 만들었다가 넘겼는데 ORACLE에 팔아버림)
#    - MariaDB     (그래서 또 만들어버림)

#  2.NoSQL : New(빅데이터)
#    - MongoDB
#    - Redis

# ** DBMS 프로세스
#  - DB에 ID와 PW 저장
#   Pycharm(Python)  ---------------------------  DB(MongoDB)
#   1.Pycharm과 DB Connection 맺기
#    - IP: 컴퓨터를 접속 할 수 있는 주소
#    - PORT: 컴퓨터 내에 프로그램의 위치
#    - ID and PW
#   2.SQL을 사용해서 작업(CRUD) 진행
#    - SQL(구조질의어): RDB를 사용하기 위해서는 반드시 사용!
#    - RDB(SQL)을 사용, NoSQL(SQL X)
#    CREATE     -> INSERT
#    READ       -> SELECT
#    UPDATE     -> UPDATE
#    DELETE     -> DELETE

#  ** MongoDB 사용방법 2가지
#  1.직접 설치(Local)
#    - IP, PORT, ID, PW
#    - 장점: 사용, 관리편함, 커스터마이징 가능
#    - 단점: 설치과정 복잡, 설정 직접, 컴퓨터 자원 부족
#  2. MongoDB에서 제공하는 Web Cloud 사용
#    - URL, ID, PW
#    - 장점: 사용편함, 설치 X, 설정 x, 컴퓨터 자원 x
#    - 단점: 관리 x, 커스터마이징 x

#  ** MongoDB구조
#  설치: MongoDB(DBMS) : 시스템
#           ㄴ DB(카카오톡) : 폴더
#                ㄴ Collection(회원) : 표
#                ㄴCollection(톡)
#                ㄴCollection(친구)
#                ㄴ ...
#           ㄴ DB(카카오뱅크) : 폴더
#                ㄴCollection(회원)
#                ㄴCollection(계좌)
#                ㄴCollection(대출)
#                ㄴ ...
#           ㄴ DB(카카오페이) : 폴더
#                ㄴ ...

# pymongo: Python - MongoDB 연결해서 사용
# 왼쪽 아래  Terminal(Alt + F12)열어서 pip install pymongo
from pymongo import MongoClient


# MongoDB Connection
def conn_mongodb():
    # URL, ID, PW
    DB_ID = "root"  # 상수 (전체 대문자로 변수명을 사용, 변하지않음)
    DB_PW = "1234"  # 예시) 은행에서 금리(상수)
    client = MongoClient(f"mongodb+srv://{DB_ID}:{DB_PW}@daumcluster.n0bbe0l.mongodb.net/")  # URL
    db = client["daum"]
    collection = db.get_collection("news")
    return collection

