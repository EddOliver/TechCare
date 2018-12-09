# TechCare
TechCare Baby Safe, an IoT solution to improve security and access to neonates, with Face recognition using Thundercomm's AI kit


# Table of contents
* [Introduction](#introduction)
* [Problematic](#problematic)
* [Our Solution](#our-solution)
* [Thundercomm AI Kit Setup](#thundercomm-ai-kit-setup)
* [Arduino Setup](#arduino-setup)
* [Raspberry Setup](#raspberry-setup)
* [Results](#results)
* [Future Rollout](#future-rollout)
* [References](#references)

## Introduction:

## Problematic:

## Our Solution:

<img src="https://i.ibb.co/f8GGL6H/Esquema.png">

Nuestra solucion se basa en el reconocimiento facial del personal de enfermeria para darle acceso a la habitacion donde estan los bebes, todo esto de forma automatizada, ademas de incluir la entrada manual de un codigo para poder acceder al cuarto.

Bill of materials.
- Thundercomm AI Kit.
- Raspberry Pi Zero w.
- Solenoid Electrolock.
- Darlington Transistor.
- 10k Resistor.

Software:
- Python.
- Watson IoT Platform.
- Raspbian.

## Thundercomm AI Kit Setup:

DOKI

## Arduino Setup:

2. Para la configuracion del Arduino solo tenemos que conectar nuestro Servo a nuestro arduino en el pin 10 como lo pusimos en nuestro cogido en la carpeta ArduinoSoft

## Raspberry Setup:

3. For this point, it's also possible to use an Electronic Lock, RaspberryPi Zero w and TCP120, instead of our Servo lock with Arduino and Raspberry Pi connecting it through MQTT.

3.1. Download the operating system of the Raspberry Pi Zero.

- To download the operating system of the Raspberry enter the following link:
- Link: https://downloads.raspberrypi.org/raspbian_lite_latest
- We will download the lite version.

3.2. Flash the operating system in the SD as shown in point 1.2 but with raspbian.

- Through Etcher flash the raspberry operating system but DO NOT put it inside the raspberry yet.

3.3. Create a wpa_supplicant for the connection of the raspberry to the internet.

- Since we have flashed the operating system, we copy and paste the files from the "RaspberryPi" folder directly into the SD card.
- Then we open the "wpa_supplicant.conf" file with a text editor
- In between the quotes in the ssid line write your wifi network and in psk the network key.

        country = us
        update_config = 1
        ctrl_interface =/var/run/wpa_supplicant

        network =
        {
        scan_ssid = 1
        ssid = "yourwifi"
        psk = "yourpassword"
        }


- We save the changes and remove the SD from the PC.

3.4. We then place the SD in the raspberry and connect it to its power source.

- The power source of a Raspberry Pi Zero is recommended to be from 5 volts to 1A minimum. We recommend the official ower supply for the Raspberry pi.

3.5. Once the Raspberry has already started, we need to access it through SSH or with a keyboard and a monitor.

- If you want to access it through SSH we need your IP.
- In order to analyze your network and obtain the number we will have to use one of the following programs.
- Advanced IP Scanner (Windows) or Angry IP Scanner program (Windows, Mac and Linux).
- In the following image you can see how we got the Raspberry IP.

<img src="https://i.ibb.co/KLThvst/AngryIP.png"> 

3.6. Copy the program inside the "RaspberrySoft" folder using FileZilla to the raspberry.

- To pass the file via wifi to the raspberry we have to download another program called "FileZilla".
- Link: https://filezilla-project.org/download.php?type=client
- Once we have the program, we open it and input the following data in the upper bar to access the raspberry.

Host: RASPBERRYIP              Username:pi           Password:raspberry             port:22

<img src="https://i.ibb.co/4Y80V96/filezilla.png"> 

- Press Quickconnect.
- Once we enter the Raspberry, we copy the file "exe.py and exe2.py" in the folder "/home/pi".

3.7. Since we have the file in the raspberry, now we have to connect the raspberry with ssh.

- To connect using ssh to the raspberry we need the Putty program.
- Link: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
- This program will let us access the command console of the raspberry.
- In Linux, just open the terminal and put the following command.

        ssh pi@RASPBERRYIP

<img src="https://i.ibb.co/PxP86Xz/terminal.png">

- Password: “raspberry”

<img src="https://i.ibb.co/NthRqRc/terminal2.png">

3.8. First, we will install the necessary libraries for our program to work.

- For it to work we just have to input the following command.

      sudo apt-get update && sudo apt-get install -y python-pip && pip install ibmiotf

- This command will install the IBM Watson IoT library

3.9. Once the console is open, we will edit the file used in the previous paragraph to configure the IP of the Ultra96.

- In the Raspberry's terminal we will write the following command.
     
    sudo nano exe2.py

<img src="https://i.ibb.co/JCpSFDJ/terminalcomand.png">

- The command will open the text editor where we can go through the file "exe2.py".

- We change the Watson IoT credentials with our application credentials.

- To create a Watson IoT application you can follow this one:

https://github.com/altaga/The-Ultimate-IBM-Watson-IoT-Platform-Guide

- Since we changed that text, we will save the changes made by pressing "ctrl + o" and enter, and to exit the editor pressing "ctrl + c".

3.10. Input boot program for the Raspberry Zero.
In order for the program to start together with raspbian, and for us to no longer need to execute it, we will write the following command.

    sudo nano /etc/rc.local

- Inside the file we will have to write the following to start both programs:

      sudo python /home/pi/exe.py &
      sudo python /home/pi/exe2.py &

- After adding that text, we will save the changes made by pressing "ctrl + o" and enter, to exit the editor press "ctrl + c".

3.11. Once we have finished editing this file, we are ready to connect everything.
Before proceeding, disconnect the raspberry and the arduino from their sources because we are going to connect them to each other.

## Results:

## Future Rollout

## References:
