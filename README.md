# TechCare

TechCare Baby Safe, an IoT solution to improve security and access to neonates, with Face recognition using Thundercomm's AI kit
<img src="https://hackster.imgix.net/uploads/attachments/686206/techcare_m01IlSQOOe.jpg?auto=compress%2Cformat&w=900&h=675&fit=min">


# Table of contents
* [Introduction](#introduction)
* [Problematic](#problematic)
* [Our Solution](#our-solution)
* [Thundercomm AI Kit Setup](#thundercomm-ai-kit-setup)
* [Arduino Setup](#arduino-setup)
* [Raspberry Setup](#raspberry-setup)
* [The Final Lock Module](#the-final-lock-module)
* [Results](#results)
* [Future Rollout](#future-rollout)
* [References](#references)


## Problematic:

According to the BBC, chinese police reports that 20,000 babies were stolen yearly in China. But this number might be 10 times bigger, because of the lack of information. In China a baby girl can be sold for 8,000 US dollars, meanwhile a baby boy is twice the price.

Most of them disappear, but some others are sold or used as work slaves.

https://www.bbc.com/news/blogs-trending-35383319

In Mexico the number is not that high, but in the latest 9 years that number reaches 25 358 according to Registro Nacional de Personas desaparecidas, being 2017 the year with more kids kidnaped. 70% of that number were babies between 0 and 5 years.

https://www.imagenradio.com.mx/un-delito-que-crece-en-mexico-el-robo-de-ninos-y-su-desaparicion

https://www.csmonitor.com/1994/0630/30061.html

<img src= "https://hackster.imgix.net/uploads/attachments/686210/pasted_image_0.png?auto=compress%2Cformat&w=740&h=555&fit=max">

This is a huge problem all around the world, first because of the lack information. Authorities (talking about statistics) do not show the whole information, and also Medical providers are not aware of the problem they are facing. The System used nowadays is just a door with a lock, the most secure hospitals having an RFID control, and the ones that do not have anything, barely have a door handle.

What we know for sure, is that this number of missing babies can be reduced drastically, helping families and saving those lives.
<img src= "https://hackster.imgix.net/uploads/attachments/686213/pasted_image_0.png?auto=compress%2Cformat&w=740&h=555&fit=max">

## Our Solution:

<img src="https://i.ibb.co/f8GGL6H/Esquema.png">

Nuestra solucion se basa en el reconocimiento facial del personal de enfermeria para darle acceso a la habitacion donde estan los bebes, todo esto de forma automatizada, ademas de incluir la entrada manual de un codigo para poder acceder al cuarto.

Bill of materials.
- Thundercomm AI Kit.
- Raspberry Pi Zero w.
- Arudino Uno.
- Servo Motor MG995.
- Numeric Keyboard.

Optional:
- Solenoid Electrolock.
- Darlington Transistor.
- 10k Resistor.
- 2 Power Banks. 5v 10000mAh.

Software:
- Python.
- Watson IoT Platform.
- Raspbian.
- Android Studio

## Thundercomm AI Kit Setup:

DOKI

## Arduino Setup:

2. Para la configuracion del Arduino solo tenemos que conectar nuestro Servo a nuestro arduino en el pin 10 como lo pusimos en nuestro cogido en la carpeta ArduinoSoft.

2.1 La cerradura con el servo se hizo a mano de la siguiente forma.

<img src="https://i.ibb.co/302CPJ5/IMG-9877.jpg"> 

2.2 El diagrama de conexiones sera el siguiente.

<img src="https://i.ibb.co/HrWPxDc/Esquema1.png"> 

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

## The Final Lock Module:

El dispositivo final una vez combinando la raspberry y el arduino quedaron de la siguiente manera.

<img src="https://i.ibb.co/YXzHxXT/IMG-9887.jpg"> 

- Se puede ver que tiene dos powerbanks para ser las fuentes de poder de el dispositivo y asi poderlo hacer inalambrico, en el caso de un hospital ya estaria integrado para tener una alimentacion directa del hospital.

Video: Click on the image

[![Tech Lock Demo Tech](https://img.freepik.com/free-vector/locker_53876-25496.jpg?size=338&ext=jpg)](https://www.youtube.com/watch?v=nQ5k8VPnbZA&feature=youtu.be)

## Results:

## Future Rollout

- We will recommend to adapt a webcamera or another usb camera to the thundersoft as its camera is only 8M pixels and not that powerful.
- The AI Kit is quite powerful and we have to delve even deeper in its capabilities.
- Deployment in a clinical situation.

Known issues and thoughts

- Face recognition via OpenCV is not that accurate, we have to work on that.
- Have to train a model much more, perhaps processing the image on Edge and then use a service like Rekognition from AWS or IBM recognition would be in order. 

## References:
