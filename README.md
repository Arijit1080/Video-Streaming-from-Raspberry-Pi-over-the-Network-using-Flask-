# Video Streaming from Raspberry Pi over the Network using Flask
Using this codes you can stream video from a raspberry pi over the network using a Flask based web platform. So, if you host the server side code on a server, then you can access the video from anywhere in the world.

## Dependencies

1. Python 3
2. Flask (tested with 1.1) [server side]
3. gunicorn [server side]

## Setups
Store the following files in the server side:
1. app.py
2. base_camera.py
3. video_server.py

Store the following file in the Raspberry Pi:
1. pi_video_client.py


## Run 

In the server
```
gunicorn --threads 5 --workers 1 --bind 0.0.0.0:5000 app:app		
```

1. Change the threads number according to your needs. If thread no is x, then only x no of people will be able to watch the stream simultaneously.
2. Change the port number (5000) according to your needs.

After running the server side code, you can run the code in Raspberry Pi.

In Raspberry Pi
```
python pi_video_client.py ip_address_of_server port_number #use the same port number used 'inside video_server.py', in my case 4444
```

Now open 0.0.0.0:5000 in browser[server public ip and port number, if you have hosted it there]

<p align="center">
<a href="#"><img src="map2.gif" alt="" width="480" height="360"></a>
</p>
</br></br>


## Credit
https://blog.miguelgrinberg.com/post/flask-video-streaming-revisited
