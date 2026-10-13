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

SESSIONS_FILE = "sessions.txt"

def load_sessions(filename):
    if not os.path.exists(filename):
        print("❌ সেশন ফাইল পাওয়া যায়নি!")
        return []
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]

async def join_channel(session_string, channel):
    try:
        client = Client(name=f"temp_{hash(session_string)%1000}", api_id=API_ID, api_hash=API_HASH, session_string=session_string)
        await client.connect()
        await client.join_chat(channel)
        await client.disconnect()
        return True
    except Exception as e:
        return False

async def main():
    sessions = load_sessions(SESSIONS_FILE)
    if not sessions:
        return
        
    total_accounts = len(sessions)
    print(f"🚀 Starting for {total_accounts} accounts...")
    
    account_index = 0
    
    while account_index < total_accounts:
        sess = sessions[account_index]
        
        for channel in CHANNELS:
            result = await join_channel(sess, channel)
                
        account_index += 1
        
        # রেট লিমিট এড়াতে বিরতি
        if account_index % 50 == 0:
            time.sleep(60)
        else:
            time.sleep(2)
            
    print("✅ Done!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
