from pyrogram import Client
import os
import time

# API Details (তোমার দেওয়া ID/Hash)
API_ID = 32074833
API_HASH = "66a91da49612ffc031459a2a8cf02a20"

# চ্যানেলের নাম
CHANNELS = ["@SFN_News", "@SFN_Payment"]

# কতবার জয়েন করার চেষ্টা করবে (৫০০০ জনের জন্য)
ATTEMPTS = 5000

async def main():
    # GitHub Secrets থেকে স্ট্রিং নেওয়া
    session_string = os.environ.get('SESSION_STRING')
    
    if not session_string:
        print("❌ Error: SESSION_STRING not found in Secrets!")
        return

    print("🚀 Connecting to Telegram...")
    
    # কানেক্ট করা
    client = Client(
        ":memory:", 
        api_id=API_ID, 
        api_hash=API_HASH,
        session_string=session_string
    )
    
    await client.connect()
    print("✅ Connected successfully!")

    for i in range(ATTEMPTS):
        try:
            for ch in CHANNELS:
                await client.join_chat(ch)
            
            # প্রতি ১০০ টি চেষ্টায় এক মিনিট বিরতি (যাতে ব্যান না হয়)
            if (i + 1) % 100 == 0:
                print(f"[+] Completed {i+1} attempts.")
                time.sleep(60) 
            else:
                time.sleep(2) # সাধারণ ডিলে
                
        except Exception as e:
            print(f"[-] Error at attempt {i}: {e}")
            
    await client.disconnect()
    print("✅ All tasks completed!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
