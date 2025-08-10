# Joy-IT SNES Gamepad Raspberry Pi Integration

This repo contains a Python script and systemd service to read inputs from a **Joy-IT SNES Design USB Gamepad** on a Raspberry Pi 4.

## Features
- Detects button presses (including D-pad).
- Automatically reconnects if the gamepad is unplugged and plugged back in.
- Runs as a background service at boot.

---

## Button Layout (Button Numbers in Script)

```
   [3]         [1] [0]
                ○   ○        A  (0)
                              B  (1)
   [2]         [4] [5]       X  (2)
                ○   ○        Y  (3)
                              L  (4)
                              R  (5)
 
      [6]   SELECT            Start   (7)
      [7]   START             Select  (6)
      
         D-Pad Axes:
         Up    → axis 1 = -1.0
         Down  → axis 1 = +1.0
         Left  → axis 0 = -1.0
         Right → axis 0 = +1.0
```

---

## Requirements
```bash
sudo apt-get update
sudo apt-get install python3-pygame git
```

---

## Installation
1. Clone this repo:
```bash
git clone https://github.com/scorqz/joy-it-snes.git
cd joy-it-snes
```

2. Move script to `/usr/local/bin`:
```bash
sudo cp gamepad_monitor.py /usr/local/bin/
sudo chmod +x /usr/local/bin/gamepad_monitor.py
```

3. Install service:
```bash
sudo cp gamepad-monitor.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable gamepad-monitor.service
sudo systemctl start gamepad-monitor.service
```

4. Check service status:
```bash
systemctl status gamepad-monitor.service
```

5. View live button press logs:
```bash
journalctl -u gamepad-monitor.service -f
```

---

## Hotplug Support (Optional)
You can add a udev rule to start/stop the service when the gamepad is plugged in:
```bash
sudo nano /etc/udev/rules.d/99-gamepad.rules
```
Add:
```ini
ACTION=="add", SUBSYSTEM=="input", ATTRS{name}=="*Joy-it Gamepad SNES*", RUN+="/bin/systemctl start gamepad-monitor.service"
ACTION=="remove", SUBSYSTEM=="input", ATTRS{name}=="*Joy-it Gamepad SNES*", RUN+="/bin/systemctl stop gamepad-monitor.service"
```

---

## License
MIT License

