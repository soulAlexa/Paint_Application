from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush, QPixmap, QBitmap, QPalette
from PyQt5.QtCore import Qt, QPoint, QRect, QSize
from scipy import signal
import numpy as np
import sys

from PyQt5.uic.properties import QtCore


class Window(QMainWindow):
    w = 800
    h = 600
    T = 0

    def __init__(self):
        super().__init__()

        title = "Paint Application"
        top = 400
        left = 400
        width = 800
        height = 600
        icon = "icons/pain.png"

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        brushSize = mainMenu.addMenu("Brush Size")
        brushColor = mainMenu.addMenu("Brush Color")
        furie = mainMenu.addMenu("Furie")

        furierectangular = QAction(QIcon("icons/furierectangular.png"), "furierectangular", self)
        furie.addAction(furierectangular)
        furierectangular.triggered.connect(self.furierectangular)

        furietriangula = QAction(QIcon("icons/furietriangula.png"), "furietriangula", self)
        furie.addAction(furietriangula)
        furietriangula.triggered.connect(self.furietriangular)

        fuiresawtooth = QAction(QIcon("icons/fuiresawtooth.png"), "fuiresawtooth", self)
        furie.addAction(fuiresawtooth)
        fuiresawtooth.triggered.connect(self.fuiresawtooth)

        fillAction = QAction(QIcon("icons/fill.png"), "fill", self)
        fillAction.setShortcut("Ctrl+N")
        brushSize.addAction(fillAction)
        fillAction.triggered.connect(self.fill)

        openAction = QAction(QIcon("icons/open.png"), "Open", self)
        openAction.setShortcut("Ctrl+O")
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.openpng)

        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon("icons/clear.png"), "Clear", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        threepxAction = QAction(QIcon("icons/threepx.png"), "3px", self)
        brushSize.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePixel)

        fivepxAction = QAction(QIcon("icons/fivepx.png"), "5px", self)
        brushSize.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePixel)

        sevenpxAction = QAction(QIcon("icons/sevenpx.png"), "7px", self)
        brushSize.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPixel)

        ninepxAction = QAction(QIcon("icons/ninepx.png"), "9px", self)
        brushSize.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePixel)

        blackAction = QAction(QIcon("icons/black.png"), "Black", self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        whitekAction = QAction(QIcon("icons/white.png"), "White", self)
        whitekAction.setShortcut("Ctrl+W")
        brushColor.addAction(whitekAction)
        whitekAction.triggered.connect(self.whiteColor)

        redAction = QAction(QIcon("icons/red.png"), "Red", self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction = QAction(QIcon("icons/green.png"), "Green", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction = QAction(QIcon("icons/yellow.png"), "Yellow", self)
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

    def mousePressEvent(self, event):
        if self.T == 4 and event.button() == Qt.LeftButton:
            x = np.linspace(0, 1, 1000, endpoint=True)
            y = signal.square(2 * np.pi * 4 * x)
            painter = QPainter(self.image)

            # painter.setRenderHint(QPainter.HighQualityAntialiasing)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            g = self.geometry()
            x_1 = round(event.x() / (g.width() / self.w))
            y_1 = round(event.y() / (g.height() / self.h))
            for i in range(999):
                painter.drawLine(int(x[i] * 50 + x_1), int(y[i] * 50 + y_1), int(x[i + 1] * 50 + x_1),
                                 int(y[i + 1] * 50 + y_1))
            self.update()
        if self.T == 3 and event.button() == Qt.LeftButton:
            x = np.linspace(0, 1, 1000, endpoint=True)
            y = signal.sawtooth(2 * np.pi * 4 * x, 0.5)
            painter = QPainter(self.image)
            # painter.setRenderHint(QPainter.HighQualityAntialiasing)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            g = self.geometry()
            x_1 = round(event.x() / (g.width() / self.w))
            y_1 = round(event.y() / (g.height() / self.h))
            for i in range(999):
                painter.drawLine(int(x[i] * 50 + x_1), int(y[i] * 50 + y_1), int(x[i + 1] * 50 + x_1),
                                 int(y[i + 1] * 50 + y_1))
            self.update()
        if self.T == 2 and event.button() == Qt.LeftButton:
            x = np.linspace(0, 1, 1000, endpoint=True)
            y = signal.sawtooth(2 * np.pi * 4 * x)
            painter = QPainter(self.image)
            # painter.setRenderHint(QPainter.HighQualityAntialiasing)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            g = self.geometry()
            x_1 = round(event.x() / (g.width() / self.w))
            y_1 = round(event.y() / (g.height() / self.h))
            for i in range(999):
                painter.drawLine(int(x[i] * 50 + x_1), int(y[i] * 50 + y_1), int(x[i + 1] * 50 + x_1),
                                 int(y[i + 1] * 50 + y_1))
            self.update()

        if self.T == 1 and event.button() == Qt.LeftButton:
            w, h = self.image.width(), self.image.height()
            x, y = event.x(), event.y()
            target_color = self.image.pixel(x, y)
            have_seen = set()
            queue = [(x, y)]

            def get_cardinal_points(have_seen, center_pos):
                points = []
                cx, cy = center_pos
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    xx, yy = cx + x, cy + y
                    if (xx >= 0 and xx < w and yy >= 0 and yy < h and (xx, yy) not in have_seen):
                        points.append((xx, yy))
                        have_seen.add((xx, yy))

                return points

            p = QPainter(self.image)
            p.setPen(QPen(self.brushColor))
            while queue:
                x, y = queue.pop()
                if self.image.pixel(x, y) == target_color:
                    p.drawPoint(QPoint(x, y))
                    queue.extend(get_cardinal_points(have_seen, (x, y)))

            self.update()

        if event.button() == Qt.LeftButton:
            self.drawing = True
            g = self.geometry()
            x = round(event.pos().x() / (g.width() / self.w))
            y = round(event.pos().y() / (g.height() / self.h))
            self.lastPoint = QPoint(x, y)
            # print(self.lastPoint)

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            # painter.drawLine(self.lastPoint, event.pos())
            g = self.geometry()
            x = round(event.pos().x() / (g.width() / self.w))
            y = round(event.pos().y() / (g.height() / self.h))
            painter.drawLine(self.lastPoint, QPoint(x, y))
            self.lastPoint = QPoint(x, y)
            self.update()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def fill(self):
        self.T = 1

    def openpng(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                              "PNG image files (*.png); JPEG image files (*jpg); All files (*.*)")
        if path:
            im = QImage(path)
            self.w, self.h = (im.width(), im.height())
            self.setGeometry(400, 400, self.w, self.h)
            self.image = im

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def threePixel(self):
        self.T = 0
        self.brushSize = 3

    def fivePixel(self):
        self.T = 0
        self.brushSize = 5

    def sevenPixel(self):
        self.T = 0
        self.brushSize = 7

    def ninePixel(self):
        self.T = 0
        self.brushSize = 9

    def blackColor(self):
        self.brushColor = Qt.black

    def whiteColor(self):
        self.brushColor = Qt.white

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow

    def furietriangular(self):
        self.T = 3

    def furierectangular(self):
        self.T = 4

    def fuiresawtooth(self):
        self.T = 2


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()