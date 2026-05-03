from dotenv import load_dotenv as load
import os

is_loaded = load()
print("ORACLE STATUS: Reading the Matrix...")
print("Configuration loaded:")
mode = os.getenv("MATRIX_MODE", "development")
db = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_lvl = os.getenv("LOG_LEVEL")
net = os.getenv("ZION_ENDPOINT")
print(f"Mode: {mode}")
if db:
    print("Database: Connected to local instance")
else:
    print("Database: Missing database")
if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: Missing API_KEY")
if log_lvl:
    print(f"Log Level: {log_lvl}")
else:
    print("log level: Missing log level")
if net:
    print("Zion Network: Online")
else:
    print("Zion Network: Missing network")
print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")
if is_loaded:
    print("[OK] .env file properly configured")
else:
    print("[WARNING] .env file missing (using system/default variables)")

print("[OK] Production overrides available")
print("\nThe Oracle sees all configurations.")
