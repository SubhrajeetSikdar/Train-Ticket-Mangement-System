from flask import Flask, render_template, request
import mysql.connector
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

class TrainTicketBookingSystem:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="train_booking"
        )
        self.cursor = self.conn.cursor()
    
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS trains (
                train_id INT AUTO_INCREMENT PRIMARY KEY,
                train_name VARCHAR(100) NOT NULL,
                source VARCHAR(100) NOT NULL,
                destination VARCHAR(100) NOT NULL,
                total_seats INT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                booking_id INT AUTO_INCREMENT PRIMARY KEY,
                train_id INT,
                passenger_name VARCHAR(100) NOT NULL,
                seat_number INT NOT NULL,
                FOREIGN KEY (train_id) REFERENCES trains(train_id)
            )
        """)
        self.conn.commit()
    
    def book_ticket(self, train_id, passenger_name, seat_number):
        try:
            self.cursor.execute("""
                INSERT INTO bookings (train_id, passenger_name, seat_number) 
                VALUES (%s, %s, %s)
            """, (train_id, passenger_name, seat_number))
            self.conn.commit()
            print("Ticket booked successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def cancel_ticket(self, booking_id):
        try:
            self.cursor.execute("""
                DELETE FROM bookings WHERE booking_id = %s
            """, (booking_id,))
            self.conn.commit()
            print("Ticket cancelled successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def display_available_trains(self):
        self.cursor.execute("SELECT * FROM trains")
        result = self.cursor.fetchall()
        if result:
            print("Available Trains:")
            for row in result:
                print(row)
        else:
            print("No trains available.")
    
    def display_bookings(self):
        self.cursor.execute("SELECT * FROM bookings")
        result = self.cursor.fetchall()
        if result:
            print("Bookings:")
            for row in result:
                print(row)
        else:
            print("No bookings yet.")
    
    def fetch_train_info(self, train_number):
        url = f"https://enquiry.indianrail.gov.in/ntes/index.html#/train/{train_number}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            train_name = soup.find('h2', class_='train-name').text.strip()
            schedule_table = soup.find('table', class_='schedule-table')
            rows = schedule_table.find_all('tr')[1:]  # Skipping header row
            schedule = []
            for row in rows:
                cols = row.find_all('td')
                station = cols[1].text.strip()
                arrival = cols[2].text.strip()
                departure = cols[3].text.strip()
                schedule.append((station, arrival, departure))
            return train_name, schedule
        else:
            print("Failed to fetch train information.")

# Initialize the TrainTicketBookingSystem
booking_system = TrainTicketBookingSystem()
booking_system.create_tables()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train_info', methods=['POST'])
def train_info():
    train_number = request.form['train_number']
    train_name, schedule = booking_system.fetch_train_info(train_number)
    return render_template('train_info.html', train_name=train_name, schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)

