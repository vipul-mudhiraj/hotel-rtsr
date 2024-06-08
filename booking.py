def book_room(user_id):
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    
    room_id = int(input('Enter room ID to book: '))
    check_in_date = input('Enter check-in date (YYYY-MM-DD): ')
    check_out_date = input('Enter check-out date (YYYY-MM-DD): ')
    
    cursor.execute('INSERT INTO bookings (user_id, room_id, check_in_date, check_out_date) VALUES (?, ?, ?, ?)',
                   (user_id, room_id, check_in_date, check_out_date))
    cursor.execute('UPDATE rooms SET status = "occupied" WHERE room_id = ?', (room_id,))
    conn.commit()
    conn.close()
    print('Room booked successfully!')

def view_bookings(user_id):
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM bookings WHERE user_id = ?', (user_id,))
    bookings = cursor.fetchall()
    
    for booking in bookings:
        print(f'Booking ID: {booking[0]}, Room ID: {booking[2]}, Check-in: {booking[3]}, Check-out: {booking[4]}')
    
    conn.close()

# Example usage
book_room(user_id)
view_bookings(user_id)