![Rester](https://raw.githubusercontent.com/schartz/rester/master/src/main/icons/linux/128.png)


# Rester
A slick REST API client. Native application built with PyQt5. Cross-platform, runs on Windows, Linux and Mac.  
At the moment Rester is under heavy development. Not meant for production use.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See _building installers_ for notes on how to deploy the project on a live system.

### Prerequisites

You will need following to get started.

```
Python 3.6+
Virtualenvwrapper
PyQt5
Qt Designer
```

### Development Environment Setup

Start by creating a virtualenv for the project.

```
mkvirtualenv rester
workon rester
```

Install dependencies

```bash
pip install PyQt5
pip install urllib3
pip install fbs
```

Clone this repository
```bash
git clone https://github.com/schartz/rester.git
```
Run the app

```
python src/main/python/main.py
```

And hack away!
## Running the tests

Testing will be added shortly. At the moment project has no tests whatsoever.


## Building Installers

Rester uses [fman build system](https://build-system.fman.io/).  
Refer to the [fman build system](https://build-system.fman.io/) docs for instructions about building installers.  
If there is any custom configuration in future, it will be added here in this README itself.


## Built With
* [Python](https://www.python.org/) - Python3.6, duh!
* [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5) - GUI Library
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE of choice
* [urllib3](https://github.com/urllib3/urllib3) - HTTP calls

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Schartz Rehan** - *Initial work* - [Twitter](https://twitter.com/schartzium)

## License

This project is licensed under the GPL License.

## Acknowledgments

* Thanks Flat Icons for the application Icon.
* Thanks brilliant folks behind urllib3
* Thanks a ton [Riverbank Computing Limited](https://www.riverbankcomputing.com) for providing us with PyQt
* A big shout out to [Michael Herrmann](http://www.herrmann.io/) for awesome fman build system.
* Thanks [Gregor](https://github.com/GrxE/PyQJsonModel) for PyQtJsonModel
