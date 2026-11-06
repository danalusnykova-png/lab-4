
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QComboBox, QCheckBox, QSpinBox,
    QVBoxLayout, QHBoxLayout, QFormLayout,
    QMessageBox
)


class StudentForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Інтерактивна форма студента")
        self.setMinimumSize(450, 350)

        main_layout = QVBoxLayout()

        title = QLabel("Введення даних студента")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(title)

        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введіть ім'я")
        form_layout.addRow("Ім'я:", self.name_input)

        self.subject_box = QComboBox()
        self.subject_box.addItems([
            "Математика", "Фізика", "Програмування"
        ])
        form_layout.addRow("Предмет:", self.subject_box)

        self.grade_spin = QSpinBox()
        self.grade_spin.setRange(0, 100)
        self.grade_spin.setValue(75)
        form_layout.addRow("Оцінка:", self.grade_spin)

        main_layout.addLayout(form_layout)

        self.checkbox = QCheckBox("Підтверджую правильність даних")
        main_layout.addWidget(self.checkbox)

        self.preview_label = QLabel("Студент: не вказано")
        main_layout.addWidget(self.preview_label)

        self.grade_label = QLabel("Поточна оцінка: 75")
        main_layout.addWidget(self.grade_label)

        button_layout = QHBoxLayout()

        self.save_button = QPushButton("Підтвердити")
        self.save_button.setEnabled(False)
        button_layout.addWidget(self.save_button)

        self.reset_button = QPushButton("Скинути")
        button_layout.addWidget(self.reset_button)

        main_layout.addLayout(button_layout)

        self.result_label = QLabel("Заповніть форму")
        self.result_label.setWordWrap(True)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

        self.name_input.textChanged.connect(self.update_preview)
        self.subject_box.currentTextChanged.connect(self.update_preview)

        self.grade_spin.valueChanged.connect(
            lambda value: self.grade_label.setText(
                f"Поточна оцінка: {value}"
            )
        )

        self.checkbox.toggled.connect(self.save_button.setEnabled)

        self.save_button.clicked.connect(self.save_data)
        self.reset_button.clicked.connect(self.reset_form)

    def update_preview(self):
        name = self.name_input.text().strip()
        subject = self.subject_box.currentText()

        if name:
            self.preview_label.setText(
                f"Студент: {name}, предмет: {subject}"
            )
        else:
            self.preview_label.setText("Студент: не вказано")

    def validate_data(self):
        name = self.name_input.text().strip()
        grade = self.grade_spin.value()

        if not name:
            return "Введіть ім'я студента"

        if grade < 1 or grade > 100:
            return "Оцінка повинна бути від 1 до 100"

        return None

    def save_data(self):
        error = self.validate_data()

        if error:
            QMessageBox.warning(self, "Помилка", error)
            self.result_label.setText("Дані введено неправильно")
            return

        name = self.name_input.text().strip()
        subject = self.subject_box.currentText()
        grade = self.grade_spin.value()

        self.result_label.setText(
            f"Збережено: {name}, {subject}, {grade} балів"
        )

        QMessageBox.information(
            self,
            "Успішно",
            "Дані студента підтверджено!"
        )

    def reset_form(self):
        self.name_input.clear()
        self.subject_box.setCurrentIndex(0)
        self.grade_spin.setValue(75)
        self.checkbox.setChecked(False)
        self.preview_label.setText("Студент: не вказано")
        self.grade_label.setText("Поточна оцінка: 75")
        self.result_label.setText("Заповніть форму")


def main():
    app = QApplication(sys.argv)
    window = StudentForm()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

