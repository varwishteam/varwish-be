Variable Wishlist
==============
This is a backend side of REST API web-application using [Django](https://www.djangoproject.com/) - a Python Web framework for clean and rapid development. See live version of this project [here](https://varwish-be.heroku.com).


Table of contents
---------------------
  - [Getting Started](#getting-started)
	  - [Prerequisites](#prerequisites)
	  - [Installation](#installation)
	  - [Configuration](#configuration)
  - [Deployment](#deployment)
  - [Documentation](#documentation)
  - [Credits](#credits)


## Getting Started
To get a copy of the project up and running on your local machine follow the these steps. However, this guide is for PyCharm users only. If you choose to use other editor (VSCode) you will need to create virtual environment and install packages manually using these commands:
```bash
git clone https://github.com/varwishteam/varwish-be.git
cd varwish-be
virtualenv venv
source venv/bin/activate
(venv) pip3 install -r requirements.txt
```

### Prerequisites
##### Primary
- [Python 3.7.1](https://www.python.org/downloads/release/python-371/)
- [PyCharm](https://www.jetbrains.com/pycharm/) (latest version)
##### Using VSCode
- [Pip](https://pip.pypa.io/en/stable/) \
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` and `python get-pip.py`
- [virtualenv](https://virtualenv.pypa.io/en/latest/) \
`pip install virtualenv`

### Installation
1. Clone this repository and open up the project in PyCharm \
`git clone https://github.com/varwishteam/varwish-be.git`
3. Create a virtual environment
	1. Navigate to `Settings | Project: {project_name} | Project interpreter`
	2. Click &nbsp;<img src="https://image.flaticon.com/icons/svg/126/126472.svg" height="17" width="17"> &nbsp;| &nbsp;Add...
	3. Choose `New environment` with Location set to root directory and leave everything default
4. Install required packages in `requirements.txt` using project interpreter or you will be asked by IDE

### Configuration
#### Enable Django Support
1. Navigate to  `Settings | Languages & Frameworks | Django`
2. :heavy_check_mark: Enable Django Support
3. Django project root should be `varwish-be` folder
4. Setup the rest as follows:
	* Settings - `varwish\settings.py`
	* Manage script  - `...\varwish-be\manage.py`
	* Environment variables `DJANGO_MODULE_SETTINGS = varwish.settings`
	
> The project uses Heroku's [mLab cloud MongoDB](https://www.mlab.com/) hosting as default database. In order to use different database provider (or use local database) you need to change `DATABASES` in `settings.py`


## Deployment
The live version of the project is currently deployed on [Heroku](https://heroku.com/). Considering you have followed all the above steps the project is ready to be deployed on different Heroku app (see [Heroku docs](https://devcenter.heroku.com/categories/python-support)).

To run development server locally use `python manage.py runserver`, or `Ctrl+Alt+R` in PyCharm then writing `runserver [port or address:port]` and visit https://127.0.0.1:8000/.

## Documentation
