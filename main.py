from pyrogram import Client
import time
import os

# --- তোমার তথ্য ---
API_ID = 32074833
API_HASH = "66a91da49612ffc031459a2a8cf02a20"

# চ্যানেলের ইউজারনেম
CHANNELS = [
    "@SFN_News",
    "@SFN_Payment"
]

# কতগুলো অ্যাকাউন্ট বানাতে চাও? (৫০০০ সাজেস্ট করছি)
NUM_ACCOUNTS = 5000

async def generate_and_join():
    print("🔄 Generating sessions and joining channels...")
    
    for i in range(NUM_ACCOUNTS):
        try:
            # প্রতিবার নতুন নাম দিয়ে ক্লায়েন্ট তৈরি
            client_name = f"gen_{i}"
            client = Client(
                name=client_name, 
                api_id=API_ID, 
                api_hash=API_HASH
            )
            
            await client.connect()
            
            # চ্যানেলে জয়েন করা
            for channel in CHANNELS:
                await client.join_chat(channel)
                
            # কাজ শেষ হলে ডিসকানেক্ট
            await client.disconnect()
            
            if (i + 1) % 100 == 0:
                print(f"[+] Completed {i+1} accounts. Waiting 1 minute to avoid ban...")
                time.sleep(60)
            else:
                time.sleep(2) # ছোট বিরতি
                
        except Exception as e:
            print(f"[-] Error at account {i}: {e}")
            
    print("✅ All tasks completed!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(generate_and_join())
