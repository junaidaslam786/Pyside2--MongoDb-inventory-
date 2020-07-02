from main import *

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:
            # Get Width
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 80

            # Set Max Width
            if width == 80:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # Animation
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b'minimumWidth')
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

