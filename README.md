Service Tracker Sample Website
==============================

This is a sample (and simple) Service and Status tracker website powered by django and celery. The public site is one page that shows all the services statuses and the 10 lastest status notices.

A simple email suscription form is also present. Whenever a service status changes or a new status notice is submitted, an email will be sent asynchronously to all suscribers.
 
 
## Requirements

Requirements for running this project are plain simple:
- Python 2.7.X + pip
- RabbitMQ

*Note: In some systems, the Python development headers, a git client and a C/C++ compilation toolchain would be required.*


## Install

- Install pip using [get-pip.py](https://bootstrap.pypa.io/get-pip.py) if not present
- While virtualenv usage is not mandatory, it's recommended. It's also recommended to install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/).
- Create a virtualenv anywhere (project root might be ideal for testing): `virtualenv env`
- Activate this virtualenv with `source /path/to/env/bin/activate`
- Install python requirements: `pip install -r requirements.txt`
- This project comes with a sample SQLite database already configured. Is you want to use any other, edit `settings/config.py` [accordingly](https://docs.djangoproject.com/en/1.8/ref/settings/#databases) and run `python settings/manage.py migrate` to create the necessary tables.


## Run

- Activate this virtualenv if used.
- Run Celery: `celery -A settings.celery_app worker -l info` (it runs in foregroud and needs to be active so you might need screen or open another shell for the rest).
- Run the website: `python settings/manage.py runserver`


## License

Although there is a copyright symbol in the index page, its purpose is entirely aesthetical.

This software can be distributed under the terms of the BSD License.