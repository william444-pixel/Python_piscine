print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
try:
    with open("lost_archive.txt", "r") as valut:
        valut.read()
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")
print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
try:
    with open("classified_vault.txt", "r") as valut:
        valut.read()
except PermissionError:
    print("RESPONSE: Security protocols deny access\n"
          "STATUS: Crisis handled, security maintained\n")
print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
try:
    with open("standard_archive.txt", "r") as valut:
        print(f"SUCCESS: Archive recovered - '{valut.read()}'")
        print("STATUS: Normal operations resumed")
except Exception as e:
    print(e)
print("\nAll crisis scenarios handled successfully. Archives secure.")
