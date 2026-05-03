fname = "ancient_fragment.txt"
print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print(f"Accessing Storage Vault: {fname}")
print("Connection established...\n")
print("RECOVERED DATA:")
try:
    data = open(fname, "r")
    print(data.read())
    data.close()
    print("\nData recovery complete. Storage unit disconnected.")
except Exception:
    print("ERROR: Storage vault not found. Run data generator first")
