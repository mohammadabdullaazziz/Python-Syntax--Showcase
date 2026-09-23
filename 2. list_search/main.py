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





সংখ্যাটি লিস্টের কত নম্বর পজিশনে (Index) আছে তা দেখানো
সংখ্যাটি লিস্টে পাওয়ার পর সেটি কত নম্বর ইনডেক্সে বা পজিশনে আছে, তা বের করতে  index() মেথড ব্যবহার:

number = [10, 20, 30, 40, 50]
user_number = int(input("Enter a number to check: "))

if user_number in number:
    position = number.index(user_number)
    print(f"{user_number} is in the list! Its position or index is: {position}")
else:
    print(f"{user_number} is not in the list.")


number = [10, 20, 30, 40, 50]

পাইথন মেমোরিতে number নামের একটি লিস্ট তৈরি হলো যার ভেতরে ৫টি উপাদান আছে।

user_number = int(input("Enter a number to check if it is in the list: "))

ইউজারের কাছ থেকে কনসোলে একটি সংখ্যা ইনপুট চাওয়া হলো। ধরা যাক ইউজার ইনপুট দিল 30। সেটি ইন্টিজারে রূপান্তরিত হয়ে user_number ভ্যারিয়েবলে জমা হলো।

if user_number in number:

কন্ডিশন চেক করা হলো যে 30 সংখ্যাটি number লিস্টের মধ্যে আছে কি না। যেহেতু 30 লিস্টে আছে, তাই শর্তটি True হলো।

position = number.index(user_number)

লিস্টে 30 সংখ্যাটি কত নম্বর ইনডেক্সে আছে তা খোঁজা হলো। এটি ইনডেক্স 2 এ পাওয়া গেল এবং position ভ্যারিয়েবলে 2 সংরক্ষিত হলো।

print(f"{user_number} is in the list! Its position or index is: {position}")

স্ক্রিনে প্রিন্ট হলো: 30 is in the list! Its position or index is: 2

else:

যেহেতু if এর শর্ত সত্য হয়েছে, তাই else ব্লকের ভেতরের কোডগুলো স্কিপ বা বাদ চলে যাবে।


position = number.index(user_number) এই লাইনটির সহজ অর্থ হলো—ইউজার যে সংখ্যাটি ইনপুট দিয়েছেন (user_number),
সেটি number নামের লিস্টের কত নম্বর ইনডেক্সে বা পজিশনে আছে তা খুঁজে বের করা এবং সেই ইনডেক্স নম্বরটি position নামের ভ্যারিয়েবলে সংরক্ষণ করা।







নতুন সংখ্যা লিস্টে যোগ করার সুবিধা (Add to List)
যদি ইউজার এমন কোনো সংখ্যা ইনপুট দেয় যা লিস্টে নেই, তখন তাকে জিজ্ঞেস করতে পারেন
যে সে সংখ্যাটি লিস্টে যোগ করতে চায় কিনা। হ্যাঁ বললে সেটা লিস্টে যোগ হয়ে যাবে:


number = [10, 20, 30, 40, 50]
user_number = int(input("Enter a number to check: "))

if user_number in number:
    print(f"{user_number} already in the list")
else:
    print(f"{user_number} is not in the list.")
    choice = input("Do you want to add this number to the list? (yes/no): ")
    if choice.lower() == 'yes':
        number.append(user_number)
        print("List updated! New list:", number)


এই সম্পূর্ণ কোডটির লাইন বাই লাইন ড্রাই রান (Dry Run) নিচে দেওয়া হলো:

number = [10, 20, 30, 40, 50]

মেমোরিতে number নামের একটি লিস্ট তৈরি হলো যার ভেতরে ৫টি উপাদান রয়েছে।

user_number = int(input("Enter a number to check: "))

ইউজারের কাছ থেকে সংখ্যা ইনপুট চাওয়া হলো।

