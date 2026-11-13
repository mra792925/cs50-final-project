# bike_store
#### Video Demo: [https://youtu.be/3lLtrBkouUE]
#### Description:

**bike_store** is a web-based e-commerce and inventory management system developed as my final project for CS50. Built by **Ahmed** from Baghdad, Iraq (GitHub: `mra792925`), the application provides a streamlined storefront for browsing and purchasing bicycle parts while maintaining real-time stock accuracy in a relational database.

### Features
- **Product Catalog:** Displays all available bicycle parts along with their prices and current stock quantities dynamically fetched from the database.
- **Real-Time Purchasing & Stock Deduction:** When a user clicks the "Buy" button for an item, the backend verifies that the item is in stock, logs the order, deducts one unit from the inventory, and updates the storefront immediately.
- **Database Persistence & Inventory Utility:** All product, user, and order records are stored persistently in SQLite, accompanied by a standalone Java utility for administrative inventory updates and restocking.

### Project Structure & Files
- **`app.py`**: The core Python backend built with the Flask framework. It manages application routes, handles HTTP requests (`GET` and `POST`), validates inventory availability during purchases, and executes SQL queries against the database.
- **`store.db`**: A SQLite relational database containing structured tables for `users`, `parts`, and `orders` to persist inventory levels and transaction history.
- **`templates/`**: Contains the HTML templates (such as `index.html`) rendered by Flask using Jinja2 syntax to display dynamic product data and interactive purchase forms.
- **`static/`**: Holds the CSS stylesheets used to format the layout, typography, and responsive presentation of the storefront.
- **`InventoryManager.java`** *(or your Java file name)*: A Java command-line utility connected to `store.db` via JDBC, allowing direct administrative restocking and inventory adjustments outside the web interface.

### Design Choices
I chose **Flask** and **SQLite** for the web application because they provide a lightweight, transparent architecture ideal for handling transactional inventory updates without unnecessary overhead. Combining a Python web frontend with a **Java** backend utility allowed me to practice multi-language database integration on a single shared SQLite file.
