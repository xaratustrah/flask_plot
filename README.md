# flask_plot

Webapp excercise on using [Flask](http://flask.pocoo.org/), based on the [Flask4Scientists](https://github.com/hplgit/web4sciapps) tutorial by [@hplgit](https://github.com/hplgit). Also using [Flask_Bootstrap](http://getbootstrap.com/). I have changed some lines to adapt the code to python3 syntax. many thanks goes to this tutorial:
[Hosting flask on linux with gunicorn and nginx](http://blog.stjepanbrkic.com/hosting-flask-on-linux-with-gunicorn-and-nginx/)




## Setting up a full stack python server with nginx, gunicorn and systemd on Rasperry Pi

First we need to install a couple of things:

    sudo apt-get update && sudo apt-get upgrade

Installing `nginx` will fail if apache is running. If your installation breaks half ways, then remove the fragments, stop apache and then install nginx again:

    sudo apt-get remove nginx* --purge
    sudo /etc/init.d/apache2 stop
    sudo apt-get install nginx-common
    sudo apt-get install nginx


then install the rest:

    sudo pip3.4 install flask-bootstrap wtforms gunicorn


create a file `/etc/nginx/sites-enabled/flask_plot.conf` with this content:

    server {  
            listen   8000; ## listen for port 8000
            location / {
            include proxy_params;
            proxy_pass http://unix:/home/pi/git/flask_plot/flask_plot_socket.sock;
        }
    }


now restart nginx server:

    sudo service nginx restart

now create a service in `/etc/systemd/system/flask_plot.service` with the content:


    [Unit]
    Description=Unicorn Daemon for flask_plot 
    After=network.target
    
    [Service]
    User=pi
    Group=www-data  
    WorkingDirectory=/home/pi/git/flask_plot
    ExecStart=/usr/local/bin/gunicorn --workers 1 --bind unix:/home/pi/git/flask_plot/flask_plot_socket.sock controller:app
    
    ExecReload=/bin/kill -s HUP $MAINPID  
    ExecStop=/bin/kill -s TERM $MAINPID
    
    
    [Install]
    WantedBy=multi-user.target


now run:

    sudo systemctl daemon-reload && sudo systemctl enable flask_plot  


now you can start / stop the daemon like any other service.

    sudo service flask_plot start
    sudo service flask_plot stop


have fun!


p.s. at some point it might be beneficial to have a `virtual_env` for your python environment.
