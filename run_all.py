import subprocess
import time

# List of your scripts
scripts = ["producer.py",  "mongo.py", "fraud.py"]
processes = []

print("🚀 Starting the MaraStream Pipeline...")

for script in scripts:
    p = subprocess.Popen(["python", script])
    processes.append(p)
    print(f"✅ Started {script}")
    time.sleep(2) # Give each script a second to connect

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Shutting down pipeline...")
    for p in processes:
        p.terminate()