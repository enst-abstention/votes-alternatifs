#         user = self.lineEdit.text()
        # password = self.lineEdit_2.text()
        # if len(user)==0 or len(password)==0:
        #     self.label_5.setText("Please fill all the fields")
        #
        # else :
        #     connection = sqlite3.connect("base de donnee identifiants.db")
        #     cur = connection.cursor()
        #     query = 'SELECT password FROM identifiants_info WHERE username= \''+user+"\'"
        #     cur.execute(query)
        #     result_pass = cur.fetchone()[0]
        #     if result_pass == password:
        #         print("Successfully logged in")
        #         self.label_5.setText("")
        #
        #     else:
        #         self.label_5.setText("Invalid username or password")


 """"
    def signup(self):       
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirmpass = self.lineEdit_3.text()
        if len(user)==0 or len(password)==0 or len(confirmpass)==0:
            self.label_5.setText("Please fill all the fields")
        elif confirmpass!=password :
            self.label_5.setText("Invalid password")
        else :
            connection = sqlite3.connect("base de donnee identifiants.db")
            cursor = connection.cursor()
            user_info=[user,password]
            cursor.excute("create table identifiants_info (username text, password numeric )")
            cursor.executemany('INSERT INTO identifiants_info  VALUES (?,?)',user_info)

            #connection.commit()
            connection.close()
            fillprofile=FillProfile()
            widget.addWidget()
            widget.setCurrentIndex(widget.currentIndex()+1)


class FillProfile(QDialog):
    def __init__(self):
        super(FillProfile,self).__init__()
        loadUi("fillprofile.ui",self)

        # combobox
        listpays=["FANCE","USA","ALLEMAGNE","ANGLETERRE","Other"]
        for pay in listpays :
            self.comboBox_3.addItem(pay)
        listoccup = ["Student","ENGINEER","Doctor","Teacher","Other"]
        for job in listoccup:
            self.comboBox_5.addItem(job)

        genre = ["M","F","Other"]
        for sexe in genre :
            self.comboBox_2.addItem(sexe)

        # Spin Box
        self.spinBox.set.Minimum(18)
        self.spinBox.set.Maximum(100)

    def profile(self):
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5.setReadOnly(True)
    """