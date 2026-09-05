থনে while-এর ভেতরে if এবং if-এর ভেতরে while—দুটিই শতভাগ সম্ভব এবং ব্যাকএন্ড ডেভেলপমেন্টে এগুলো নিয়মিত ব্যবহার করা হয়। প্রোগ্রামিংয়ের ভাষায় একে Nested Control Flow বলা হয়।

is_logged_in = True  # ধরি ইউজার সফলভাবে লগইন করেছে

print("--- System Authentication ---")

# প্রথমে একটি if কন্ডিশন দিয়ে চেক করা হচ্ছে ইউজার লগইন করা কি না
if is_logged_in:
    print("Authentication Success! ✅ Starting active session...")
    
    ping_count = 1
    
    # if কন্ডিশনের ভেতরে একটি while লুপ শুরু হলো যা সেশন ধরে রাখবে
    while ping_count <= 3:
        print(f"Session ping {ping_count}: Server is active... 🟢")
        ping_count += 1
        
else:
    print("Access Denied! ❌ Please log in to continue.")

--- System Authentication ---
Authentication Success! ✅ Starting active session...
Session ping 1: Server is active... 🟢
Session ping 2: Server is active... 🟢
Session ping 3: Server is active... 🟢

সেশন ম্যানেজমেন্ট কোডটির ড্রাই রান, কোনো রকম তীর চিহ্ন (->) ছাড়াই নিচে সিরিয়াল অনুযায়ী দেওয়া হলো:

ধাপ ১: ইনিশিয়ালাইজেশন এবং প্রিন্ট
is_logged_in = True

মেমরিতে is_logged_in ভেরিয়েবলের মধ্যে True মান সংরক্ষিত হলো (অর্থাৎ ইউজার লগইন করা অবস্থায় আছেন)।

print("--- System Authentication ---")

টার্মিনাল আউটপুটে প্রিন্ট হলো: --- System Authentication ---

ধাপ ২: মেইন কন্ডিশন চেক (If Block)
if is_logged_in:

চেক করা হলো is_logged_in-এর মান সত্য কি না। যেহেতু মান True, তাই শর্তটি সত্য হিসেবে গণ্য হলো এবং পাইথন if ব্লকের ভেতরে প্রবেশ করল।

print("Authentication Success! ✅ Starting active session...")

টার্মিনাল আউটপুটে প্রিন্ট হলো: Authentication Success! ✅ Starting active session...

ping_count = 1

মেমরিতে একটি কাউন্টার ভেরিয়েবল ping_count তৈরি হলো এবং এর প্রাথমিক মান 1 সেট করা হলো।

ধাপ ৩: ভেতরের লুপ এক্সিকিউশন (Nested While Loop)
১ম বার লুপ ঘোরা (Iteration 1):

while ping_count <= 3: অংশটি যাচাই করল ping_count-এর মান ৩-এর সমান বা ছোট কি না। বর্তমান মান ১ হওয়ায় শর্তটি সত্য হলো এবং লুপের ভেতরে প্রবেশ করল।

print(f"Session ping {ping_count}: Server is active... 🟢") কোডটি আউটপুট দিল: Session ping 1: Server is active... 🟢

ping_count += 1 কোডের মাধ্যমে ping_count-এর মান ১ বেড়ে হলো ২।

২য় বার লুপ ঘোরা (Iteration 2):

while ping_count <= 3: যাচাই করল বর্তমান মান ২, যা ৩-এর সমান বা ছোট কি না। শর্ত সত্য হওয়ায় লুপ আবার চলল।

print(...) কোডটি আউটপুট দিল: Session ping 2: Server is active... 🟢

ping_count += 1 কোডের মাধ্যমে মান ১ বেড়ে হলো ৩।

৩য় বার লুপ ঘোরা (Iteration 3):

while ping_count <= 3: যাচাই করল বর্তমান মান ৩, যা ৩-এর সমান বা ছোট কি না। শর্ত সত্য হওয়ায় লুপ শেষবারের মতো চলল।

print(...) কোডটি আউটপুট দিল: Session ping 3: Server is active... 🟢

ping_count += 1 কোডের মাধ্যমে মান ১ বেড়ে হলো ৪।

লুপ সমাপ্তি:

চতুর্থবার যখন লুপ উপরে গিয়ে যাচাই করল ৪ সংখ্যাটি ৩-এর সমান বা ছোট কি না, তখন শর্তটি মিথ্যা হলো। ফলে while লুপের কাজ শেষ হলো এবং এক্সিকিউশন লুপের বাইরে চলে আসল।

