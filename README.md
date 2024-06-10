Train Ticket Booking System
This project implements a simple Train Ticket Booking System using Flask and a MySQL database.

Features:

Book train tickets for available trains.
Cancel existing bookings.
View a list of available trains.
View a list of current bookings.
Fetch train information (name and schedule) from an external website (https://enquiry.indianrail.gov.in/).
Requirements:

Python 3
Flask
mysql-connector-python
requests
beautifulsoup4
Setup:

Clone this repository.
Install required libraries:
Bash
pip install Flask mysql-connector-python requests beautifulsoup4
Use code with caution.
content_copy
Create a MySQL database named train_booking and configure the connection details in TrainTicketBookingSystem.py:
Python
self.conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="train_booking"
        )
Use code with caution.
content_copy
Run the application:
Bash
python app.py
Use code with caution.
content_copy
Usage:

Access the application in your web browser at http://127.0.0.1:5000/ (default Flask development server).
The homepage (/) provides an interface to view available trains and book tickets.
You can fetch train information by entering the train number in the provided form.
Notes:

This is a basic implementation and does not handle real-time ticket booking or integration with payment gateways.
The code fetches train information from an external website. The website structure or data format might change in the future, requiring code modifications.
Contributing:

Feel free to fork this repository and contribute improvements or new features.
