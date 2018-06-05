# Setup

```bash
# Install dependencies
sudo pacman -S python-pip picocom
sudo pip install esptool adafruit-ampy

# Flash the board (16MB does not work for now)
wget http://micropython.org/resources/firmware/esp8266-20180511-v1.9.4.bin
sudo esptool.py --port /dev/ttyUSB0 erase_flash
sudo esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=4MB 0 esp8266-20180511-v1.9.4.bin
```

# Configuration

```bash
cp configuration.json.example configuration.json
```

## Getting a Hue API key

```
./hue-api-key.sh
```

# Deploy

```bash
./deploy.sh
```

# Connecting to the REPL

```bash
sudo picocom /dev/ttyUSB0 --baud 115200
```
