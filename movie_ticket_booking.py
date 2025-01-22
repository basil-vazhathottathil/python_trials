# Global Variables
total_tickets = 0
discount = False
total_cost = 0


def movie_availability():
    movies = ['Action', 'Comedy', 'Horror', 'Romantic']
    print('Available Movies:')
    for i, movie in enumerate(movies, 1):
        print(f" {i}. {movie}")

    while True:
        try:
            movie_no = int(input('Enter the movie number: ')) - 1
            if 0 <= movie_no < len(movies):
                return movies[movie_no]
            else:
                print('Invalid Movie Number. Try again.')
        except ValueError:
            print('Please enter a valid number.')


def show_timings():
    timings = ['10:00 AM', '1:00 PM', '4:00 PM', '7:00 PM', '10:00 PM']
    print('Available Timings:')
    for i, timing in enumerate(timings, 1):
        print(f" {i}. {timing}")

    while True:
        try:
            timing_no = int(input('Enter the timing number: ')) - 1
            if 0 <= timing_no < len(timings):
                return timings[timing_no]
            else:
                print('Invalid Timing Number. Try again.')
        except ValueError:
            print('Please enter a valid number.')


def ticket():
    global total_cost
    while True:
        print('Enter the type of ticket you want to book:')
        print(' 1. Normal (Rs 100)')
        print(' 2. Premium (Rs 150)')
        try:
            ticket_type = int(input('Enter the ticket type (1 or 2): '))
            if ticket_type == 1:
                total_cost += 100
                return 'Normal Ticket'
            elif ticket_type == 2:
                total_cost += 150
                return 'Premium Ticket'
            else:
                print('Invalid Ticket Type. Try again.')
        except ValueError:
            print('Please enter a valid number.')


def ticket_count():
    global total_tickets, discount
    while True:
        try:
            total_tickets = int(input('Enter the number of tickets you want to book: '))
            if total_tickets > 0:
                break
            else:
                print('The number of tickets must be at least 1.')
        except ValueError:
            print('Please enter a valid number.')

    for _ in range(total_tickets):
        ticket_type = ticket()
        print(f"Ticket booked: {ticket_type}")

    if total_tickets > 5:
        discount = True
        print('You are eligible for a discount.')


def print_ticket(movie, timing, total_tickets, total_cost, discount):
    print('\n----- Your Ticket -----')
    ticket_block = f"""
    Movie: {movie}
    Timing: {timing}
    Total Tickets: {total_tickets}
    Discount: {'Yes' if discount else 'No'}
    Total Cost: Rs {total_cost:.2f}
    """
    print(ticket_block.strip())


def main():
    movie = movie_availability()
    timing = show_timings()
    ticket_count()
    # Apply discount if eligible
    if discount:
        global total_cost
        total_cost *= 0.9
    print_ticket(movie, timing, total_tickets, total_cost, discount)

main()