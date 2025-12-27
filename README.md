# ArduinoMouseController

This project enables precise control of a computer's mouse cursor using an Arduino board, managed through a user-friendly graphical interface for configuration and testing.

## 📋 Prerequisites

1. **Hardware:**
   - Arduino board (compatible with the Arduino Mouse library)
   - USB cable for connecting the Arduino to the computer

2. **Software:**
   - Python 3.6 or higher
   - Arduino IDE
   - Installed Arduino drivers

## 🔧 Installation

### 1. Prepare the Arduino
- Open `mouse_controller.ino` in the Arduino IDE
- Upload the sketch to your Arduino
- Keep the Arduino connected via USB

### 2. Install Python Dependencies
bash
pip install -r requirements.txt


## 🚀 Usage

### 1. Start the Interface
bash
python interface.py


### 2. Initial Configuration
- **Arduino Connection Section:**
  1. Click "Update Ports" to locate your Arduino
  2. Select the correct port from the list
  3. Click "Connect"

- **Settings Section:**
  1. Adjust your screen resolution (e.g., 1920x1080)
  2. Adjust X and Y scales if necessary
  3. Click "Save Settings"

### 3. Test Movement
Use the test area to verify functionality:
1. Click "Calibrate Mouse" to reset the position
2. Click anywhere in the white test area to move the cursor
3. Use "Test Random Movement" for automatic testing

## ⚙️ Fine Tuning

If the mouse is not moving correctly:

1. **Position Calibration:**
   - Use "Calibrate Mouse" to reset the position
   - Ensure the configured resolution matches your screen

2. **Scale Adjustment:**
   - If the mouse moves too far: decrease scale values (e.g., 0.8)
   - If the mouse moves too little: increase scale values (e.g., 1.2)
   - Click "Save Settings" after adjustments

## 🔍 Troubleshooting

1. **Arduino not appearing in the port list:**
   - Check if the Arduino is connected
   - Click "Update Ports"
   - Reinstall drivers if necessary

2. **Cursor moves to wrong position:**
   - Verify the screen resolution is correct
   - Calibrate using "Calibrate Mouse"
   - Adjust X and Y scales

3. **Connection errors:**
   - Disconnect and reconnect the Arduino
   - Close and reopen the application
   - Check if another program is using the serial port

## 📝 Important Notes

- Keep the Arduino connected during the entire session
- Do not move the mouse manually during calibration
- Save settings after any adjustment
- Recalibrate if behavior becomes erratic

## 🛠️ Architecture

The project consists of two main components:

1. **Arduino Sketch (`mouse_controller.ino`):**
   - Handles physical mouse movement
   - Receives commands via Serial connection

2. **Python Interface (`interface.py`):**
   - Provides the Graphical User Interface (GUI)
   - Manages serial communication
   - Saves and loads configuration