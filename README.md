# Pyropulse
AI-driven early detection systems and autonomous technology revolutionize wildfire management
# AI-Driven Wildfire Detection and Autonomous Drone Management System

## Overview

Welcome to our GitHub repository! This project focuses on leveraging artificial intelligence for early wildfire detection and management through autonomous drone technology. By integrating machine learning algorithms with an advanced drone setup, we aim to revolutionize wildfire monitoring and response systems.

## Table of Contents
1. [Introduction](#introduction)
2. [Hardware Components](#hardware-components)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

Wildfires pose significant threats to the environment and communities. Our project combines state-of-the-art drone technology with machine learning to create an early detection and autonomous response system. The repository includes code for the drone's flight control, camera integration, and the machine learning model responsible for wildfire detection.

## Hardware Components

To build the autonomous drone system, you will need the following hardware components:

- LiteRadio 2 SE Radio
- F4 1S 12A AIO Brushless Flight Controller
- Pavo20 Brushless Whoop Frame
- Gemfan 2015 2-Blade Propellers
- Pavo Series COB LED Strip
- 1103 Brushless Motors 11000KV
- Raspberry Pi Zero 2 W
- Raspberry Pi Camera Module 3
- 900 mAh 2S Li-Po battery
- 2 resistors for a 5V to 3.3V voltage divider
- Soft sponge and rubber bands for mounting and dampening vibrations
- VR02 FPV Goggles
- DarwinFPV 5.8Ghz 25-200mW VTX for Baby Ape

## Installation

Follow these steps to set up the AI-driven wildfire detection system:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/khaled22salama/Pyropulse.git
   ```


2. Connect and configure the hardware components according to the provided documentation.
   ![interface](Drone/interface.png)

## Usage

1. Upload the drone control code to the flight controller.
2. Integrate the camera code with the Raspberry Pi Camera Module 3.
3. Deploy the machine learning code for wildfire detection on the Raspberry Pi Zero 2 W.
4. Power up the drone, ensuring all components are functioning correctly.

Check the code for [Drone](Drone)
check the code for [machine learning model & dataset](Dataset)


## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your own projects.

Thank you for your interest in our AI-driven wildfire detection and autonomous drone management system! If you have any questions or issues, please don't hesitate to [open an issue](https://github.com/khaled22salama/Pyropulse/issues).
