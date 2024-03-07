# Raspberry Pi OSD Video Recorder

## Overview

This Python script utilizes a Raspberry Pi camera to record video while displaying real-time GPS data and additional information as overlays. The GPS data includes speed, climb, direction, satellite count, and mode. Additional information includes altitude, location, home distance, and recording duration.

## Prerequisites

- Raspberry Pi Zero 2 W and Camera Module 3
- GPS sensor
- Python libraries: picamera, gps, Pillow

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Install the required Python libraries:

   ```bash
   pip install picamera gps Pillow
   ```

3. Download the Roboto font to `/usr/share/fonts/truetype/roboto/Roboto-Regular.ttf`.

4. Set up the necessary directories and files:

   ```bash
   mkdir /home/pi/OSD/
   touch /home/pi/OSD/crosshair.png
   ```

  

## Usage

Run the script by executing:

```bash
python your_script_name.py
```

## Features

- Real-time GPS data overlay on recorded video
- Crosshair overlay for better reference
- Automatic recording with information such as speed, altitude, and more
- Integration with Raspberry Pi camera and GPS sensor

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to the [picamera library](https://picamera.readthedocs.io/) for Raspberry Pi camera access.
- GPS data is obtained using the [gps library](https://pypi.org/project/gps/).


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Author

- [Khaled Salama]((https://github.com/khaled22salama))


