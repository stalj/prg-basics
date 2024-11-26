cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    for row in seats:
        for counter in range(len(row)):
            counter += 1  
    return counter * len(row)

def seats_available(seats):
    available = 0
    for row in seats:
        for seat in row:
            if seat == 'A':
                available += 1
    return available

def seats_booked(seats):
    booked = 0
    for row in seats:
        for seat in row:
            if seat == 'B':
                booked += 1
    return booked

def seat_status(seats, row, place):
    if seats[row - 1][place - 1] == 'A':
        return 'This seat is available'
    else:
        return 'This seat is not available'

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))