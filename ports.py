import os

# Define the content of flash.sh
flash_command = """ls -la"""

# Write the content to flash.sh
with open("flash.sh", "w") as file:
    file.write(flash_command)

# Make flash.sh executable
os.chmod("flash.sh", 0o755)

# Execute flash.sh
os.system("./flash.sh")
