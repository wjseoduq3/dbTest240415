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

    def member_join(self):  # 회원가입 이벤트 처리 함수
        memberid = self.joinid_edit.text()  # 우저가 입력한 회원아이디 텍스트 가져오기
        memberpw = self.joinpw_edit.text()
        membername = self.joinname_edit.text()
        memberemail = self.joinemail_edit.text()
        memberage = self.joinage_edit.text()

        dbConn = pymysql.connect(user='guest01', password='12345', host='192.168.0.100', db='shopdbjdy')

        sql =(f"INSERT INTO appmember VALUES('{memberid}', '{memberpw}', '{membername}', '{memberemail}', '{memberage}'")


        cur =dbConn.cursor()
        result = cur.execute(sql)  # 회원가입 sql 문이 성공하면 1이 반환

        cur.close()
        dbConn.commit()
        dbConn.close()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())

