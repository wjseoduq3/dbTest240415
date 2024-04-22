import sys
import pymysql

from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/member.ui")[0]  # 미리 제작해놓은 UI 불러오기

# 메인 윈도우 만들기
class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원관리프로그램")

        # 버튼 이벤트 처리
        self.join_btn.clicked.connect(self.member_join)
        self.joinreset_btn.clicked.connect(self.join_reset)
        self.idcheck_btn.clicked.connect(self.idcheck)
        self.membersearch_btn.clicked.connect(self.member_search)
        self.memberreset_btn.clicked.connect(self.memberInfo_reset)
        self.membermodify_btn.clicked.connect(self.member_modify)
        self.loginreset_btn.clicked.connect(self.loginInfo_reset)
        self.login_btn.clicked.connect(self.member_login)

    def member_join(self):  # 회원가입 이벤트 처리 함수
        memberid = self.joinid_edit.text()  # 유저가 입력한 회원아이디 텍스트 가져오기
        memberpw = self.joinpw_edit.text()
        membername = self.joinname_edit.text()
        memberemail = self.joinemail_edit.text()
        memberage = self.joinage_edit.text()

        if memberid == "" or memberpw == "" or membername == "" or memberemail == "" or memberage == "":
            QMessageBox.warning(self, "정보입력오류", "입력정보중 누락된 부분이 있습니다. 다시 입력해주세요.")
        elif len(memberid) < 4 or len(memberid) >=15:
            QMessageBox.warning(self, "아이디길이오류", "아이디는 4자 이상 11자 이하이어야 합니다. 다시 입력해주세요.")
        elif len(memberpw) < 4 or len(memberid) >= 15:
            QMessageBox.warning(self, "비밀번호길이오류", "비밀번호는 4자 이상 11자 이하이어야 합니다. 다시 입력해주세요.")
        elif self.idcheck() == 0:  # 가입불가
            # QMessageBox.warning(self, "회원가입불가", "이미 가입된 아이디입니다.")
            pass

        else:
            dbConn = pymysql.connect(user='guest01', password='12345', host='192.168.0.100', db='shopdbjdy')
            sql =f"INSERT INTO appmember VALUES('{memberid}', '{memberpw}', '{membername}', '{memberemail}', '{memberage}')"

            cur =dbConn.cursor()
            result = cur.execute(sql)  # 회원가입 sql 문이 성공하면 1이 반환

            if result == 1:
                QMessageBox.warning(self, "회원가입성공", "축하합니다.\n회원가입이 성공하였습니다.")
                self.join_reset()
            else:
                QMessageBox.warning(self, "회원가입실패", "회원가입이 실패하였습니다.")
            cur.close()
            dbConn.commit()
            dbConn.close()

    def join_reset(self):  # 회원가입장보 입력내용 초기화
        self.joinid_edit.clear()
        self.joinpw_edit.clear()
        self.joinname_edit.clear()
        self.joinemail_edit.clear()
        self.joinage_edit.clear()

    # 문제 있음 - 체크 필요
    def idcheck(self):  # 기존 아이디 존재 여부 체크 함수

        if memberid == "":
            QMessageBox.warning(self, "아이디입력오류", "아이디는 필수입력사항입니다. 다시 입력해주세요.")
        elif len(memberid) < 4 or len(memberid) >= 15:
            QMessageBox.warning(self, "아이디길이오류", "아이디는 4자 이상 11자 이하이어야 합니다. 다시 입력해주세요.")
        else:
            dbConn = pymysql.connect(user='guest01', password='12345', host='192.168.0.100', db='shopdbjdy')
            sql = f"SELECT count(*) FROM appmember WHERE memberid='{memberid}'"

            cur = dbConn.cursor()
            cur.execute(sql)

            result = cur.fetchall()
            print(result)

            if result[0][0] == 1:
                # 내용수정
                QMessageBox.warning(self, "회원가입불가", "이미 가입된 아이디입니다.")
                return 0
            else:
                # 내용수정
                QMessageBox.warning(self, "회원가입가능", "회원가입가능한 아이디입니다.")
                return 1

            cur.close()
            dbConn.close()

    def member_check(self):
        memberid = self.memberid_edit.text()

        dbConn = pymysql.connect(user='guest01', password='12345', host='192.168.0.100', db='shopdbjdy')
        sql = f"SELECT count(*) FROM appmember WHERE memberid='{memberid}'"

        cur = dbConn.cursor()
        cur.execute(sql)

        result = cur.fetchall()
        print(result)

        if result[0][0] == 1:
           return 1
        else:
           # 내용수정
            QMessageBox.warning(self, "회원조회불가", "아이디를 다시 입력해주세요.")
            return 0

            cur.close()
            dbConn.close()

    # 회원 조회
    def member_search(self):
        memberid = self.memberid_edit.text()  # 유저가 입력한 아이디 텍스트 가져오기
        dbConn = pymysql.connect(user="guest01", password="12345", host="192.168.0.100", db="shopdbjdy")

        sql = f"SELECT * FROM appmember WHERE memberid='{memberid}'"
        # SQL문 실행 시 1 또는 0이 반환(기존에 가입된 아이디면 1, 아니면 0)

        if memberid == "":
            QMessageBox.warning(self, "아이디입력오류", "아이디는 필수 입력사항입니다.\n아이디를 입력해주세요.")
        elif self.member_check() == 0:
            pass
        else:
            cur = dbConn.cursor()
            cur.execute(sql)  # 회원가입하는 sql문이 성공하면 1이 반환

            result = cur.fetchall()

            print(result)

            self.memberpw_edit.setText(str(result[0][1]))  # 비밀번호 출력
            self.membername_edit.setText(str(result[0][2]))  # 회원이름 출력
            self.memberemail_edit.setText(str(result[0][3]))  # 이메일 출력
            self.memberage_edit.setText(str(result[0][4]))  # 회원나이 출력

            cur.close()
            dbConn.close()

    def memberInfo_reset(self):  # 회원조회정보 입력내용 초기화
        self.memberid_edit.clear()
        self.memberpw_edit.clear()
        self.membername_edit.clear()
        self.memberemail_edit.clear()
        self.memberage_edit.clear()

    def loginInfo_reset(self):  # 회원가입 이벤트 처리 함수
        self.loginid_edit.clear()  # 유저가 입력한 회원아이디 텍스트 가져오기
        self.loginpw_edit.clear()

    def member_modify(self):
        memberid = self.memberid_edit.text()
        memberpw = self.memberpw_edit.text()
        membername = self.membername_edit.text()
        memberemail = self.memberemail_edit.text()
        memberage = self.memberage_edit.text()

        dbConn = pymysql.connect(user="guest01", password="12345", host="192.168.0.100", db="shopdbjdy")

        sql = f"UPDATE appmember SET memberpw='{memberpw}', membername='{membername}', memberemail='{memberemail}', memberage='{memberage}' WHERE memberid='{memberid}'"

        cur = dbConn.cursor()
        result = cur.execute(sql)

        if result == 1:
            QMessageBox.warning(self, "회원정보수정 성공", "회원정보수정이 성공하였습니다.")
        else:
            QMessageBox.warning(self, "회원정보수정 실패", "회원정보수정이 실패하였습니다.")

        cur.close()
        dbConn.commit()
        dbConn.close()

    def member_login(self):
        loginid = self.loginid_edit.text()
        loginpw = self.loginpw_edit.text()

        if loginid == "" or loginpw == "":
            QMessageBox.warning(self, "로그인 실패", "아이디 또는 비밀번호를 입력하세요.")
        else:
            dbConn = pymysql.connect(user="guest01", password="12345", host="192.168.0.100", db="shopdbjdy")
            sql = f"SELECT count(*) FROM appmember WHERE memberid='{loginid}' AND memberpw='{loginpw}'"

            cur = dbConn.cursor()
            cur.execute(sql)

            result = cur.fetchall()

            if result[0][0] == 1:
                QMessageBox.warning(self, "로그인 성공", f"{loginid}님 로그인 성공하였습니다.")
            else:
                QMessageBox.warning(self, "로그인 실패", "아이디 또는 비밀번호가 잘못되었습니다.")


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())

