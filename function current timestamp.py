import os
from datetime import datetime

def create_text_file():
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Define the file name with the timestamp
    file_name = f"text_file_{timestamp}.txt"

    # Create and open the text file in write mode
    with open(file_name, 'w') as file:
        file.write("This is a text file created at: " + timestamp)

    print(f"Text file '{file_name}' has been created.")

# Call the function to create the text file
create_text_file()
