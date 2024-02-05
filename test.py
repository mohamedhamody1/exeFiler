from PyQt5.QtWidgets import QApplication, QMessageBox
import sys
import subprocess

def restart_computer():
    subprocess.call(["shutdown", "-r", "-t", "0"])


def popup():
    app = QApplication(sys.argv)
    for _ in range(30):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Your computer is about to reset")
        msgBox.setWindowTitle("Warning")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            msgBox.setText("Your computer is about to reset...")
            restart_computer()
            break

popup()
