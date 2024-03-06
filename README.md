# Arstotzka Shipment Services

## Overview
Arstotzka Shipment Services is a desktop application designed to streamline the process of managing shipments for both customers and employees. Built with Python, Tkinter, PIL, and MySQL, this application offers a user-friendly interface for submitting and viewing shipment orders.

## Features
- **Customer Interface:** Allows customers to submit shipment orders by providing details such as name, company, goods type, weight, destination, and description.
- **Employee Interface:** Employees can view and manage submitted orders, including details on category, location, weight, the customer who placed the order, and order description.
- **Database Integration:** Utilizes MySQL for storing and managing orders, ensuring data persistence and reliability.


### Prerequisites
- Python 3.x
- MySQL Server
- PIL (Python Imaging Library)
- Tkinter (should be included with Python)

### Setup
1. Install Python 3.x from [the official Python website](https://www.python.org/downloads/).
2. Ensure MySQL Server is installed and running on your machine.
3. Install required Python packages:
    ```bash
    pip install pillow mysql-connector-python
    ```
4. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
5. Navigate to the project directory and run the application:
    ```bash
    python port.py
    ```

## Configuration
Before running the application, make sure to configure the MySQL database connection in `port.py` by setting the appropriate `host`, `user`, `password`, and `database` values.

## Usage
Upon launching, the application presents a start screen with options for customers and employees. Customers can submit new orders, while employees can view all orders. Follow the on-screen instructions to navigate through the application.

## Contributing
Contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
