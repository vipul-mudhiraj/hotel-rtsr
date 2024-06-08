def add_room():
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    
    room_number = input('Enter room number: ')
    room_type = input('Enter room type: ')
    price = float(input('Enter room price: '))
    status = input('Enter room status (available/occupied): ')
    
    cursor.execute('INSERT INTO rooms (room_number, room_type, price, status) VALUES (?, ?, ?, ?)',
                   (room_number, room_type, price, status))
    conn.commit()
    conn.close()
    print('Room added successfully!')

def view_rooms():
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM rooms')
    rooms = cursor.fetchall()
    
    for room in rooms:
        print(f'Room ID: {room[0]}, Number: {room[1]}, Type: {room[2]}, Price: {room[3]}, Status: {room[4]}')
    
    conn.close()

# Example usage
add_room()
view_rooms()
