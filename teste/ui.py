import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication

def main():
    app = QApplication(sys.argv)
    startWindow()
    sys.exit(app.exec())

# constroÃ­ a janela inicialmente
def startWindow():
    window = QWidget()
    window.setWindowTitle("CLP Python")
    window.setGeometry(300, 300, 300, 100)
    window.show()

# define evento para iniciar a pintura
def paintEvent(self, e):
    qp = QPainter()
    qp.begin(self)
    self.DrawObject(qp)
    qp.end()

# # desenhar o objeto em si
# def drawObject(self, qp):
#     col = QColor(0, 0, 0)
#     col.setNamedColor('#d4d4d4')
#     qp.setPen(col)

#     qp.setBrush(QColor(200, 0, 0))
#     qp.drawRect(10, 15, 90, 60)

#     qp.setBrush(QColor(255, 80, 0, 160))
#     qp.drawRect(130, 15, 90, 60)

#     qp.setBrush(QColor(25, 0, 90, 200))
#     qp.drawRect(250, 15, 90, 60)

if __name__ == '__main__':
    main()