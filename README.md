# Sample-FlaskApp

- Have Docker Installed ***GLOBALLY*** in your system
- Clone the repo in a folder
- Run the command  ***docker build -t "your_tag" .***
- Where docker will build the image and put it in a destination file which is represented here with a dot(***.***)
- Now run  ***docker run -d -p 5000:5000 "your_tag"*** 
- -d in detached mode so that the terminal becomes free
- -p to map your container port with the server port 

### Example code run
![image](./img.png)