ধরে নেওয়া যাক ইউজার ইনপুট দিল 30 (যা লিস্টে আছে)।

if user_number in number:

চেক করা হলো 30 সংখ্যাটি লিস্টে আছে কি না। যেহেতু 30 লিস্টে আছে, তাই শর্তটি True হলো।

print(f"{user_number} already in the list")

কনসোলে প্রিন্ট হলো: 30 already in the list

যেহেতু if শর্ত সত্য হয়েছে, তাই else ব্লকের ভেতরের কোডগুলো আর রান হবে না। প্রোগ্রাম এখানেই শেষ হয়ে যাবে।

যদি ইউজার এমন সংখ্যা দিত যা লিস্টে নেই (যেমন: 60):

number = [10, 20, 30, 40, 50] (লিস্ট ডিক্লেয়ার হলো)

user_number এ ইউজার ইনপুট দিল 60।

if user_number in number: চেক করে দেখল 60 লিস্টে নেই, তাই শর্তটি False হলো এবং কোডটি else ব্লকে চলে গেল।

print(f"{user_number} is not in the list.") প্রিন্ট হলো: 60 is not in the list.

choice = input("Do you want to add this number to the list? (yes/no): ")

ইউজারের কাছে জানতে চাওয়া হলো সে লিস্টে যোগ করতে চায় কিনা।

ধরে নিই ইউজার লিখল yes।

if choice.lower() == 'yes': শর্তটি সত্য হলো।

number.append(user_number)

60 সংখ্যাটি number লিস্টের একদম শেষে যুক্ত হয়ে গেল। এখন লিস্টটি হলো: [10, 20, 30, 40, 50, 60]।

print("List updated! New list:", number)

প্রিন্ট হলো: List updated! New list: [10, 20, 30, 40, 50, 60]

ব্যাকএন্ডের ভাষায় কোডের রূপ কেমন হয়?
ব্যাকএন্ডের ছোট একটা এপিআই (API) বা ফাংশন তৈরি করা যায়। যেমন:

# ব্যাকএন্ডে একটি ডাটাবেজের ডামি লিস্ট (ধরে নিন এটি আপনার ডেটাবেজ)
database_numbers = [10, 20, 30, 40, 50]

def check_and_add_number(user_number):
    if user_number in database_numbers:
        return {"status": "success", "message": f"{user_number} আগেই ডাটাবেজে আছে!"}
    else:
        # ব্যাকএন্ড স্বয়ংক্রিয়ভাবে বা ইউজারের অনুমতি নিয়ে ডাটাবেজে সেভ করে দেবে
        database_numbers.append(user_number)
        return {"status": "updated", "message": f"{user_number} সফলভাবে ডাটাবেজে যোগ করা হয়েছে!", "new_db": database_numbers}

# ফাংশন টেস্ট করে দেখি:
print(check_and_add_number(100))

{'status': 'updated', 'message': '100 সফলভাবে ডাটাবেজে যোগ করা হয়েছে!', 'new_db': [10, 20, 30, 40, 50, 100]}






লুপ চালিয়ে বারবার চেক করার সুবিধা (While Loop)
একবার কোড রান করে চেক করার পর প্রোগ্রাম বন্ধ হয়ে যায়। চাইলে একটি while লুপ ব্যবহার করা যাবে, যাতে ইউজার যতক্ষণ চায় ততক্ষণ সংখ্যা চেক করতে পারে:


number = [10, 20, 30, 40, 50]

while True:
    user_input = input("একটি সংখ্যা লিখুন (অথবা বন্ধ করতে 'q' চাপুন): ")
    
    if user_input.lower() == 'q':
        print("প্রোগ্রাম শেষ!")
        break
        
    user_number = int(user_input)
    
    if user_number in number:
        print(f"✅ {user_number} লিস্টের মধ্যে আছে।\n")
    else:
        print(f"❌ {user_number} লিস্টের মধ্যে নেই।\n")






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
