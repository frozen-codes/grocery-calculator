# grocery-calculator
Project Description: Grocery Calculator App
Overview
The Grocery Calculator App is a Python-based command-line application designed to simplify and automate calculations for small grocery shop owners. It allows users to store product prices, calculate quantities based on customer requests, and generate receipts for transactions. This lightweight and user-friendly tool eliminates the need for manual calculations, making it ideal for local grocery shops.

Key Features
Product Management: Add, edit, and remove products with their prices and units (e.g., per kg or per packet).

Automatic Calculations: Calculate the quantity of a product based on the customer’s requested amount.

Receipt Generation: Generate and save receipts for transactions in a text file.

Local Data Storage: All data (products and receipts) is stored locally for easy access and persistence.

User-Friendly Interface: Interactive command-line interface powered by the rich library for a visually appealing experience.

How It Works
Product Management: Users can add, edit, or remove products through the app’s menu.

Transaction Processing: Users enter the product name and the customer’s requested amount, and the app calculates the quantity to be given.

Receipt Generation: Users can add multiple items to a transaction, and the app generates a receipt with itemized details.

Data Persistence: All data is stored locally, ensuring it is available even after the app is closed.

Technical Details
Programming Language: Python

Libraries Used:

rich: For a visually enhanced command-line interface.

json: For storing and retrieving product data.

os: For file and folder management.

File Structure:

Copy
grocery-calculator/
├── data/
│   ├── items.json         # Stores product data
│   └── receipts/          # Stores generated receipts
├── src/
│   ├── item_manager.py    # Handles product CRUD operations
│   ├── calculator.py      # Core calculation logic
│   ├── receipt_handler.py # Generates and saves receipts
│   └── main.py            # Main CLI interface
└── requirements.txt       # Lists project dependencies
How to Run
Clone the repository:

bash
Copy
git clone https://github.com/your-username/grocery-calculator.git
Install dependencies:

bash
Copy
pip install -r requirements.txt
Run the app:

bash
Copy
python src/main.py
Future Enhancements
Graphical User Interface (GUI): Develop a desktop or mobile app with a graphical interface.

Barcode Scanning: Integrate barcode scanning to automatically fetch product details.

Inventory Management: Track stock levels and generate low-stock alerts.

Data Export: Allow users to export transaction data to Excel or CSV.

License
This project is licensed under the MIT License. See the LICENSE file for details.


