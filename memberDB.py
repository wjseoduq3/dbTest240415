import pymysql

dbConn = pymysql.connect(user='guest01', password='12345', host='192.168.0.100', db='shopdbjdy')

while True:
    print("************ 회원관리 프로그램 ****************")
    print("1: 회원 가입")
    print("2: 회원 정보 수정")
    print("3: 회원 탈퇴")
    print("4: 전체 회원목록 조회")
    print("5: 프로그램 종료")
    print("****************************")
    menuNum = input("메뉴 중 한 가지를 선택하세요(1~5): ")

    if menuNum == "1":
        print("회원정보를 입력하세요")
        memberID = input("1) 회원ID를 입력하세요: ")
        memberName = input("2) 회원이름을 입력하세요: ")
        memberAddress = input("3) 회원주소를 입력하세요: ")

        sql = f"INSERT INTO membertbl VALUES('{memberID}', '{memberName}', '{memberAddress}')"
        cur = dbConn.cursor()
        result = cur.execute(sql)

        if result == 1:
            print("축하합니다! 회원가입 성공하였습니다.")
        else:
            print("회원가입 실패입니다.")

        cur.close()
        dbConn.commit()

    elif menuNum == "2":
        memberID = input("1) 정보를 수정할 수정할 회원ID를 입력하세요: ")
        memberName = input("2) 수정할 회원이름을 입력하세요: ")
        memberAddress = input("3) 수정할 회원주소를 입력하세요: ")

        sql = f"UPDATE membertbl SET memberName = '{memberName}', memberAddress = '{memberAddress}' WHERE memberID = '{memberID}'"

        cur = dbConn.cursor()
        result = cur.execute(sql)

        if result == 1:
            print("축하합니다! 회원수정 성공하였습니다.")
        else:
            print("회원수정 실패입니다.")

        cur.close()
        dbConn.commit()

    elif menuNum == "3":
        memberID = input("1) 탈퇴할 회원ID를 입력하세요: ")

        sql = f"DELETE FROM membertbl WHERE memberID = '{memberID}'"

        cur = dbConn.cursor()
        result = cur.execute(sql)

        if result == 1:
            print("회원탈퇴에 성공하였습니다.")
        else:
            print("회원탈퇴 실패입니다.")

        cur.close()
        dbConn.commit()

    elif menuNum == "4":
        sql = f"SELECT * FROM membertbl"
        cur = dbConn.cursor()
        cur.execute(sql)
        memberList = cur.fetchall()

        print("************ 회원리스트 ****************")
        for member in memberList:
            print(member[0], end=" / ")
            print(member[1], end=" / ")
            print(member[2])

        cur.close()
        dbConn.commit()

    elif menuNum == "5":
        print("프로그램을 종료합니다. 안녕히 가세요")
        dbConn.close()
        break

    else:
        print("잘못 입력하셨습니다.")



