import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()
        self.contacts = {}  # 주소록 데이터를 저장할 딕셔너리
        self.initUI()   # UI 초기화 함수 호출

    def initUI(self):
        """ GUI 요소들을 생성하고 배치하는 함수 """
        layout = QVBoxLayout()  # 세로로 정렬되는 레이아웃 생성

        # 이름 입력
        self.name_label = QLabel('이름:')  # 이름 라벨
        self.name_input = QLineEdit()   # 사용자 입력을 받을 수 있는 텍스트 필드
        layout.addWidget(self.name_label)  # 레이아웃에 라벨 추가
        layout.addWidget(self.name_input)  # 레이아웃에 텍스트 필드 추가

        # 전화번호 입력
        self.phone_label = QLabel('전화번호:')  # 전화번호 라벨
        self.phone_input = QLineEdit()  # 전화번호 입력 필드
        layout.addWidget(self.phone_label)  # 레이아웃에 전화번호 라벨 추가
        layout.addWidget(self.phone_input)  # 레이아웃에 전화번호 입력 필드 추가

        # 추가 버튼
        self.add_button = QPushButton('추가')  # '추가' 버튼 생성
        self.add_button.clicked.connect(self.add_contact)  # 버튼 클릭 시 연락처 추가 함수 호출
        layout.addWidget(self.add_button)  # 레이아웃에 '추가' 버튼 추가

        # 검색 입력
        self.search_label = QLabel('이름 검색:')  # 검색 라벨
        self.search_input = QLineEdit()  # 검색 텍스트 필드
        layout.addWidget(self.search_label)  # 레이아웃에 검색 라벨 추가
        layout.addWidget(self.search_input)  # 레이아웃에 검색 텍스트 필드 추가

        # 검색 버튼
        self.search_button = QPushButton('검색')  # '검색' 버튼 생성
        self.search_button.clicked.connect(self.search_contact)  # 버튼 클릭 시 연락처 검색 함수 호출
        layout.addWidget(self.search_button)  # 레이아웃에 '검색' 버튼 추가ㄴ

        # 결과 표시
        self.result_text = QTextEdit()  # 결과를 보여줄 텍스트 편집기 생성
        self.result_text.setReadOnly(True)  # 읽기 전용으로 설정
        layout.addWidget(self.result_text)  # 레이아웃에 결과 텍스트 편집기 추가

        # 레이아웃을 설정하고 창 제목, 크기 설정
        self.setLayout(layout)
        self.setWindowTitle('간단한 주소록')  # 창의 제목 설정
        self.setGeometry(100, 100, 300, 300)  # 창의 위치와 크기 설정

    def add_contact(self):
        """ 사용자가 입력한 이름과 전화번호를 주소록에 추가하는 함수 """
        name = self.name_input.text().strip()   # 이름 입력값 가져오기
        phone = self.phone_input.text().strip() # 전화번호 입력값 가져오기
        
        if name and phone:  # 이름과 전화번호가 비어있지 않다면
            self.contacts[name] = phone # 딕셔너리에 이름과 전화번호 추가
            self.result_text.setText(f'연락처 저장 완료: {name} - {phone}') # 결과 텍스트로 저장 완료 메시지 표시
            self.name_input.clear() # 이름 입력 필드 비우기
            self.phone_input.clear()    # 전화번호 입력 필드 비우기
        else:
            self.result_text.setText('이름과 전화번호를 입력하세요!')   # 입력이 비어있으면 안내 메시지 표시

    def search_contact(self):
        """ 사용자가 입력한 이름으로 연락처를 검색하는 함수 """
        name = self.search_input.text().strip() # 검색 입력값 가져오기
        if name in self.contacts:   # 주소록에 이름이 있으면
            self.result_text.setText(f'{name}: {self.contacts[name]}')  # 이름과 전화번호 출력
        else:
            self.result_text.setText('연락처를 찾을 수 없습니다.')  # 이름이 없으면 찾을 수 없다는 메시지 출력

if __name__ == '__main__':
    app = QApplication(sys.argv)  # PyQt 애플리케이션 생성
    window = AddressBook()  # AddressBook 클래스의 인스턴스 생성
    window.show()  # 주소록 창을 화면에 표시
    sys.exit(app.exec_())  # 애플리케이션 실행
