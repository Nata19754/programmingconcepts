# Come Fly with Me Project
# Created by : Natally Chaves :)
# This project  simulate buying seats on an airplane. The program  validates if a seat is already taken and be able to purchase multiple seats. The program has a first-class section that charges a fee to purchase.  The regular seats will not have a fee to select.  There are only 20 seats on this plane.  The plane has 2 rows of emergency seats.  The user is prompted to accept responsibility for being able to help in-case of emergency, if the user selects those seats


FIRST_CLASS_FEE = 100.00
TOTAL_SEATS = 20


class Seat:
    def __init__(self, number, seat_type="regular", is_emergency=False):
        self.number = number
        self.seat_type = seat_type
        self.is_emergency = is_emergency
        self.is_taken = False

    def fee(self):
        # First-class seats cost extra
        if self.seat_type == "first":
            return FIRST_CLASS_FEE
        return 0.0


class Airplane:
    def __init__(self):
        self.seats = []
        # Build all 20 seats
        for n in range(1, TOTAL_SEATS + 1):
            if 1 <= n <= 4:
                seat_type = "first"     # first-class section
            else:
                seat_type = "regular"

            is_emergency = 9 <= n <= 12  # emergency rows
            self.seats.append(Seat(n, seat_type, is_emergency))

    def show_seats(self):
        # Display seat availability
        print("\nSeat map (O=open, X=taken)")
        for seat in self.seats:
            mark = "X" if seat.is_taken else "O"
            print(f"{seat.number}:{mark}", end="  ")
            if seat.number % 5 == 0:
                print()
        print()

    def get_seat(self, number):
        # Return a seat object by number
        if 1 <= number <= TOTAL_SEATS:
            return self.seats[number - 1]
        return None


def confirm_emergency():
    # Emergency seats require confirmation
    print("You chose an emergency exit seat.")
    while True:
        ans = input("Do you accept the responsibility? (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please enter y or n.")


def main():
    plane = Airplane()
    total_fee = 0.0

    print("Welcome to the Come Fly With Me program.")

    while True:
        plane.show_seats()
        choice = input("Pick a seat number (1-20) or q to quit: ").strip()

        if choice.lower() == "q":
            break

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        number = int(choice)
        seat = plane.get_seat(number)

        if seat is None:
            print("Seat does not exist.")
            continue

        if seat.is_taken:
            print("Seat already taken.")
            continue

        if seat.is_emergency:
            if not confirm_emergency():
                print("Seat not assigned.")
                continue

        # Assign seat
        seat.is_taken = True
        fee = seat.fee()
        total_fee += fee

        if fee > 0:
            print(f"First-class seat. Fee: ${fee:.2f}")
        else:
            print("Regular seat. No fee.")

        more = input("Buy another seat? (y/n): ").strip().lower()
        if more not in ("y", "yes"):
            break

    print("\nPurchase complete.")
    print(f"Total fees: ${total_fee:.2f}")


if __name__ == "__main__":
    main()
