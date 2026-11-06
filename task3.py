import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit,
    QFileDialog, QMessageBox, QToolBar
)
from PyQt6.QtGui import QAction, QKeySequence


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Текстовий редактор")
        self.resize(650, 450)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Введіть текст...")
        self.setCentralWidget(self.text_edit)

        self.statusBar().showMessage("Програма готова до роботи")

        file_menu = self.menuBar().addMenu("Файл")
        help_menu = self.menuBar().addMenu("Довідка")

        self.open_action = QAction("Відкрити", self)
        self.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_action.triggered.connect(self.open_file)
        file_menu.addAction(self.open_action)

        self.save_action = QAction("Зберегти", self)
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.triggered.connect(self.save_file)
        file_menu.addAction(self.save_action)

        self.exit_action = QAction("Вихід", self)
        self.exit_action.triggered.connect(self.close)
        file_menu.addAction(self.exit_action)

        self.about_action = QAction("Про програму", self)
        self.about_action.triggered.connect(self.show_about)
        help_menu.addAction(self.about_action)

        self.info_action = QAction("Інструкція", self)
        self.info_action.triggered.connect(self.show_instruction)
        help_menu.addAction(self.info_action)

        toolbar = QToolBar("Панель інструментів")
        self.addToolBar(toolbar)

        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)

        self.text_edit.textChanged.connect(self.update_status)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Відкрити файл",
            "",
            "Текстові файли (*.txt);;Усі файли (*)"
        )

        if filename:
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    self.text_edit.setPlainText(file.read())

                self.statusBar().showMessage(
                    f"Відкрито файл: {filename}"
                )
            except (OSError, UnicodeError) as error:
                QMessageBox.warning(self, "Помилка", str(error))

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Зберегти файл",
            "",
            "Текстові файли (*.txt)"
        )

        if filename:
            try:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(self.text_edit.toPlainText())

                self.statusBar().showMessage(
                    f"Збережено файл: {filename}"
                )
            except OSError as error:
                QMessageBox.warning(self, "Помилка", str(error))

    def update_status(self):
        text = self.text_edit.toPlainText()
        self.statusBar().showMessage(
            f"Кількість символів: {len(text)}"
        )

    def show_about(self):
        QMessageBox.about(
            self,
            "Про програму",
            "Простий текстовий редактор на Python з PyQt6."
        )
        self.statusBar().showMessage("Відкрито інформацію про програму")

    def show_instruction(self):
        QMessageBox.information(
            self,
            "Інструкція",
            "Ctrl+O - відкрити файл\n"
            "Ctrl+S - зберегти файл\n"
            "Текст можна вводити у центральному полі."
        )
        self.statusBar().showMessage("Відкрито інструкцію")


def main():
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

