import sys
import webbrowser
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from go import go_
import logging
import logfolder.logging
from paths import *

logging.basicConfig(filename=pathlog_,format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logfolder.logging.log_date()

def pushButton():
    '''
    function runs after clicking  "Выполнить экспорт" button in PyQT window
    use function go_(number_lines_to_export) if no any exceptions occures
    '''

    try:
        import shutil
        shutil.copyfile(pathprice1, pathprice2)

        number_lines_to_export=0  # 0 for all lines
        go_(number_lines_to_export)
        form.plainTextEdit.setPlainText("ЭКСПОРТ ДАННЫХ ВЫПОЛНЕН")


    except FileNotFoundError:
        logfolder.logging.log_txt("Нет excel-файла price.xlsx в каталоге export/files/ !")
        form.plainTextEdit.setPlainText("Нет excel-файла price.xlsx в каталоге export/files/")
        logging.exception('Нет excel-файла price.xlsx в каталоге export/files/')

    except ValueError:
        print('Нет подключения к базе данных Mysql')
        form.plainTextEdit.setPlainText('Нет подключения к базе данных Mysql. Проверьте Ваш IP')
        logfolder.logging.log_txt('Нет подключения к базе данных Mysql. Проверьте Ваш IP')
        logging.exception('Нет подключения к базе данных Mysql. Проверьте Ваш IP')
    except Exception:
        form.plainTextEdit.setPlainText(str(Exception))
        logging.exception("Exception occurred")

    finally:
        form.pushButton_3.setEnabled(True)
        form.pushButton_2.setEnabled(True)

Form, Window = uic.loadUiType(pathqt_)
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)



form.pushButton_2.setEnabled(False)
form.pushButton_3.setEnabled(False)
form.pushButton.clicked.connect(pushButton)
form.pushButton_3.clicked.connect(lambda: webbrowser.open(pathlog_))
form.pushButton_2.clicked.connect(app.quit)

window.show()
sys.exit(app.exec_())







