# Arstotzka Shipment Services

## Overview
Arstotzka Shipment Services is a desktop application designed to streamline the process of managing shipments for both customers and employees. Built with Python, Tkinter, PIL, and MySQL, this application offers a user-friendly interface for submitting and viewing shipment orders.

## Features
- **Customer Interface:** Allows customers to submit shipment orders by providing details such as name, company, goods type, weight, destination, and description.
- **Employee Interface:** Employees can view and manage submitted orders, including details on category, location, weight, the customer who placed the order, and order description.
- **Database Integration:** Utilizes MySQL for storing and managing orders, ensuring data persistence and reliability.

## Images 
![Screenshot 2023-02-18 at 12 25 29 PM](https://github.com/NemoPatel/Ports_Project/assets/126904097/c8442ce7-f05f-473b-8da4-c6381d0d577c)
![Screenshot 2023-02-18 at 12 27 23 PM](https://github.com/NemoPatel/Ports_Project/assets/126904097/7214dc3b-2eda-45b0-beaf-4e7788752ca6)
![Screenshot 2023-02-18 at 12 27 30 PM](https://github.com/NemoPatel/Ports_Project/assets/126904097/f95daf99-2f70-4258-8db6-a9eeef108b72)
![Screenshot 2023-02-18 at 12 27 36 PM](https://github.com/NemoPatel/Ports_Project/assets/126904097/76a531a9-20e7-4805-809f-8992a100d4c7)
![Screenshot 2023-02-18 at 12 27 42 PM](https://github.com/NemoPatel/Ports_Project/assets/126904097/81f9cca9-fd87-4dfb-8ad5-7c09d82936d4)
![Screenshot 2023-02-18 at 12 27 47 PM](https://github.com/NemoPatel/Ports_Project/assets/126904097/2c2c4de5-10fc-4f36-823e-7a1dd72d439d)



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
