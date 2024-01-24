from PySide6 import QtWidgets, QtGui, QtCore
import currency_converter

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Currency Converter")
        self.setup_ui()
        self.setup_connections()
        self.set_default_values()
        self.setup_css()
        self.resize(500, 50)

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_currencies_from = QtWidgets.QComboBox()
        self.le_amount = QtWidgets.QSpinBox()
        self.cbb_currencies_to = QtWidgets.QComboBox()
        self.le_converted_amount = QtWidgets.QSpinBox()
        self.btn_swap_currencies = QtWidgets.QPushButton("Swap Currencies")

        self.layout.addWidget(self.cbb_currencies_from)
        self.layout.addWidget(self.le_amount)
        self.layout.addWidget(self.cbb_currencies_to)
        self.layout.addWidget(self.le_converted_amount)
        self.layout.addWidget(self.btn_swap_currencies)
    
    def setup_connections(self):
        self.cbb_currencies_from.activated.connect(self.compute)
        self.cbb_currencies_to.activated.connect(self.compute)
        self.le_amount.valueChanged.connect(self.compute)
        self.btn_swap_currencies.clicked.connect(self.swap_currencies)

    def setup_css(self):
        self.setStyleSheet("""
        background-color: rgb(30, 30, 30);
        color: rgb(240, 240, 240);
        border: none;
        """)
        style = """
        QComboBox::down-arrow {
            image: none;
            border-width: 0px;
        }
        QComboBox::drop-down {
            border-width: 0px;
        } 
        """
        self.cbb_currencies_from.setStyleSheet(style)
        self.cbb_currencies_to.setStyleSheet(style)

    def set_default_values(self):
        self.cbb_currencies_from.addItems(sorted(list(self.c.currencies)))
        self.cbb_currencies_to.addItems(sorted(list(self.c.currencies)))
        self.cbb_currencies_from.setCurrentText("EUR")
        self.cbb_currencies_to.setCurrentText("EUR")
        self.le_amount.setValue(100)
        self.le_converted_amount.setValue(100)
        self.le_amount.setRange(1, 1000000)
        self.le_converted_amount.setRange(1, 1000000)

    def compute(self):
        amount = self.le_amount.value()
        currency_from = self.cbb_currencies_from.currentText()
        currency_to = self.cbb_currencies_to.currentText()

        try:
            result = self.c.convert(amount, currency_from, currency_to)
        except currency_converter.currency_converter.RateNotFoundError:
            print("Rate not found")
        else:
            self.le_converted_amount.setValue(result)

    def swap_currencies(self):
        currency_from = self.cbb_currencies_from.currentText()
        currency_to = self.cbb_currencies_to.currentText()

        self.cbb_currencies_from.setCurrentText(currency_to)
        self.cbb_currencies_to.setCurrentText(currency_from)
        self.compute()

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
