# Train Ticket Booking System

This project implements a simple Train Ticket Booking System using Flask and a MySQL database.

## Features

- Book train tickets for available trains.
- Cancel existing bookings.
- View a list of available trains.
- View a list of current bookings.
- Fetch train information (name and schedule) from an external website (https://enquiry.indianrail.gov.in/).

## Requirements

- Python 3
- Flask
- mysql-connector-python
- requests
- beautifulsoup4

## Setup

1. Clone this repository.
2. Install required libraries:

```bash
pip install Flask mysql-connector-python requests beautifulsoup4
```

3. Create a MySQL database named train_booking and configure the connection details in TrainTicketBookingSystem.py:
self.conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="train_booking"
        )
4. Run the application:
   python app.py



## Usage
1. Access the application in your web browser at http://127.0.0.1:5000/ (default Flask development server).
2. The homepage (/) provides an interface to view available trains and book tickets.
3. You can fetch train information by entering the train number in the provided form.


## Notes
1. This is a basic implementation and does not handle real-time ticket booking or integration with payment gateways.
2. The code fetches train information from an external website. The website structure or data format might change in the future, requiring code modifications.


## Contributing
Feel free to fork this repository and contribute improvements or new features.

This markdown document provides a structured overview of the Train Ticket Booking System project, including its features, requirements, setup instructions, usage guidelines, notes, and contribution guidelines.



