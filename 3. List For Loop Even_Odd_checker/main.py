count = 0

start = False

while count < 5 or not start:
    user_input = input("Enter 'start' to begin or 'exit' to quit: ").strip().lower()
    
    if user_input == 'start':
      start = True
      print("Starting the process...")
    elif user_input == 'exit':
      print("Exiting the program.")
      break
    else:
      print("Invalid input. Please try again.")
    
    count += 1
  
  
  