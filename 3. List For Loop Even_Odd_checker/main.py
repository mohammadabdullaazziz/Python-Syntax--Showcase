# count = 0

# start = False

# while count < 5 or not start:
#     user_input = input("Enter 'start' to begin or 'exit' to quit: ").strip().lower()
    
#     if user_input == 'start':
#       start = True
#       print("Starting the process...")
#     elif user_input == 'exit':
#       print("Exiting the program.")
#       break
#     else:
#       print("Invalid input. Please try again.")
    
#     count += 1
  
  

# A list containing random numbers
numbers = [12, 35, 7, 44, 56, 89, 90, 23, 11, 40]

# Loop through each number in the list
for num in numbers:
    # Check if the number is even using the modulus operator
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

১. প্রথম ইটারেশন (num = 12):

পাইথন লিস্ট থেকে প্রথম মান 12 নিয়ে num ভেরিয়েবলে রাখল।

শর্ত চেক করা হলো: if 12 % 2 == 0: (১২ কে ২ দিয়ে ভাগ করলে ভাগশেষ ০ হয়)।

শর্তটি সত্য (True)।

আউটপুট: 12 is even

২. দ্বিতীয় ইটারেশন (num = 35):

পাইথন পরের মান 35 নিল।

শর্ত চেক করা হলো: if 35 % 2 == 0: (৩৫ কে ২ দিয়ে ভাগ করলে ভাগশেষ ১ থাকে, যা ০ এর সমান নয়)।

শর্তটি মিথ্যা (False), তাই পাইথন চলে গেল else ব্লকে।

আউটপুট: 35 is odd

৩. তৃতীয় ইটারেশন (num = 7):

পাইথন মান 7 নিল।

শর্ত চেক করা হলো: 7 % 2 == 0 (মিথ্যা, ভাগশেষ ১ থাকে)।

পাইথন else ব্লকে চলে গেল।

আউটপুট: 7 is odd

৪. চতুর্থ ইটারেশন (num = 44):

পাইথন শেষ মান 44 নিল।

শর্ত চেক করা হলো: 44 % 2 == 0 (সত্য, ভাগশেষ ০)।

if ব্লকের কোড রান করল।

আউটপুট: 44 is even

লিস্টের সব উপাদান চেক করা শেষ, তাই লুপ নিজে থেকেই বন্ধ হয়ে গেল!
