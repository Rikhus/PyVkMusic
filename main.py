import sys
sys.path.insert(0, 'design')
sys.path.insert(0, 'resources')
from time import time
import os
import requests
import vk_api
from vk_api import audio
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import design
from PyQt5.QtCore import *
import config
import loginDesign
import notif


#класс окна логина
#класс дизайна
class loginApp(QtWidgets.QMainWindow, loginDesign.Ui_MainWindow):
    def __init__(self):
        super(loginApp, self).__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.login)

    def login(self):
        self.login=self.loginLine.text()
        self.password=self.passLine.text()
        #try:
        if(1==1):
            if(self.login!="" and self.password!=""):
                self.vk_session = vk_api.VkApi(login=self.login, password=self.password)
                self.vk_session.auth()
                self.vk = self.vk_session.get_api()
                self.userJson=self.vk.photos.getWallUploadServer(v="5.0")
                self.my_id=self.userJson['user_id']    #получение id
                os.remove('vk_config.v2.json')
                config.login=self.login
                config.password=self.password
                config.my_id=self.my_id
                notif.sendNotification("Авторизация прошла успешно","VkMusic","VkMusic","resources\\img\\vk.ico")
                self.window=mainApp() #берем дизайн
                self.window.setWindowTitle('VK Music')
                self.window.setWindowIcon(QIcon('resources\\img\\vk.png'))       #favicon-32x32.png
                self.window.show()   #показываем окно
                self.close()

        #except vk_api.exceptions.BadPassword:
        #    self.lblStatus.setText('Неверный логин/пароль')


#класс дизайна
class mainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(mainApp, self).__init__()
        self.setupUi(self)
        self.downloadButton.clicked.connect(self.downloadAll)
        self.stopButton.clicked.connect(self.stopThis)
        self.listWidget.itemClicked.connect(self.checkItem)
        self.downloadCheckedButton.clicked.connect(self.downloadChecked)
        #vk init

        self.login =  config.login # Номер телефона
        self.password = config.password   # Пароль
        self.my_id = config.my_id  # Ваш id vk
        self.vk_session = vk_api.VkApi(login=self.login, password=self.password)
        self.vk_session.auth()
        self.vk = self.vk_session.get_api()  # Теперь можно обращаться к методам API как к обычным классам
        self.vk_audio = audio.VkAudio(self.vk_session)  # Получаем доступ к audio
        os.remove('vk_config.v2.json')
        #-----вывод музыки
        self.thread1 = QThread()
        self.shower = AudioShow(self,self.my_id,self.vk_audio)
        self.shower.moveToThread(self.thread1)
        self.thread1.started.connect(self.shower.run)
        self.thread1.start()
        self.thread2 = QThread()
    #загрузка музыки
    def downloadAll(self):
        j=0
        for i in self.vk_audio.get(owner_id=self.my_id):
            config.songsToDownload.append(j)
            j+=1
        self.downloadChecked()

    def downloadChecked(self):
        config.songsToDownload=list(set(config.songsToDownload))
        if(config.isStopped==True and config.isDownloadStopped==True):
            self.thread2.terminate()
            del self.thread2
            self.thread2 = QThread()
            self.path = QFileDialog.getExistingDirectory()
            self.downloader = AudioDownloader(self,self.my_id,self.vk_audio,self.path)
            self.downloader.moveToThread(self.thread2)
            self.thread2.started.connect(self.downloader.run)
            self.thread2.start()
    #остановка загрузки
    def stopThis(self):
        if config.isStopped==False:
            self.lblStatus.setStyleSheet("color: rgb(255, 0, 0)")
            self.lblStatus.setText("Остановка загрузки ")
            config.songsToDownload=[]
            config.isStopped=True

    #отметить аудиозапись для скачивания
    def checkItem(self,item):
        if(config.isStopped):
            if(not self.listWidget.currentRow() in config.songsToDownload):
                item.setBackground(QColor('#3830d1'))
                self.listWidget.update()
                config.songsToDownload.append(self.listWidget.currentRow())
            else:
                item.setBackground(QColor('#dddddd'))
                self.listWidget.update()
                config.songsToDownload=list(filter(lambda a: a !=self.listWidget.currentRow() , config.songsToDownload))

