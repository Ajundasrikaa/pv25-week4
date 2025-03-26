import sys
from PyQt5 import QtWidgets, QtGui

class POSApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POS Application_F1D022108")
        self.setGeometry(100, 100, 400, 250)
        self.setStyleSheet("background-color: #f0f8ff;")  
        
        self.products = {
            "Bimoli (Rp. 20,000)": 20000,
            "Beras 5 Kg (Rp. 75,000)": 75000,
            "Kecap ABC (Rp. 7,000)": 7000,
            "Saos Saset (Rp. 2,500)": 2500
        }
        
        layout = QtWidgets.QGridLayout()
        
        label_product = QtWidgets.QLabel("Product")
        self.comboBox_product = QtWidgets.QComboBox(self)
        self.comboBox_product.addItem("")  
        self.comboBox_product.addItems(self.products.keys())
        self.comboBox_product.setStyleSheet("background-color: white; border: 2px solid #4682b4; padding: 5px; border-radius: 5px;")
        
        layout.addWidget(label_product, 0, 0, 1, 1)  
        layout.addWidget(self.comboBox_product, 0, 1, 1, 2)  
        
        label_quantity = QtWidgets.QLabel("Quantity")
        self.lineEdit_quantity = QtWidgets.QLineEdit(self)
        self.lineEdit_quantity.setStyleSheet("border: 2px solid #4682b4; padding: 5px; border-radius: 5px;")
        
        layout.addWidget(label_quantity, 1, 0, 1, 1)
        layout.addWidget(self.lineEdit_quantity, 1, 1, 1, 2)  
        
        label_discount = QtWidgets.QLabel("Discount")
        self.comboBox_discount = QtWidgets.QComboBox(self)
        self.comboBox_discount.addItems(["0%", "5%", "10%", "20%"])
        self.comboBox_discount.setStyleSheet("background-color: white; border: 2px solid #4682b4; padding: 5px; border-radius: 5px;")
        
        layout.addWidget(label_discount, 2, 0, 1, 1)  
        layout.addWidget(self.comboBox_discount, 2, 1, 1, 2)  
        
        self.pushButton_add = QtWidgets.QPushButton("Add to Cart", self)
        self.pushButton_clear = QtWidgets.QPushButton("Clear", self)
        
        self.pushButton_add.setStyleSheet("background-color: #4682b4; color: white; padding: 5px; border-radius: 5px;")
        self.pushButton_clear.setStyleSheet("background-color: #ff6347; color: white; padding: 5px; border-radius: 5px;")
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.pushButton_add)
        button_layout.addWidget(self.pushButton_clear)
        layout.addLayout(button_layout, 3, 0, 1, 3)  
        
        self.listWidget_cart = QtWidgets.QListWidget(self)
        self.listWidget_cart.setStyleSheet("background-color: white; border: 2px solid #4682b4; padding: 5px; border-radius: 5px;")
        layout.addWidget(self.listWidget_cart, 4, 0, 1, 3)
        
        self.label_total = QtWidgets.QLabel("Total: Rp 0", self)
        self.label_total.setStyleSheet("font-weight: bold; color: #4682b4;")
        layout.addWidget(self.label_total, 5, 0, 1, 3)
        
        self.pushButton_add.clicked.connect(self.add_to_cart)
        self.pushButton_clear.clicked.connect(self.clear_fields)
        
        self.comboBox_product.currentIndexChanged.connect(self.reset_fields)

        self.total_price = 0
        self.cart = []
        
        container = QtWidgets.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
    def add_to_cart(self):
        product = self.comboBox_product.currentText()
        quantity = self.lineEdit_quantity.text()
        discount = int(self.comboBox_discount.currentText().replace('%', ''))

        if not product and not quantity:
            self.label_total.setText("Invalid input")
            return

        if not product:
            self.label_total.setText("Invalid input")
            return

        if not quantity.isdigit() or int(quantity) == 0:
            self.label_total.setText("Invalid input")
            return

        quantity = int(quantity)
        unit_price = self.products[product]
        total_price = unit_price * quantity  
        discount_amount = total_price * (discount / 100) 
        final_price = total_price - discount_amount 

        item_text = f"{product} - {quantity} x Rp. {unit_price:,} (disc {discount}%)"
    
        self.cart.append(item_text)
        self.total_price += final_price

       
        self.listWidget_cart.addItem(item_text)
        self.label_total.setText(f"Total: Rp. {self.total_price:,.0f}")
        
    def clear_fields(self):
        self.comboBox_product.setCurrentIndex(0)
        self.lineEdit_quantity.clear()
        self.comboBox_discount.setCurrentIndex(0)
        self.listWidget_cart.clear()
        self.cart.clear()
        self.total_price = 0
        self.label_total.setText("Total: Rp 0")

    def reset_fields(self):
        """Mengosongkan input quantity dan reset discount saat produk dipilih ulang."""
        self.lineEdit_quantity.clear()
        self.comboBox_discount.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = POSApp()
    window.show()
    sys.exit(app.exec_())
