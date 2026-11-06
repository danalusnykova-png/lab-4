import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QComboBox, QSpinBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QFormLayout,
    QGroupBox
)


class StudentInput(QWidget):
    student_changed = pyqtSignal(str)
    grade_changed = pyqtSignal(int, str)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        group = QGroupBox("Введення даних")
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

        self.reset_button = QPushButton("Скинути дані")
        form.addRow(self.reset_button)

        group.setLayout(form)
        layout.addWidget(group)
        self.setLayout(layout)

        self.name_input.textChanged.connect(
            self.send_student
        )

        self.grade_spin.valueChanged.connect(
            lambda value: self.send_grade()
        )

        self.subject_box.currentTextChanged.connect(
            lambda text: self.send_grade()
        )

        self.reset_button.clicked.connect(self.reset_data)

    def send_student(self, name):
        self.student_changed.emit(name)

    def send_grade(self):
        grade = self.grade_spin.value()
        subject = self.subject_box.currentText()

        self.grade_changed.emit(grade, subject)

    def reset_data(self):
        self.name_input.blockSignals(True)
        self.subject_box.blockSignals(True)
        self.grade_spin.blockSignals(True)

        self.name_input.clear()
        self.subject_box.setCurrentIndex(0)
        self.grade_spin.setValue(75)

        self.name_input.blockSignals(False)
        self.subject_box.blockSignals(False)
        self.grade_spin.blockSignals(False)

        self.student_changed.emit("")
        self.grade_changed.emit(75, "Математика")


class StudentResult(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        group = QGroupBox("Інформація про студента")
        result_layout = QVBoxLayout()

        self.name_label = QLabel("Студент: не вказано")
        self.subject_label = QLabel("Предмет: Математика")
        self.grade_label = QLabel("Оцінка: 75")
        self.status_label = QLabel("Статус: предмет складено")

        result_layout.addWidget(self.name_label)
        result_layout.addWidget(self.subject_label)
        result_layout.addWidget(self.grade_label)
        result_layout.addWidget(self.status_label)

        group.setLayout(result_layout)
        layout.addWidget(group)
        self.setLayout(layout)

    def update_student(self, name):
        if name.strip():
            self.name_label.setText(f"Студент: {name}")
        else:
            self.name_label.setText("Студент: не вказано")

    def update_grade(self, grade, subject):
        self.subject_label.setText(f"Предмет: {subject}")
        self.grade_label.setText(f"Оцінка: {grade}")

        if grade >= 60:
            self.status_label.setText("Статус: предмет складено")
        else:
            self.status_label.setText("Статус: предмет не складено")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Обмін даними між компонентами")
        self.setMinimumSize(650, 300)

        layout = QHBoxLayout()

        self.input_panel = StudentInput()
        self.result_panel = StudentResult()

        layout.addWidget(self.input_panel)
        layout.addWidget(self.result_panel)

        self.setLayout(layout)

        self.input_panel.student_changed.connect(
            self.result_panel.update_student
        )

        self.input_panel.grade_changed.connect(
            self.result_panel.update_grade
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

