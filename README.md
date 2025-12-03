# ECSE 211 Team 18 Project - Delivvery
![Delivvery logo](assets/logo.png)
McGill University - Fall 2025

## Team members
- David
- Emilie
- Jason
- Ralph
- Santiago
- Sarah

## The Mission
Create a robot that can navigate an office, scan rooms and deliver packages.

## The Tech
This project was made using BrickPi, based on the Lego Mindstorms and EV3 Sensors.

The code was made using Python.

## Running the project
Make sure all the proper connections are made to the BrickPi:
```
Motors:
- Left Wheel -> Port "B"
- Right Wheel -> Port "C"
- Conveyor Belt -> Port "D"

Color Sensor -> Port '2'
Touch Sensor -> Port '4'
Gyro Sensor -> Port '1'
```
Then, run the following:
```bash
python3 ./src/robot.py
```

> [!TIP]
> For best results, make sure your battery is fully charged before running the robot. Also, if you want to hear sounds, make sure to have a speaker plugged in and turned on.

## Repository structure
Here is the structure of this project repository
```
.
├── README.md
├── assets
│   └── logo.png
├── data_analysis
│   └── robot-demo-logs.md
├── docs
│   ├── brickpi3.html
│   ├── index.html
│   ├── simpleaudio.html
│   ├── simpleaudio.shiny.html
│   ├── utils.brick.html
│   ├── utils.filters.html
│   ├── utils.html
│   ├── utils.sound.html
│   └── utils.telemetry.html
├── sample_code
│   ├── _sample_defining_devices.py
│   ├── _sample_motors.py
│   ├── _sample_sensors.py
│   ├── _sample_sensors_explained.py
│   ├── collect_color_sensor_data.py
│   └── drumming_software.py
├── scripts
│   └── reset_brick.py
└── src
    ├── color_utils
    │   ├── color_average_finder.py
    │   ├── color_detect.py
    │   └── colors.json
    ├── delivery.py
    ├── office_navigation.py
    ├── office_scanning.py
    ├── robot.py
    ├── utils
    │   ├── __init__.py
    │   ├── brick.py
    │   ├── dummy.py
    │   ├── filters.py
    │   ├── gyro_align.py
    │   ├── remote.py
    │   ├── rmi.py
    │   ├── sound.py
    │   └── telemetry.py
    └── wheels.py
```
And here is a description on some of the important directories/files: 
- `src` contains all of our python code used for our robot. 
    - `src/utils` was copied from the lab and contains all the brickpi libraries. 
    - `src/color_utils` are a special set of utilities made by us in order to accurately detect colors with the color sensor.
    - `delivery.py` contains our `DeliverySystem`, responsible for dropping packages with the conveyor belt and producing sounds.
    - `office_navigation.py` contains our `NavigationSystem`, responsible for navigating from one room to the next and for going back to the mailroom after mission complete.
    - `office_scanning.py` contains two helper functions for scanning a room and detecting red and green stickers
    - `robot.py` is our main program containing the `Robot` class. We run this file whenever we want to run our entire robot and do the full mission.
    - `wheels.py`contains our `Wheels` class with a lot of useful functions for robot movement.
- `docs` contains some useful documentation on the different BrickPi library functions
- `sample_code` was copied over from Labs 1-3, it contains some examples.
- `scripts` contains a useful `reset_brick.py` script. This was copied over from Labs 1-3, but we do not use it in our Robot. We use `utils.brick.reset_brick()` instead.
- `data_analysis` contains our logs from the demo tests
- `assets` contains images and other assets used for this GitHub page.
