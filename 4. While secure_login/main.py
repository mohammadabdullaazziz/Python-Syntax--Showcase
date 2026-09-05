correct_pin = "1234"
attempts_left = 3   # সর্বোচ্চ ৩ বার চেষ্টা করার সুযোগ আছে

print("--- Welcome to ATM System ---")

# While লুপ: ইউজারের যতক্ষণ সুযোগ বাকি থাকবে, লুপটি চলতেই থাকবে
while attempts_left > 0:
    entered_pin = input("Enter your 4-digit PIN code: ")
    
    # If কন্ডিশন ১: পিন সঠিক কি না তা চেক করা
    if entered_pin == correct_pin:
        print("Success! Your account has been unlocked. ✅")
        break  # পিন সঠিক হলে লুপটি সাথে সাথে ভেঙে বের হয়ে যাবে
        
    # Else কন্ডিশন: পিন ভুল হলে এটি রান করবে
    else:
        attempts_left -= 1  # এক দফা সুযোগ কমে গেল
        print(f"Incorrect PIN! ❌ You have {attempts_left} attempt(s) left.")

# ইউজার সব সুযোগ হারিয়ে ফেললে এটি ব্লক করে দেবে
if attempts_left == 0:
    print("Security Alert! 🚨 Your card has been blocked.")


ইনিশিয়ালাইজেশন (Initialization)
correct_pin = "1234"

মেমরিতে correct_pin ভেরিয়েবলের মধ্যে "1234" স্ট্রিংটি সংরক্ষিত হলো।

attempts_left = 3

মেমরিতে attempts_left ভেরিয়েবলে ইন্টিজার মান 3 সেট করা হলো।

print("--- Welcome to ATM System ---")

টার্মিনাল আউটপুটে প্রিন্ট হলো: --- Welcome to ATM System ---

ধাপ ২: প্রথমবার লুপ এক্সিকিউশন (ইউজার ভুল পিন দিল: "0000")
while attempts_left > 0:

শর্ত চেক করা হলো যে 3 > 0 কি না, যা সত্য হিসেবে গণ্য হলো। ফলে এক্সিকিউশন লুপের ভেতরে প্রবেশ করল।

entered_pin = input("Enter your 4-digit PIN code: ")

প্রোগ্রাম ইউজারের ইনপুটের জন্য অপেক্ষা করল। ইউজার দিল "0000"।

if entered_pin == correct_pin:

চেক করা হলো "0000" এবং "1234" সমান কি না, যা মিথ্যা হিসেবে গণ্য হলো। প্রোগ্রাম if ব্লক এড়িয়ে else ব্লকে চলে গেল।

attempts_left -= 1

else ব্লক রান করল। attempts_left-এর মান ১ কমে নতুন মান হলো 2।

print(f"Incorrect PIN! ❌ You have {attempts_left} attempt(s) left.")

টার্মিনাল আউটপুটে প্রিন্ট হলো: Incorrect PIN! ❌ You have 2 attempt(s) left.

ধাপ ৩: দ্বিতীয়বার লুপ এক্সিকিউশন (ইউজার ভুল পিন দিল: "1111")
while attempts_left > 0:

শর্ত চেক করা হলো যে 2 > 0 কি না, যা সত্য। লুপ আবার চলল।

entered_pin = input(...)

ইউজার দিল "1111"।

if entered_pin == correct_pin:

চেক করা হলো "1111" এবং "1234" সমান কি না, যা মিথ্যা।

attempts_left -= 1

attempts_left-এর মান ১ কমে নতুন মান হলো 1।

print(...)

টার্মিনাল আউটপুটে প্রিন্ট হলো: Incorrect PIN! ❌ You have 1 attempt(s) left.

ধাপ ৪: তৃতীয়বার লুপ এক্সিকিউশন (ইউজার সঠিক পিন দিল: "1234")
while attempts_left > 0:

শর্ত চেক করা হলো যে 1 > 0 কি না, যা সত্য। লুপ শেষবারের মতো চলল।

entered_pin = input(...)

ইউজার সঠিক পিন "1234" দিল।

if entered_pin == correct_pin:

চেক করা হলো "1234" এবং "1234" সমান কি না, যা সত্য হিসেবে গণ্য হলো। এক্সিকিউশন if ব্লকের ভেতরে প্রবেশ করল।

print("Success! Your account has been unlocked. ✅")

টার্মিনাল আউটপুটে প্রিন্ট হলো: Success! Your account has been unlocked. ✅

break

ব্রেক কমান্ড রান করল, যা সাথে সাথে while লুপটিকে চিরতরে থামিয়ে দিল এবং এক্সিকিউশনকে লুপের বাইরে নিয়ে গেল।

ধাপ ৫: লুপের বাইরের শেষ মূল্যায়ন
if attempts_left == 0:

চেক করা হলো 1 এবং 0 সমান কি না, যা মিথ্যা হিসেবে গণ্য হলো (কারণ attempts_left-এর মান তখনো 1 ছিল)।

প্রোগ্রাম সমাপ্তি (Program Termination):

শর্ত মিথ্যা হওয়ায় কার্ড ব্লক হওয়ার ওয়ার্নিং মেসেজটি স্কিপ করা হলো এবং প্রোগ্রাম সফলভাবে শেষ হলো।
