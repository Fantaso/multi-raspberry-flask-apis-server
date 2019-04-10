<!-- logo -->
<a href="https://www.fantaso.de">
<img src="readme/fantaso.png" align="right" />
</a>

<!-- header -->
<h1 style="text-align: left; margin-top:0px;">
  Raspberry API - House Plant Sensor
</h1>

> This project aims for improving API Development using a Raspberry PI as a weather sensor and House Plant sensor. All the Apis are installed on the raspberryPi as a way of communicating to a Client-Side Server where a User can add as many sensors he would have in its house as long as the Raspberry Pi is On and running. The Raspberry PI will be running a server using Flask Micro Framework where all the endpoints of the API will be accessed.





<!-- build -->
<!-- [![Build Status][travis-image]][travis-link] -->

<!-- banner -->
![banner][banner]

<br><br>


## Index:
- #### Overview
    1. Raspberry PI Boot Up
    2. Rasberry PI Flask API's Server
- #### Information:
- #### Maintainer


<br><br>


## Overview:
#### 1. Raspberry PI Boot Up ![raspberrypi][raspberrypi]:

##### Set Up:
    1. Database Set Up:
        If first-time:
            Create, initialize & migrate database
            Create RasberryUser and add default values for sensors

    2. WiFi Set Up:
        Check in database for the authentication data and connects
        to the WiFi router.

    3. Network Set Up:
        Retrieve NIC information and GET Wifi interface available
        Retrieve Ip Address, Netmask and MAC address

    4. Web Server Scan:
        Based on Network Set Up data: Scans the whole network he is connected to and if a WEB SERVER (Client-side) is found.
        It sends a request to be added to the clients list of sensors.

    5. Run "Raspberry PI Flask API's Server"
        Starts the API Server, ready to be registered onto the user-client
        and start sending the data and receiving user-client requests.



<br><br>

#### 2. Rasberry PI Flask API's Server ![Flask-RESTful][Flask-RESTful]:

The resources available from the apis in the raspberry pi are segmented into 4 different API to organized better the architecture and for easy maintainability. the 4 API are:

- Device API
- Shadow API
- Measurement/Timeseries API
- WiFi API

###### A. Device API:
* Endpoint: `/device/`
    * `GET`     > Check if device online


* Endpoint: `/device/register`       
    * `GET`     > returns info for registration on client side
    * `POST`    > register device to belong to a client user


* Endpoint: `/device/deregister`
    * `POST`    > unregistered the device


###### B. Shadow API:
* Endpoint: `/shadow/`
    * `GET`     > returns current status of the device, sensors and alarm


* Endpoint: `/shadow/update`       
    * `PUT/PATCH`     > update soil & weather threshold (min / max, temp, moisture, etc) variables responsible for triggering alarm


###### C. Measurement/Timeseries API:
* Endpoint: `/timeseries/`
    * `GET`     > returns the last measurement


* Endpoint: `/timeseries/latest/<num_measurements>`       
    * `GET`     > returns the last amount of measurements
        implied in the variable <num_measurements>


###### D. WiFi API:
* Endpoint: `/wifi/`
    * `GET`     > returns WiFi information
    * `PUT/PATCH`     > Update WiFi authentication data


<br><br>


## Information:
| Technology Stack |  |  |
| :- | :-: | :- |
| Python          | ![back-end][Python]                   | Back-end |
| Flask           | ![web-framework][Flask]               | Web-framework |
| Flask-RESTful   | ![REST-api][Flask-RESTful]            | RESTful Extension |
| SQLAlchemy      | ![orm][SQLAlchemy]                    | ORM |
| Marschmallow    | ![ De/Serialization][Marschmallow]    | De/Serialization |
| SQLite          | ![database][SQLite]                   | Database |




<br><br>


## Maintainer
Get in touch -–> [fantaso.de][fantaso]



<!-- links -->
<!-- Profiles -->
[github-profile]: https://github.com/fantaso
[linkedin-profile]: https://www.linkedin.com/
[fantaso]: https://www.fantaso.de/

<!-- Repos -->
[github-repo]: https://github.com/Fantaso/multi-raspberry-flask-apis-server
[client-repo]: https://github.com/Fantaso/

<!-- Builds -->
[travis-link]: https://travis-ci.org/
[travis-image]: https://travis-ci.org/

<!-- images -->
[banner]: readme/banner.png
[raspberrypi]: readme/raspberrypi.png
[Python]: readme/python.png
[Flask]: readme/flask.png
[Flask-RESTful]: readme/flaskrestful.png
[Marschmallow]: readme/marshmallow.png
[SQLAlchemy]: readme/sqlalchemy.jpg
[SQLite]: readme/sqlite.png