ধাপ ৪: শেষ অংশ (Else Block Skip)
else:

যেহেতু কোডের শুরুতে if শর্তটি সত্য হয়েছিল এবং পুরো কাজটি সফলভাবে সম্পন্ন হয়েছে, তাই else ব্লকটি সম্পূর্ণ স্কিপ বা বাদ হয়ে গেল এবং প্রোগ্রাম সফলভাবে শেষ হলো।





even_odd_filter

number = 1

while number <= 10:
    # যদি সংখ্যাটি জোড় হয়, তবেই প্রিন্ট করবে
    if number % 2 == 0:
        print(f"Even number found: {number}")
        
    number += 1



সার্ভার ফেইল হ্যান্ডেলিং বা রি-ট্রাই লজিক (Retry Mechanism)
ব্যাকএন্ডে কোনো এপিআই (API) কল ফেইল করলে বারবার চেষ্টা করার জন্য এই লজিক ব্যবহার করা হয়।

  
attempts = 0
max_retries = 3
is_connected = False

while attempts < max_retries:
    attempts += 1
    
    # ধরি দ্বিতীয়বারে কানেকশন সফল হলো
    if attempts == 2:
        is_connected = True
        print(f"Attempt {attempts}: Connection Successful! 🟢")
        break  # সফল হলে লুপ ভেঙে বের হয়ে যাবে
    else:
        print(f"Attempt {attempts}: Connection failed... Retrying 🔄")



নেগেটিভ (Negative) সংখ্যা পেলেই লুপ থামিয়ে দেওয়া
ইউজার যতক্ষণ পজিটিভ সংখ্যা দেবে লুপ চলতে থাকবে, কিন্তু মাইনাস সংখ্যা পেলেই if এবং break দিয়ে লুপ বন্ধ করে দেওয়া হবে।


current_value = 1

while current_value > 0:
    # শর্ত: মান যদি ৫ এর বেশি হয়, তবে লুপ ব্রেক করবে
    if current_value > 5:
        print("Value exceeded limit! Stopping loop... 🛑")
        break
        
    print(f"Current safe value: {current_value}")
    current_value += 1





if-এর ভেতরে while (Nested While inside If)
এই সিনারিওয়িওতে প্রথমে একটি মেইন কন্ডিশন (if) চেক করা হয়। শর্ত সত্য হলে তার ভেতরে একটিভ সেশনের মতো একটি while লুপ শুরু হয় এবং count == 3 হলে লুপটি আর ঘোরে না।


is_authenticated = True
count = 0

print("--- System Check Initiated ---")

# প্রথমে একটি if কন্ডিশন দিয়ে চেক করা হচ্ছে ইউজার ভ্যালিড কি না
if is_authenticated:
    print("User authenticated successfully! ✅ Starting background process...")
    
    # if এর ভেতরে একটি while লুপ শুরু হলো
    # count == 3 হলে লুপ আর ঘুরবে না (condition false হয়ে যাবে)
    while count < 3:
        count += 1
        print(f"Background process running... Cycle count: {count}")
        
    print("Background process finished safely. 🟢")
else:
    print("Access Denied! ❌")



           

while-এর ভেতরে if (Nested If inside While)
এই সিনারিওতে মেইন লুপটি ঘুরতে থাকে (while), আর প্রতিবার ঘোরার সময় ভেতরের কন্ডিশন (if) চেক করে। যখনই count == 3 হয়, তখন if-এর ভেতরে থাকা লজিক লুপের পরবর্তী চলা বন্ধ করে দেয়।


count = 0
is_running = True

print("--- Monitoring Server Status ---")

# while লুপটি ঘুরতে থাকবে যতক্ষণ is_running সত্য থাকে
while is_running:
    count += 1
    print(f"Checking server... Current count: {count}")
    
    # if কন্ডিশন দিয়ে চেক করা হচ্ছে count এর মান ৩ হলো কি না
    if count == 3:
        # count == 3 হলে is_running কে False করে দেওয়া হলো
        # ফলে লুপের শর্ত মিথ্যা হয়ে যাবে এবং এটি আর ঘুরবে না
        is_running = False
        print("Limit reached (count == 3)! Stopping the server monitor. 🛑")

print("Monitor program exited successfully. ✅")



if-এর ভেতরে while (সিস্টেম বুট প্রসেস সিমুলেশন)
এখানে প্রথমে সিস্টেম স্ট্যাটাস চেক করা হয় (if), স্ট্যাটাস ওকে থাকলে ভেতরের while লুপের মাধ্যমে বুটিং স্টেপগুলো কাউন্ট করা হয়। ঠিক count == 3 তে পৌঁছালে বুটিং শেষ হয়ে লুপটি বন্ধ হয়ে যায়।


