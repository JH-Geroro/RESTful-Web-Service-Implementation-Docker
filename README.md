# My RESTful Website + Docker container

Notes: Ensure that the docker is installed on the device and system. If the docker is not install properly, the website will display some errors or maybe not display.

1. Clone my repository from the github
2. Build the new docker image
   sudo docker build -t <templates> .
3. Running the app using this command:
   sudo docker run -p <port>:80 <templates>.

The other way is only simple open the templates file and click any html file to start the website and its router. 
