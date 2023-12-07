# Author: Rayon Foster, 20231888
# Date Created: 07/12/2023
# Course: ITT103
# Purpose: This program implements an automated reservation system for UCC Signature Express Limited's new luxury executive coach buses, offering first-class, business-class, and economy-class traveling options.

# Initialize constants for bus capacities
FIRST_CLASS_CAPACITY = 27
BUSINESS_CLASS_CAPACITY = 38
ECONOMY_CLASS_CAPACITY = 56

# Initialize 2D array to represent seat reservations
first_class_seats = [[0] * 2 for _ in range(FIRST_CLASS_CAPACITY)]
business_class_seats = [[0] * 2 for _ in range(BUSINESS_CLASS_CAPACITY)]
economy_class_seats = [[0] * 2 for _ in range(ECONOMY_CLASS_CAPACITY)]

# Function to display the reservation menu
def display_menu():
    print("UCC Signature Express Limited")
    print("Take the journey, enjoy the ride")
    print("Reservation Options:")
    print("First Class (F/f)")
    print("Business Class (B/b)")
    print("Economy Class (E/e)")
    print("Quit or Cancel (Q/q)")
    print("Please select an option:")

# Function to reserve a seat
def reserve_seat(seat_type, seat_array):
    row = int(input("Enter row number: "))
    column = int(input("Enter column number (1 for window, 2 for aisle): "))

    if row <= 0:
        print("Number must be positive or greater than zero!")
        return

    if seat_array[row - 1][column - 1] == 1:
        print("Seat already reserved!")
        return

    seat_array[row - 1][column - 1] = 1
    print(f"Reserving seat: row {row} column {column:02}")

# Function to calculate and print reservation statistics
def print_reservation_stats(seat_type, seat_array):
    total_seats = len(seat_array)
    reserved_seats = sum(sum(row) for row in seat_array)
    print(f"Reservation Type: {seat_type} Class")
    print(f"Total number of seats: {total_seats}")
    print(f"Total number of seats reserved: {reserved_seats}")

# Main program
while True:
    display_menu()
    user_choice = input().lower()

    if user_choice == 'q':
        print_reservation_stats("First", first_class_seats)
        print_reservation_stats("Business", business_class_seats)
        print_reservation_stats("Economy", economy_class_seats)
        break

    elif user_choice == 'f':
        reserve_seat("First", first_class_seats)

    elif user_choice == 'b':
        reserve_seat("Business", business_class_seats)

    elif user_choice == 'e':
        reserve_seat("Economy", economy_class_seats)

    else:
        print("Invalid choice!")
