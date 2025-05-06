import os
from datetime import datetime, timedelta

# Base directories (Updated to use /home/vagrant instead of /home/ubuntu)
base_dirs = [
    "/home/vagrant/projects/spriced-backend/sim-spriced-resources/docker-compose/kafka/data/processed/",
    "/home/vagrant/projects/view_export_csv/"
]

# Function to create file with a specific filename in each target dir
def create_files_with_timestamp(filename):
    for base_dir in base_dirs:
        temp_dir = os.path.join(base_dir, "temp")
        os.makedirs(temp_dir, exist_ok=True)
        full_path = os.path.join(temp_dir, filename)
        with open(full_path, 'w') as f:
            f.write("column1,column2,column3\n")
            f.write("value1,value2,value3\n")
        print(f"File created: {full_path}")

# Start from a base datetime in the past
base_time = datetime(2020, 1, 1, 0, 0, 0)

# Generate 20 files with varying years/months
for i in range(20):
    # Spread timestamps by ~3 months each
    future_time = base_time + timedelta(days=i * 90)

    # Epoch values
    epoch_seconds = int(future_time.timestamp())
    epoch_millis = int(future_time.timestamp() * 1000)

    # Rotate timestamp formats
    if i % 4 == 0:
        timestamp = future_time.strftime("%Y%m%d%H%M")  # yyyyMMddHHmm
    elif i % 4 == 1:
        timestamp = future_time.strftime("%Y-%m-%d_%H-%M-%S")  # yyyy-MM-dd_HH-mm-ss
    elif i % 4 == 2:
        timestamp = str(epoch_millis)  # Epoch in milliseconds
    else:
        timestamp = str(epoch_seconds)  # Epoch in seconds

    filename = f"export_{timestamp}.csv"
    create_files_with_timestamp(filename)
