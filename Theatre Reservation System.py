print('Welcome to XYZ Cinemas. This is a user-driven theatre reservation program.')
print('Please follow the instructions to avoid errors.', end='\n')
print('There are no pre-programmed movies. Administrator must add movies before the customer can book tickets')
movies = {}

def displaySeatChart(movieKey):
    seats = []
    seatRow = "ABCDEFGHIJ"
    print('''\n\n----------------------------------SCREEN-----------------------------------\n\n''')
    for i in range(9):
        row= []
        for j in range(10):
            seatStr = seatRow[i]+str(j+1)
            row.append([seatStr])
        count = 1
        for k in row:
            if k[0]in movies[movieKey]['seats']:
                k=['##']
        
            if count==3 or count==7:
                print(k, end='\t')
            else:
                print(k, end='')
            count+=1
        print()
        seats.append(row)
    print()

utilityChoice = 1

while utilityChoice:
    print('\n1. Book Ticket')
    print('2. Print Ticket')
    print('3. Change Booking')
    print('4. Cancel Ticket')
    print('5. Authorized Access (Add Movie, Display All Data)')
    print('0. Exit Program')
    utilityChoice = input('Enter your choice(1/2/3/4/5/0): ')
    print()
    
    if utilityChoice=='1':
        
        for movieKey in movies:
            print(movies[movieKey]['name'], ' Movie Code: ', movieKey)
        print()
        movieKey = input('Enter movie code: ').upper()
        print()        
                
        popcorn = input('What popcorn would you like to have, sweet, salty or none? (SW, SA, NO)').upper()
        print()
        if popcorn == 'SA':
            movies[movieKey]['popcorn?'].append('Salty')
        elif popcorn == 'SW':
            movies[movieKey]['popcorn?'].append('Sweet')
        else:
            movies[movieKey]['popcorn?'].append('None')

        print('Choose your seat from the seat chart below. Booked Seats are marked with ##')
        displaySeatChart(movieKey)
        seatChoice = input('Enter your seat choice: ').upper()
        print()
        if seatChoice in movies[movieKey]['seats']:
            print('Seat already booked. Please go through booking process again.')
            continue
        elif seatChoice[0] in 'ABCDEFGHI' and (1<=int(seatChoice[1:])<=10):
            movies[movieKey]['seats'].append(seatChoice)
        else:
            print('Seat Number Invalid. Please go through booking process again.')
            continue

        if len(movies[movieKey]['tickets']) == 90:
            print('Sorry, Movie is full.')
        else:
            ticketID = movieKey + seatChoice
        print('Ticket ID: ', ticketID, end='\n')
        movies[movieKey]['tickets'].append(ticketID)        

    elif utilityChoice=='2':
        tickID = input('Enter your Ticket ID: ').upper()
        print()
        if tickID in movies[tickID[:3]]['tickets']:
            movName = movies[tickID[:3]]['name']
            index = movies[tickID[:3]]['tickets'].index(tickID)
            screenNO = movies[tickID[:3]]['screen']
            seatNO = movies[tickID[:3]]['seats'][index]
            popcorn = movies[tickID[:3]]['popcorn?'][index]
            if popcorn=='Sweet'or popcorn=='Salty':
                popcornText = 'Popcorn will be served directly to you seat.\n'
            else:
                popcornText = ''
            lines = [
                '-------------------------------------------------------------\n',
                '                         XYZ Cinemas\n',
                '-------------------------------------------------------------\n',
                '                                123, ABC Road,\n',
                '                                Singanallur,\n',
                '                                Coimbatore\n',
                '-------------------------------------------------------------\n',
                'Email  :  xyzcinemas@gmail.com\n',
                'Phone  :  0422-1234567\n',
                'Branch : Coimbatore\n',
                '-------------------------------------------------------------\n',
                '\n',
                'Movie Ticket for '+movName+'\n',
                'Screen Number : '+str(screenNO)+'\n',
                'Seat Number   : '+str(seatNO)+'\n',
                'Ticket ID     : '+tickID+'\n',
                'Popcorn       : '+popcorn+'\n',
                popcornText+'\n',
                '\n',
                '-------------------------------------------------------------\n',
                '                         THANK YOU\n'
                ]

            fileName = tickID+'_Ticket_Print.txt'
            ticketFile = open(fileName, 'w')
            ticketFile.writelines(lines)
            ticketFile.close()

            print('Ticket has been printed at the same location of this program as a .txt file.')

        else:
            print('Ticket N/A')

    elif utilityChoice=='3':
        tickID = input('Enter your Ticket ID: ').upper()
        print()
        print('1. Modify Seat')
        print('2. Modify Popcorn')
        modifyChoice = input('Enter your choice: ')
        print()
        index = movies[tickID[:3]]['tickets'].index(tickID)
        if modifyChoice == '1':
            previousSeat = movies[tickID[:3]]['seats'][index]
            displaySeatChart(tickID[:3])
            print('Your previous seat choice was ', previousSeat)
            newSeat = input('Enter your new seat choice: ').upper()
            print()
            newTickID = tickID[:3]+newSeat
            print('Your ticket ID has been updated to: ', newTickID)
            movies[tickID[:3]]['seats'][index] = newSeat
            movies[tickID[:3]]['tickets'][index] = newTickID
        elif modifyChoice == '2':
            previousPopcorn = movies[tickID[:3]]['popcorn?'][index]
            print('Your previous popcorn choice was ', previousPopcorn)
            newPopcorn = input('Enter your new popcorn choice(SW, SA, NO): ').upper()
            print()
            if newPopcorn == 'SA':
                movies[movieKey]['popcorn?'].append('Salty')
            elif newPopcorn == 'SW':
                movies[movieKey]['popcorn?'].append('Sweet')
            else:
                movies[movieKey]['popcorn?'].append('None')
            
    elif utilityChoice=='4':
        tickID = input('Enter your Ticket ID: ').upper()
        print()
        cancelString = 'To cancel your ticket, please type Y (Note: This action cannot be undone): '
        cancel = input(cancelString).upper()
        print()
        if cancel=='Y':
            index = movies[tickID[:3]]['tickets'].index(tickID)
            movies[tickID[:3]]['tickets'].pop(index)
            movies[tickID[:3]]['popcorn?'].pop(index)
            movies[tickID[:3]]['seats'].pop(index)
        print('Your ticket has been cancelled.')

    elif utilityChoice=='5':
        print('Only administrators can access. Please enter administrator password.')
        password = input('Enter password: ')
        print()
        if password=='admin135':
            adminChoice = 1
            while adminChoice:
                print('1. Add Movie')
                print('2. Modify Movie')
                print('3. Delete a Movie')
                print('4. Display All Data for a Movie')
                print('5. Display All Data for All Movies')
                print('0. Logout from Administrator Interface')
                adminChoice = input('Enter your choice(1/2/3/4/5/0): ')
                print()

                if adminChoice=='1':
                    movieKey = input('Enter Movie Code(3 Characters in CAPS) (eg. ABC): ').upper()
                    print()
                    movies[movieKey] = {}
                    movies[movieKey]['name'] = input('Enter Movie Name: ')
                    print()
                    movies[movieKey]['screen'] = int(input('Enter Screen Number: '))
                    print()
                    movies[movieKey]['tickets'] = []
                    movies[movieKey]['popcorn?'] = []
                    movies[movieKey]['seats'] = []

                elif adminChoice=='2':
                    movieKey = input('Enter Movie Code to Modify: ').upper()
                    print()
                    print('1. Modify Movie Name')
                    print('2. Modify Movie Screen')
                    print('3. Modify Movie Name and Screen')
                    modChoice = input('Enter your choice(1/2/3): ')
                    print()
                    if modChoice=='1':
                        print('Previous name: ', movies[movieKey]['name'])
                        movies[movieKey]['name'] = input('Enter new Name: ')
                        print()
                    elif modChoice=='2':
                        print('Previous screen: ', movies[movieKey]['screen'])
                        movies[movieKey]['screen'] = int(input('Enter new Screen No: '))
                        print()
                    elif modChoice=='3':
                        print('Previous name: ', movies[movieKey]['name'])
                        movies[movieKey]['name'] = input('Enter new Name: ')
                        print()
                        print('Previous screen: ', movies[movieKey]['screen'])
                        movies[movieKey]['screen'] = int(input('Enter new Screen No: '))
                        print()

                elif adminChoice=='3':
                    for movieKey in movies:
                        print(movies[movieKey]['name'], ' Movie Code: ', movieKey)
                    print()
                    movieKey = input('Enter Movie Code to Delete: ').upper()
                    print()
                    movieKeyConfirm = input('Enter Movie Code again to confirm the delete (This action cannot be undone): ')
                    if movieKeyConfirm==movieKey:
                        del movies[movieKey]
                        print('The movie with code: ', movieKey, ' has been deleted.')
                    else:
                        print('The codes you have entered do not match. Please try again.')

                elif adminChoice=='4':
                    for movieKey in movies:
                        print(movies[movieKey]['name'], ' Movie Code: ', movieKey)
                    print()
                    movieKey = input('Enter movie code: ').upper()
                    print()
                    print('Movie Name: ', movies[movieKey]['name'])
                    print('Movie Screen Number: ', movies[movieKey]['screen'])
                    print()
                    print('Ticket IDs\tPopcorn?\tSeat Number')
                    for indexes in range(len(movies[movieKey]['tickets'])):
                        print(str(movies[movieKey]['tickets'][indexes]).center(9), '\t', \
                              movies[movieKey]['popcorn?'][indexes].center(8), '\t', \
                              movies[movieKey]['seats'][indexes].center(11))
                    print()
                    print('Seat Chart (## denotes Seat Booked)'.center(75))
                    displaySeatChart(movieKey)
                    print()

                elif adminChoice=='5':
                    for movieKey in movies:
                        pauseVariable = input('Press enter for next movie: ')
                        print()
                        print('Movie Name: ', movies[movieKey]['name'])
                        print('Movie Screen Number: ', movies[movieKey]['screen'])
                        print()
                        print('Ticket IDs\tPopcorn?\tSeat Number')
                        for indexes in range(len(movies[movieKey]['tickets'])):
                            print(str(movies[movieKey]['tickets'][indexes]).center(9), '\t', \
                                  movies[movieKey]['popcorn?'][indexes].center(8), '\t', \
                                  movies[movieKey]['seats'][indexes].center(11))
                        print()
                        print('Seat Chart (## denotes Seat Booked)'.center(75))
                        displaySeatChart(movieKey)
                        print()

                elif adminChoice=='0':
                    print()
                    break

                else:
                    print('Please enter valid choice.')
        else:
            print('Incorrect Password.')

    elif utilityChoice=='0':
        print('Thank you for using our platform. We hope you will visit again.')
        break

    else:
        print('Please enter valid choice.')
