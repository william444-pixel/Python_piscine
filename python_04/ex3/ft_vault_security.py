print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
print("Initiating secure vault access...\n"
      "Vault connection established with failsafe protocols\n")
print("SECURE EXTRACTION:")
with open("classified_data.txt", "r") as valut:
    print(valut.read())
print("\nSECURE PRESERVATION:")
msg = "[CLASSIFIED] New security protocols archived"
with open("test.txt", "w") as valut:
    valut.write(msg)
    print(msg)
    print("Vault automatically sealed upon completion")
print("\nAll vault operations completed with maximum security.")
