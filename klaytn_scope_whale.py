import requests, time

def klaytn_whale():
    print("Klaytn — Scope Whale Sighted (> 50M KLAY moved in one block)")
    seen = set()
    while True:
        r = requests.get("https://scope.klaytn.com/api/v1/transactions?size=40")
        for tx in r.json().get("result", []):
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            # Pure KLAY transfer (type 0x0)
            if tx.get("typeInt") != 0: continue
            amount = int(tx.get("value"), 16) / 1e18

            if amount >= 50_000_000:  # > 50 million KLAY
                print(f"SCOPE WHALE DETECTED\n"
                      f"{amount:,.0f} KLAY moved instantly\n"
                      f"From: {tx['from'][:16]}...\n"
                      f"To:   {tx['to'][:16]}...\n"
                      f"Block: {tx['blockNumber']']}\n"
                      f"https://scope.klaytn.com/tx/{h}\n"
                      f"→ Kakao-level or exchange cold wallet move\n"
                      f"→ Klaytn just proved enterprise scale in production\n"
                      f"{'-'*80}")
        time.sleep(1.8)

if __name__ == "__main__":
    klaytn_whale()
