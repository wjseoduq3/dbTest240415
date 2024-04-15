import pymysql  # mysql과 연동시켜주는 라이브러리

# 파이썬과 mysql간에 커넥션 생성(4가지 필요)
# 1) 계정 guest01
# 2) 비밀번호 12345
# 3) 데이터베이스가 설치된 컴퓨터 IP 주소:
# 본인 컴퓨터: localhost
# 교수용컴퓨터: 192.168.0.100
# 4) 데이터베이스 스키마의 이름: ex-shopdb

#  커넥션 생성
dbConn = pymysql.connect(host='192.168.0.100', user='guest01', password='12345', db='shopdb')

sql = "SELECT * FROM membertbl"  #DB에 실행할 sql문 생성
cur = dbConn.cursor()
cur.execute(sql)  # 연결된 DB의 스키마에 지정된 sql문 실행

records = cur.fetchall()  # sql에서 실행된 select문의 결고를 받아서 records로 저장
print(records)  # 결과는 튜플로 옴
# print(records[0])
# print(records[0][1])

for member in records:
    print(member[1])


# dbConn의 사용이 종로된 후에는  DB 닫아줘야 함
# 먼저 cur닫고 다음에 dbConn 닫음
cur.close()
dbConn.close()


