import requests
import random
from bs4 import BeautifulSoup


def scrape_net_worth():
    # Send an HTTP request to the Unacademy website
    page = requests.get('https://unacademy.com/content/general-awareness/list-of-top-15-richest-people-of-the-world-forbes-worlds-billionaires-list/')

    # Parse the HTML data
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the table containing the list of billionaires
    table = soup.find('table')

    # Initialize an empty list to store the data
    data = []

    # Loop through the rows of the table
    for row in table.find_all('tr'):
        # Get the cells in the row
        cells = row.find_all('td')

        # Skip rows that don't have data
        if not cells:
            continue

        # Get the name and net worth from the cells
        name = cells[1].text.strip()
        net_worth = cells[2].text.strip()

        # Add the data to the list
        data.append({'name': name, 'net_worth': net_worth})

    return data


def play_game():
    # Scrape the net worth data
    data = scrape_net_worth()


    while True:
        # Initialize the score and the current person's index
        score = 0
        i = 1  # Start the loop at index 1 to skip the first element

        # Play the game for 5 rounds
        for _ in range(5):
            # Get the current person's name and net worth
            name = data[i]['name']
            real_net_worth_str = data[i]['net_worth']
            real_net_worth = float(real_net_worth_str.replace('Net Worth:', '').replace('$', '').replace('Billion', ''))

            # Generate a random net worth in billions
            random_net_worth = random.uniform(0, 200)

            # Print the current person's name and the random net worth
            print(f'{name}: {random_net_worth:.2f} billion')

            # Prompt the user to guess whether the real net worth is higher or lower
            guess = input('Is the real net worth higher (H) or lower (L)? ')

            # Check if the user guessed correctly
            if guess.upper() == 'H' and real_net_worth > random_net_worth:
                print('########################### You guessed correctly! ###########################')
                score += 1
            elif guess.upper() == 'L' and real_net_worth < random_net_worth:
                print('########################### You guessed correctly! ###########################')
                score += 1
            elif guess.upper() not in ('H', 'L'):
                print('Invalid input. Please type H or L.')
            else:
                print('########################### You guessed incorrectly! ###########################')

            # Increment the current person's index
            i += 1

        # Print the final score
        print(f'------------------- Your final score is {score}. -------------------')

        # Ask the user if they want to play again
        play_again = input('Do you want to play again (Y/N)? ')

        if play_again.upper() == 'N':
            break

# Run the game
play_game()