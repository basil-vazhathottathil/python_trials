# Global Variables
total_tickets = 0
discount = False
total_cost = 0


def movie_availability():
    movies = ['Action', 'Comedy', 'Horror', 'Romantic']
    print('Available Movies\n 1. Action \n 2. Comedy \n 3. Horror \n 4. Romantic')
    movie_no = int(input('Enter the movie number: ')) - 1

    if movie_no in range(0, 4):
        print('Movie Selected:', movies[movie_no])
    else:
        print('Invalid Movie Number')
        movie_availability()


def show_timings():
    timings = ['10:00 AM', '1:00 PM', '4:00 PM', '7:00 PM', '10:00 PM']
    print('Available Timings\n 1. 10:00 AM \n 2. 1:00 PM \n 3. 4:00 PM \n 4. 7:00 PM \n 5. 10:00 PM')
    timing_no = int(input('Enter the timing number: ')) - 1

    if timing_no in range(0, 5):
        print('Timing Selected:', timings[timing_no])
    else:
        print('Invalid Timing Number')
        show_timings()


def ticket():
    global total_cost 
    print('Enter the type of ticket you want to book \n 1. Normal ($100) \n 2. Premium ($150)')
    ticket_type = int(input('Enter the ticket type (1 or 2): '))

    if ticket_type == 1:
        total_cost += 100
        return 'Normal Ticket'
    elif ticket_type == 2:
        total_cost += 150
        return 'Premium Ticket'
    else:
        print('Invalid Ticket Type')
        return ticket() 


def ticket_count():
    global total_tickets, discount
    total_tickets = int(input('Enter the number of tickets you want to book: '))
    for _ in range(total_tickets):
        ticket_type = ticket()
        print(f"Ticket booked: {ticket_type}")

    if total_tickets > 5:
        discount = True
        print('You are eligible for a discount.')


def calculate_total_cost():
    global total_cost, discount
    if discount:
        total_cost -= total_cost * 0.1
    print('Total Cost:', total_cost)


def main():
    movie_availability()
    show_timings()
    ticket_count()
    calculate_total_cost()

main()
