import gspread

# from oauth2client.service_account import ServiceAccountCredentials

 

def print_character_grid(doc_url):
    # Set up the credentials and authorize the client
    gc = gspread.service_account(filename="C:/Users/dawso/OneDrive/Desktop/Desktop Folder/Code/service-account.json")
    sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/19grv9wlcumBafPCJMZhZAV0NUOZxI1aLxzSqIXeX7h4/edit?gid=0#gid=0")

    # Fetch the worksheet from google sheet
    worksheet = sheet.get_worksheet(0)
    records = worksheet.get_all_records()

    # Get max coordinate
    max_x = max(item['x-coordinate'] for item in records )+1
    max_y = max(item['y-coordinate'] for item in records )+1

    
    # Create the grid initialized with spaces
    grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]

    for item in records:
        x = item['x-coordinate']
        y = item['y-coordinate']
        char = item['Character']
        grid[y][x] = char

    # Print the grid

    for row in grid:
        print(''.join(row))

def main():
    print_character_grid("https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub")

main()

