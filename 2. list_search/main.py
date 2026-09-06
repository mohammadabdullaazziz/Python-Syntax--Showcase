# লিস্টের নাম দিলাম numbers (বহুবচন)
numbers = [10, 20, 30, 40, 50]

# ইউজারের ইনপুটের নাম দিলাম user_number (একবচন)
user_number = int(input("Enter a number to check if it is in the list: "))

# এখন লিস্টের ভেতরে সংখ্যাটি খুঁজছি
if user_number in numbers:
    print(f"{user_number} is in the list.")
else:
    print(f"{user_number} is not in the list.")



১. numbers = [10, 20, 30, 40, 50]

কী হচ্ছে: মেমোরিতে numbers নামের একটি লিস্ট তৈরি হলো, যার ভেতরে পাঁচটি পূর্ণসংখ্যা আছে।

২. user_number = int(input(...))

কী হচ্ছে:

পাইথন স্ক্রিনে প্রম্পট দেখাবে: Enter a number to check if it is in the list:

ইউজার কীবোর্ড থেকে টাইপ করলেন 30।

input() ফাংশন এই 30-কে প্রথমে স্ট্রিং ("30") হিসেবে ধরবে।

সামনের int() ফাংশনটি এটাকে স্ট্রিং থেকে ইনটিজার সংখ্যায় (30) রূপান্তর (Type Cast) করবে।

সবশেষে মানটি user_number ভেরিয়েবলে জমা হবে।

৩. if user_number in numbers:

কী হচ্ছে: পাইথন চেক করবে user_number (যার মান 30) numbers লিস্টটির ভেতরে আছে কি না (in অপারেটর ব্যবহার করে)।

যেহেতু লিস্টে 30 موجود আছে, তাই শর্তটি সত্য (True) হলো।

৪. print(f"{user_number} is in the list.")

কী হচ্ছে: যেহেতু if এর শর্ত সত্য হয়েছে, তাই এই ব্লকের ভেতরে ঢুকে কনসোলে প্রিন্ট করবে:

30 is in the list.

(else ব্লকটি এই ক্ষেত্রে পুরোপুরি স্কিপ বা বাদ হয়ে যাবে)।




user_input = int(input("Enter a number: "))

# সংখ্যাটি জোড় কি না তা চেক করা
if user_input % 2 == 0:
    print(f"{user_input} is an Even (জোড়) number")
else:
    print(f"{user_input} is an Odd (বিজোড়) number")






even_numbers = []
odd_numbers = []

for num in range(1, 21):
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)


list Comprehension

even_numbers = [num for num in range(1, 21) if num % 2 == 0]
odd_numbers = [num for num in range(1, 21) if num % 2 != 0]

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)





১. যদি numbers = [1, 2, 3, 4, 5] থাকে:

numbers = [1, 2, 3, 4, 5]

for x in numbers:
    print(x)

কীভাবে কাজ করবে? এখানে x কোনো ইনডেক্স (0, 1, 2...) নয়, বরং x সরাসরি লিস্টের ভেତরের মূল উপাদানগুলো একে একে ধরে নেবে।

অর্থাৎ, প্রথম লুপে x = 1, দ্বিতীয় লুপে x = 2, এভাবে শেষ পর্যন্ত (5) চলতে থাকবে।


২. যদি range(0, 21) থাকে:

for x in range(0, 21):
    print(x)

কীভাবে কাজ করবে? এটি কোনো লিস্টের উপাদান রিড করছে না, বরং পাইথনকে বলে দিচ্ছে যে 0 থেকে শুরু করে 20 পর্যন্ত (২১ এর আগ পর্যন্ত) 
সংখ্যাগুলোর একটি সিকোয়েন্স তৈরি করতে। এখানে x এর মান হবে 0, 1, 2, 3 ... 20 পর্যন্ত।

৩. সংখ্যা যদি অজানা বা ডাইনামিক হয় (যেমন ইউজারের কাছ থেকে এসেছে):
লিস্টের ভেତরের ডেটা আগে থেকে জানা থাকুক বা অজানা (ডাইনামিক) থাকুক—for x in numbers: এর নিয়ম সবসময় একই থাকে।

লিস্টে যতগুলো উপাদান থাকবে, লুপ ঠিক ততবারই ঘুরবে।

আর x প্রতিবার ওই লিস্টের একেকটি উপাদানকে নিজে ধারণ করবে।






numbers = [1, 2, 3, 4, 5, 6, 7, 8]

new_numbers = []

for x in numbers:
  if x > 4:
    new_numbers.append(x)

print(new_numbers)

কোডে একটি শর্ত বা কন্ডিশন: if x > 4: (যার মানে হলো—যে সংখ্যাগুলো ৪ এর চেয়ে বড়, শুধু সেগুলোকে নাও)।

লুপে আসলে কী ঘটছে?
১. যখন x এর মান 1, 2, 3, 4 হয়, তখন x > 4 শর্তটি মিথ্যা (False) হয়। তাই পাইথন এই সংখ্যাগুলোকে ইগ্নোর করে (লিস্টে যোগ করে না)।
২. যখন x এর মান 5, 6, 7, 8 হয়, তখন x > 4 শর্তটি সত্য (True) হয়। তাই শুধু এই বড় সংখ্যাগুলোই new_numbers লিস্টে গিয়ে জমা হয়।

যদি 1, 2, 3, 4 দেখতে, তবে কী করতে হবে?
যদি  ৪ বা তার চেয়ে ছোট সংখ্যাগুলো লিস্টে আসুক, তবে শর্তে > (বড়) এর বদলে <= (ছোট বা সমান) বা < (ছোট) ব্যবহার করতে হবে। যেমন:


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

new_numbers = []

for x in numbers:
  if x < 4:
    new_numbers.append(x)

print(new_numbers)


list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# ৪ এর চেয়ে বড় সংখ্যাগুলোর জন্য লিস্ট কমপ্রহেনশন
new_numbers = [x for x in numbers if x > 4]

print("Bigger than 4:", new_numbers) 
# আউটপুট: [5, 6, 7, 8]


৪ বা তার চেয়ে ছোট সংখ্যাগুলো ফিল্টার করার জন্য (1, 2, 3, 4 পাওয়ার জন্য):

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# ৪ বা তার চেয়ে ছোট সংখ্যাগুলোর জন্য লিস্ট কমপ্রহেনশন
smaller_numbers = [x for x in numbers if x <= 4]

print("Less than or equal to 4:", smaller_numbers) 
# আউটপুট: [1, 2, 3, 4]
