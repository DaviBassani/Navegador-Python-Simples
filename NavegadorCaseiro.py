import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


# Janela principal do Navegador
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showNormal()

        navbar = QToolBar() # Criando a barra de navegação
        self.addToolBar(navbar)

        back_btn = QAction('<', self) # Criando o botão de voltar
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('>', self) #Criando o botão de Avançar
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Recarregar', self) #Criando o botão de recarregar
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self) #Criando o botão home
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit() #Criando a barra de URL
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url) #Atualizar o URL quando pedir para entrar em outra página

        search_btn = QAction('Pesquisar', self) #Criando o botão de pesquisa
        search_btn.triggered.connect(self.navigate_to_url)
        navbar.addAction(search_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com')) #Site para o qual irá quando apertar o botão home

    def navigate_to_url(self): # Pesquisar o URL
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self): #Atualizar o URL
        self.url_bar.setText(q.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Bassani Browser')
    window = MainWindow()
    app.exec_()