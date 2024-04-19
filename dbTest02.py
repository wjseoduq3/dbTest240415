import pymysql  # mysql과 연동시켜주는 라이브러리

# 파이썬과 mysql간에 커넥션 생성(4가지 필요)
# 1) 계정 guest01 (본인PC는 root계정)
# 2) 비밀번호 12345
# 3) 데이터베이스가 설치된 컴퓨터 IP 주소:
# 본인 컴퓨터: localhost(127.0.0.1 쳐도 됨)
# 교수용컴퓨터: 192.168.0.100
# port: 3306
# 4) 데이터베이스 스키마의 이름: 예: shopdbjdy

#  커넥션 생성
dbConn = pymysql.connect(host='192.168.0.100', user='guest01', password='12345', db='shopdbjdy')

sql = "INSERT INTO membertbl VALUES('pion', '김호랑', '인천 동구')"  #DB에 실행할 sql문 생성/
# 매번 아이디 변경해줘야 중복 에러 안남

cur = dbConn.cursor()
result = cur.execute(sql)  # 연결된 DB의 스키마에 지정된 sql문 실행
# result = cur.execute(sql)이 성공적으로 수행되면
# print(result) 하면 1이 출력됨 (insert, delete, update)
if result == 1:
    print('회원가입이 성공하였습니다.')

records = cur.fetchall()  # sql에서 실행된 select문의 결과를 받아서 records로 저장
# print(records)  # 결과는 튜플로 옴
# print(records[0])
# print(records[0][1])
#
# for member in records:
#     print(member[1])


# dbConn 사용이 종료된 후에는  DB 닫아줘야 함
# 먼저 cur 닫고 다음에 dbConn 닫음
cur.close()
dbConn.commit()  # DB를 변화시킨 후 커밋하고 닫아야 함
dbConn.close()


