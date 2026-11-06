import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QTextEdit, QComboBox,
    QCheckBox, QRadioButton, QSpinBox,
    QVBoxLayout, QHBoxLayout, QFormLayout
)


class StudentWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Інформація про студента")
        self.setMinimumSize(450, 450)

        main_layout = QVBoxLayout()

        title = QLabel("Форма студента")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(title)

        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введіть ім'я студента")
        form_layout.addRow("Ім'я:", self.name_input)

        self.subject_box = QComboBox()
        self.subject_box.addItems([
            "Математика", "Фізика", "Програмування"
        ])
        self.subject_box.setToolTip("Оберіть предмет")
        form_layout.addRow("Предмет:", self.subject_box)

        self.grade_spin = QSpinBox()
        self.grade_spin.setRange(0, 100)
        self.grade_spin.setValue(75)
        form_layout.addRow("Оцінка:", self.grade_spin)

        self.comment_input = QTextEdit()
        self.comment_input.setPlaceholderText("Додаткова інформація")
        self.comment_input.setMaximumHeight(90)
        form_layout.addRow("Коментар:", self.comment_input)

        main_layout.addLayout(form_layout)

        self.checkbox = QCheckBox("Студент відвідує заняття")
        self.checkbox.setChecked(True)
        main_layout.addWidget(self.checkbox)

        self.radio = QRadioButton("Денна форма навчання")
        self.radio.setChecked(True)
        main_layout.addWidget(self.radio)

        button_layout = QHBoxLayout()

        self.save_button = QPushButton("Зберегти")
        self.save_button.setToolTip("Збереження інформації")
        button_layout.addWidget(self.save_button)

        self.clear_button = QPushButton("Очистити")
        self.clear_button.setToolTip("Очищення форми")
        button_layout.addWidget(self.clear_button)

        main_layout.addLayout(button_layout)

        self.result_label = QLabel("Форма готова до заповнення")
        self.result_label.setWordWrap(True)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)


def main():
    app = QApplication(sys.argv)
    window = StudentWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

