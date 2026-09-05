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
