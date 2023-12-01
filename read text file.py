def read_text_file(file_name):
    try:
        # Attempt to open the file in read ('r') mode
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()
            
            # Print the content to the console
            print(content)
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"File '{file_name}' not found.")
    except Exception as e:
        # Handle other exceptions that might occur during file reading
        print(f"An error occurred: {e}")

# Example: Call the function with the file name
file_name = "read.txt"  # Replace with the actual file name
read_text_file(file_name)
