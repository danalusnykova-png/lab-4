import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QDialog, QLabel,
    QLineEdit, QPushButton, QComboBox,
    QSpinBox, QVBoxLayout, QHBoxLayout,
    QFormLayout, QDialogButtonBox, QMessageBox,
    QInputDialog
)


STYLE = """
QWidget {
    background-color: #f1f5f9;
    color: #243247;
    font-size: 13px;
}

QLabel {
    font-size: 13px;
    color: #243247;
}

QPushButton {
    background-color: #dce6f4;
    border: 1px solid #b7c7dc;
    border-radius: 6px;
    padding: 9px;
}

QPushButton:hover {
    background-color: #bdcff0;
}

QPushButton:pressed {
    background-color: #9db8e7;
}

QLineEdit, QComboBox, QSpinBox {
    background-color: white;
    border: 1px solid #a8b7cb;
    border-radius: 5px;
    padding: 6px;
}

QLineEdit:focus {
    border: 2px solid #4278c7;
}

QPushButton#mainButton {
    background-color: #3467b1;
    color: white;
    font-weight: bold;
}

QPushButton#mainButton:hover {
    background-color: #24518e;
}
"""


class StudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Дані нового студента")
        self.setMinimumWidth(340)

        layout = QVBoxLayout()
        form = QFormLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введіть ім'я")
        form.addRow("Ім'я:", self.name_input)

        self.subject_box = QComboBox()
        self.subject_box.addItems([
            "Математика", "Фізика", "Програмування"
        ])
        form.addRow("Предмет:", self.subject_box)

        self.grade_spin = QSpinBox()
        self.grade_spin.setRange(0, 100)
        self.grade_spin.setValue(75)
        form.addRow("Оцінка:", self.grade_spin)

        layout.addLayout(form)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )

        self.buttons.accepted.connect(self.check_data)
        self.buttons.rejected.connect(self.reject)

        layout.addWidget(self.buttons)
        self.setLayout(layout)

    def check_data(self):
        if not self.name_input.text().strip():
            QMessageBox.warning(
                self, "Помилка", "Введіть ім'я студента"
            )
            return

        self.accept()

    def get_data(self):
        return (
            self.name_input.text().strip(),
            self.subject_box.currentText(),
            self.grade_spin.value()
        )


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Інформація про студентів")
        self.setMinimumSize(460, 350)

        self.name = "Не вказано"
        self.subject = "Не вказано"
        self.grade = 0
        self.styled = False

        layout = QVBoxLayout()

        self.title_label = QLabel("Робота з даними студентів")
        self.title_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.title_label)

        self.name_label = QLabel()
        self.subject_label = QLabel()
        self.grade_label = QLabel()
        self.status_label = QLabel()

        layout.addWidget(self.name_label)
        layout.addWidget(self.subject_label)
        layout.addWidget(self.grade_label)
        layout.addWidget(self.status_label)

        self.add_button = QPushButton("Додати студента")
        self.add_button.setObjectName("mainButton")
        self.rename_button = QPushButton("Змінити назву")
        self.clear_button = QPushButton("Очистити дані")
        self.style_button = QPushButton("Увімкнути стиль")

        layout.addWidget(self.add_button)
        layout.addWidget(self.rename_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.style_button)

        self.add_button.clicked.connect(self.add_student)
        self.rename_button.clicked.connect(self.rename_title)
        self.clear_button.clicked.connect(self.clear_data)
        self.style_button.clicked.connect(self.change_style)

        self.setLayout(layout)
        self.update_information()

    def update_information(self):
        self.name_label.setText(f"Студент: {self.name}")
        self.subject_label.setText(f"Предмет: {self.subject}")
        self.grade_label.setText(f"Оцінка: {self.grade}")

        if self.name == "Не вказано":
            self.status_label.setText("Статус: дані відсутні")
        elif self.grade >= 60:
            self.status_label.setText("Статус: предмет складено")
        else:
            self.status_label.setText("Статус: предмет не складено")

    def add_student(self):
        dialog = StudentDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.name, self.subject, self.grade = dialog.get_data()
            self.update_information()

    def rename_title(self):
        text, ok = QInputDialog.getText(
            self,
            "Зміна назви",
            "Введіть нову назву вікна:",
            text=self.windowTitle()
        )

        if ok and text.strip():
            self.setWindowTitle(text.strip())
            self.title_label.setText(text.strip())

    def clear_data(self):
        answer = QMessageBox.question(
            self,
            "Підтвердження",
            "Ви дійсно хочете очистити дані?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.name = "Не вказано"
            self.subject = "Не вказано"
            self.grade = 0
            self.update_information()

    def change_style(self):
        self.styled = not self.styled

        if self.styled:
            QApplication.instance().setStyleSheet(STYLE)
            self.title_label.setStyleSheet("font-weight: bold;")
            self.style_button.setText("Вимкнути стиль")
        else:
            QApplication.instance().setStyleSheet("")
            self.title_label.setStyleSheet("font-weight: bold;")
            self.style_button.setText("Увімкнути стиль")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

