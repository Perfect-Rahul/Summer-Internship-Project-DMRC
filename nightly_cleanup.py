from db import get_old_records, delete_old_records
from api_pusher import delete_old_from_firewall

def cleanup_job():
    print("🧹 Starting cleanup job...")

    # Delete old entries from DB
    for table in ['ips_table', 'domains_table', 'hashes_table']:
        old_records = get_old_records(table)
        if old_records:
            print(f"⏳ Deleting {len(old_records)} old records from {table}")
            delete_old_records(table)
        else:
            print(f"✅ No old records in {table}")

    # Call delete APIs to sync firewall
    delete_old_from_firewall()

    print("✅ Cleanup job completed.")

if __name__ == "__main__":
    cleanup_job()