system_ready = True
boot_count = 0

print("--- System Boot Sequence ---")

# প্রথমে চেক করা হচ্ছে সিস্টেম রেডি কি না
if system_ready:
    print("Power ON signal received. ⚡ Starting boot process...")
    
    # if এর ভেতরে while লুপ
    # boot_count ৩ না হওয়া পর্যন্ত লুপ ঘুরবে
    while boot_count < 3:
        boot_count += 1
        print(f"Booting phase {boot_count} in progress...")
        
    print("System boot completed successfully! 🚀")
else:
    print("Power failure! System cannot boot. ❌")



           
while-এর ভেতরে if (ডাটা প্রসেসিং কিউ/Queue)
এখানে মূল লুপ চলতে থাকে (while), আর প্রতি ধাপে if কন্ডিশন চেক করে যে কাজ কতদূর হলো। যখনই count == 3 হয়, 
তখন ফ্লাগ ভেরিয়েবল পরিবর্তন করে লুপের পুনরাবৃত্তি থামিয়ে দেওয়া হয়।

queue_count = 0
is_queue_active = True

print("--- Data Packet Processing ---")

# while লুপ চলতে থাকবে যতক্ষণ queue active থাকে
while is_queue_active:
    queue_count += 1
    print(f"Processing packet number: {queue_count}")
    
    # if কন্ডিশন দিয়ে চেক করা হচ্ছে count এর মান ৩ হলো কি না
    if queue_count == 3:
        # count == 3 হলে কিউ বা লুপ বন্ধ করার ফ্লাগ True থেকে False করা হলো
        is_queue_active = False
        print("Packet limit (count == 3) reached. Closing queue safely. 🔒")

print("All packets processed. Program ended. ✅")



if-এর ভেতরে while (API রেট লিমিট হ্যান্ডলিং)
রিয়েল-ওয়ার্ল্ড ব্যাকএন্ডে অনেক সময় ইউজারকে একটি নির্দিষ্ট সময়ের জন্য সীমিত সংখ্যক রিকোয়েস্ট (Rate Limit) করতে দেওয়া হয়।
এখানে প্রথমে চেক করা হয় ইউজারের অ্যাক্সেস টোকেন ভ্যালিড কি না (if), এরপর ভেতরের while লুপ দিয়ে সর্বোচ্চ ৩টি রিকোয়েস্ট প্রসেস করা হয়।

is_token_valid = True
request_count = 0
max_allowed_requests = 3

print("--- API Gateway Security Check ---")

# প্রথমে চেক করা হচ্ছে ইউজারের টোকেন ভ্যালিড কি না
if is_token_valid:
    print("Token verified! 🟢 Processing API requests...")
    
    # if এর ভেতরে while লুপ: রিকোয়েস্ট কাউন্ট ৩ না হওয়া পর্যন্ত চলবে
    while request_count < max_allowed_requests:
        request_count += 1
        print(f"API Request #{request_count}: Data fetched successfully. 📦")
        
    print("Rate limit reached for this cycle. Please wait. ⏳")
else:
    print("Invalid Token! Access Denied. ❌")



while-এর ভেতরে if (ইকমার্স কার্ট বা শপিং ব্যাগ চেকআউট)
ব্যাকএন্ডে শপিং কার্ট থেকে একে একে আইটেম প্রসেস করার সময় এই ধরনের লজিক লাগে। মূল লুপ আইটেম প্রসেস করতে থাকে (while), 
আর if কন্ডিশন চেক করে যে ৩টি আইটেম প্রসেস হয়েছে কি না। ৩টি আইটেম হয়ে গেলে লুপটি আর ঘোরে না।   

item_count = 0
is_cart_processing = True

print("--- E-Commerce Checkout System ---")

# কার্টে আইটেম প্রসেসিং লুপ চলতে থাকবে
while is_cart_processing:
    item_count += 1
    print(f"Processing item number {item_count} in cart...")
    
    # যদি ৩টি আইটেম প্রসেস করা হয়ে যায়
    if item_count == 3:
        # প্রসেসিং স্ট্যাটাস False করে দেওয়া হলো, ফলে লুপ আর ঘুরবে না
        is_cart_processing = False
        print("All 3 items processed successfully! Closing checkout gateway. 🛍️✅")

print("Checkout session ended. Thank you! 🙏")
             
                                                                                             
