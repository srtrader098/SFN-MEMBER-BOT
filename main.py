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

# কতগুলো অ্যাকাউন্ট চাও? (৫০০০ ডিফল্ট)
NUM_ACCOUNTS = 5000

async def run_bot():
    print("🚀 Starting Bot...")
    for i in range(NUM_ACCOUNTS):
        try:
            client_name = f"user_{i}"
            # নতুন অ্যাকাউন্ট খুলে কাজ করছে
            client = Client(name=client_name, api_id=API_ID, api_hash=API_HASH)
            await client.connect()
            
            for channel in CHANNELS:
                await client.join_chat(channel)
                
            await client.disconnect()
            
            if (i + 1) % 100 == 0:
                print(f"[+] Done {i+1} accounts. Waiting 1 min...")
                time.sleep(60)
            else:
                time.sleep(2)
                
        except Exception as e:
            print(f"[-] Error at {i}: {e}")
            
    print("✅ All Done!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_bot())
