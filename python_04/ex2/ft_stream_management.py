import sys
print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
msg = input("Input Stream active. Enter archivist ID: ")
rep_msg = input("Input Stream active. Enter status report: ")
print(f"\n[STANDARD] Archive status from {msg}: {rep_msg}")
sys.stderr.write("[ALERT] System diagnostic: "
                 "Communication channels verified\n")
sys.stdout.write("[STANDARD] Data transmission complete\n")
print("\nThree-channel communication test successful.")
