import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import serial.tools.list_ports
import subprocess

def flash_8051():
    hex_file_path = hex_file_entry.get()
    selected_chip = get_selected_chip()
    port_name = selected_port  # Use the selected port
    
    # Write the command to flash.sh
    flash_command = f"""/Users/rohansingh/Downloads/Arduino.app/Contents/Java/hardware/tools/avr/bin/avrdude \
-C /Users/rohansingh/Desktop/AVR8051.conf \
-c stk500v1 \
-P {selected_port} \
-p {selected_chip} \
-b 19200 \
-U flash:w:{hex_file_path}:a
"""
    # Execute flash.sh asynchronously
    subprocess.Popen(flash_command)




def refresh_serial_ports():
    ports = [port.device for port in serial.tools.list_ports.comports()]
    port_dropdown["values"] = ports

def on_select(event=None):
    global selected_port
    selected_port = port_dropdown.get()

def get_hex_file():
    file_path = filedialog.askopenfilename()
    hex_file_entry.delete(0, tk.END)
    hex_file_entry.insert(0, file_path)

def get_selected_chip():
    selected_chip = ""
    if chip_var.get() == 1:
        selected_chip = "89s51"
    elif chip_var.get() == 2:
        selected_chip = "89s52"
    elif chip_var.get() == 3:
        selected_chip = chip_other_entry.get()
    return selected_chip



root = tk.Tk()
root.title("Flash 8051")
root.geometry("800x300")

# Hex File Path
hex_file_label = tk.Label(root, text="Path of HEX File:")
hex_file_label.grid(row=0, column=0, padx=10, pady=5)

hex_file_entry = tk.Entry(root, width=50)
hex_file_entry.grid(row=0, column=1, padx=10, pady=5)

browse_button = tk.Button(root, text="Browse", command=get_hex_file)
browse_button.grid(row=0, column=2, padx=10, pady=5)

# Selected Chip
chip_var = tk.IntVar()

chip_label = tk.Label(root, text="Select Chip:")
chip_label.grid(row=1, column=0, padx=10, pady=5)

chip_at89s51 = tk.Radiobutton(root, text="AT89S51", variable=chip_var, value=1)
chip_at89s51.grid(row=1, column=1, padx=0, pady=5)

chip_at89s52 = tk.Radiobutton(root, text="AT89S52", variable=chip_var, value=2)
chip_at89s52.grid(row=1, column=2, padx=0, pady=5)

chip_other = tk.Radiobutton(root, text="Other", variable=chip_var, value=3)
chip_other.grid(row=1, column=3, padx=0, pady=5)

# Port Name
port_label = tk.Label(root, text="Select Port:")
port_label.grid(row=2, column=0, padx=10, pady=5)

port_dropdown = ttk.Combobox(root)
port_dropdown.grid(row=2, column=1, padx=10, pady=5)

refresh_button = ttk.Button(root, text="Refresh Ports", command=refresh_serial_ports)
refresh_button.grid(row=2, column=2, padx=10, pady=5)

port_dropdown.bind("<<ComboboxSelected>>", on_select)

# Flash Button
flash_button = tk.Button(root, text="Flash 8051", bg="green", fg="green", command=flash_8051)
flash_button.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Refresh the serial port list initially
refresh_serial_ports()

root.mainloop()
