txt = ("[ENTRY 001] New quantum algorithm discovered"
       "\n[ENTRY 002] Efficiency increased by 347%"
       "\n[ENTRY 003] Archived by Data Archivist trainee")
fname = "new_discovery.txt"
print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
print(f"Initializing new storage unit: {fname}")
print("Storage unit created successfully...\n")
print("Inscribing preservation data...")
data = open(fname, "w")
data.write(txt)
print(txt)
data.close()
print("\nData inscription complete. Storage unit sealed.")
print(f"Archive '{fname}' ready for long-term preservation.")
