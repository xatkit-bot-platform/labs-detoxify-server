# labs-detoxify-server
Detoxify server for Xatkit

## Instructions

1. Open a new terminal and clone this repository
2. Install ```python-virtualenv``` to create an environment where you will install all necessary packages in isolation.
```
//Debian, Ubuntu
$ sudo apt-get install python-virtualenv
//CentOS, Fedora
$ sudo yum install python-virtualenv
//Arch
$ sudo pacman -S python-virtualenv
```
3. Navigate to the repository folder and [install detoxify in a virtual environment](https://github.com/unitaryai/detoxify#how-to-run)
4. Install Flask.
```
$ pip install Flask
```
5. Run ```$ gedit toxic-env/bin/activate``` to edit it. At the end of the file you have to define some environment variables used by Flask.
```
export FLASK_APP="run_detoxify_server.py"
export FLASK_ENV="development"
# Set the port you want to use in the server, or delete the next line if you want to use the default port
export FLASK_RUN_PORT=8000
```
6. Run again ```$ source toxic-env/bin/activate``` to apply the changes in step 5.
7. Run the Flask server.
```
$ flask run
```
For more information about Detoxify, [visit its repository](https://github.com/unitaryai/detoxify)