#класс скачивания музыки
#---------класс бота
class AudioDownloader(QObject):
    def __init__(self, window,my_id,vk_audio,path):
        super(AudioDownloader, self).__init__()
        self.window=window
        self.my_id=my_id
        self.vk_audio=vk_audio
        self.path=path
        self.REQUEST_STATUS_CODE = 200

    @pyqtSlot()
    def run(self):
        try:
            notif.sendNotification("Загрузка началась","VkMusic","VkMusic","resources\\img\\vk.ico")
        except Exception as e:
            print(e)
                        
        self.window.lblStatus.setStyleSheet("color: rgb(0, 255, 0)")
        self.window.lblStatus.setText('Идет скачивание')
        for x in range(self.window.listWidget.count()):
            if(not x in config.songsToDownload):
                self.window.listWidget.item(x).setBackground(QColor('#DDDDDD'))
        config.isStopped=False
        config.isDownloadStopped=False
        if(self.path!=""):
            print("Path:"+self.path)
            os.chdir(self.path)
            self.time_start = time()
            j=0
            for i in self.vk_audio.get(owner_id=self.my_id):
                if(j in config.songsToDownload):
                    try:
                        self.window.lblStatus.setStyleSheet("color: rgb(0, 255, 0)")
                        self.window.lblStatus.setText('Идет скачивание')
                        self.filename=i["artist"] + '_' + i["title"] + '.mp3'
                        if(not os.path.isfile(self.filename)):    #проверка на существование файла
                            self.r = requests.get(i["url"])
                            if self.r.status_code == self.REQUEST_STATUS_CODE:
                                if(config.isStopped==False):
                                    with open(self.filename, 'wb') as self.output_file:
                                        self.output_file.write(self.r.content)
                                else:
                                    break

                        self.listItem=self.window.listWidget.item(j)
                        self.listItem.setBackground( QColor('#32CD32') )
                        self.window.listWidget.update()
                        j+=1
                    except OSError:
                        print("Error:"+i["artist"] + '_' + i["title"])
                        self.listItem=self.window.listWidget.item(j)
                        self.listItem.setBackground( QColor('#eb0000') )
                        self.window.listWidget.update()
                        j+=1
                else:
                    j+=1

            self.time_finish = time()
            print("Time seconds:", self.time_finish - self.time_start)
            config.isDownloadStopped=True
            #если песни скачаны а не нажата кнопка стоп
            if(config.isStopped==False):
                self.window.lblStatus.setStyleSheet("color: rgb(0, 255, 0)")
                self.window.lblStatus.setText('Скачано успешно')
                config.isStopped=True
                notif.sendNotification("Загрузка завершена","VkMusic","VkMusic","resources\\img\\vk.ico")
            else:
                self.window.lblStatus.setStyleSheet("color: rgb(255, 0, 0)")
                self.window.lblStatus.setText("Остановлено")
                notif.sendNotification("Загрузка остановлена","VkMusic","VkMusic","resources\\img\\vk.ico")
            print('Stop')


#класс для вывода аудио
class AudioShow(QObject):
    def __init__(self, window,my_id,vk_audio):
        super(AudioShow,self).__init__()
        self.window=window
        self.my_id=my_id
        self.vk_audio=vk_audio
    @pyqtSlot()
    def run(self):
        self.window.lblStatus.setStyleSheet("color: rgb(0, 255, 0)")
        self.window.lblStatus.setText('Загружаю список песен')
        for i in self.vk_audio.get(owner_id=self.my_id):
            try:
                self.window.listWidget.addItem(i['artist']+" - "+i['title'])
            except OSError:
                print(i["artist"] + '_' + i["title"])
        self.window.lblStatus.setText('Список песен загружен')



#главная функция
def main():
    app=QtWidgets.QApplication(sys.argv)    #новая прога
    window=loginApp() #берем дизайн
    window.setWindowTitle('VK Music - Login')
    window.setWindowIcon(QIcon('resources\\img\\vk.png'))       #favicon-32x32.png
    window.show()   #показываем окно
    app.exec()  #запускаем

#запуск скрипта
main()
