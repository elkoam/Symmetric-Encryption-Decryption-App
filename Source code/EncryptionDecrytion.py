from PyQt5.QtWidgets import *
from cryptography.fernet import Fernet
from PyQt5 import uic , QtWidgets

class  MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("mygui.ui", self)
        self.show()
        
        self.GenerateKey.clicked.connect(self.Gen)
        self.BrowseKey.clicked.connect(self.SelectKey)
        self.BrowseFile.clicked.connect(self.SelectFile)
        self.Encrypt.clicked.connect(self.EncryptF)
        self.Decrypt.clicked.connect(self.decryptF)
    

    def Gen(self):
        key = Fernet.generate_key()
        save_filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save the key")
        with open(save_filepath ,"wb") as TheKey:
            TheKey.write(key)

    
    def SelectKey(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select the encryption key")
        self.KeyLine.setText(filepath)

    def SelectFile(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select the file to be encrypted")
        self.FileLine.setText(filepath)


    def EncryptF(self):

         filepath1 = self.KeyLine.text()
         filepath2 = self.FileLine.text()

        
         with open(filepath1, "rb") as  key:
            my_key = key.read()

            f = Fernet(my_key)
        
         with open(filepath2, "rb") as ptext:
             my_plaintext = ptext.read()

         encrypted_text = f.encrypt(my_plaintext)

         save_filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save the encrypted file")
         with open(save_filepath ,"wb") as TheEncryptedFile:
            TheEncryptedFile.write(encrypted_text) 
         

    def decryptF(self):
        filepath1 = self.KeyLine.text()
        filepath2 = self.FileLine.text()

        
        with open(filepath1, "rb") as  key:
            my_key = key.read()

            f = Fernet(my_key)
        
        with open(filepath2, "rb") as etext:
             my_etext = etext.read()

        decrypted_text = f.decrypt(my_etext)

        save_filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save the decrypted file")
        with open(save_filepath ,"wb") as ThedecryptedFile:
            ThedecryptedFile.write(decrypted_text)


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == '__main__':
    main()