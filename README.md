<!-- PROJECT SHIELDS -->
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/EdwinHuitz/python-applets">
    <img src="images/python_logo.png" alt="Logo" width="300" height="80">
  </a>
  <h3 align="center">Python Applets</h3>

  <p align="center">
    A continuously growing set of small single purpose applets. Each of which are completely written in Python 3, with some using 3rd party libraries.
    <br />
    <a href="https://github.com/EdwinHuitz/python-applets"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/EdwinHuitz/python-applets/issues">Report Bug</a>
    ·
    <a href="https://github.com/EdwinHuitz/python-applets/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built Using](#built-using)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<br/>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This entire repo is and alway will be a work in progress, including this readme. Which means each applet is subject to change over time as I discover new and better ways to optimize them both visually and functionally. I will try my best to contiuously optimize and add more applets on a consistent basis, but I will not push any incomplete applets to the live repo. Which means that there may seem to be inactivity for brief periods between each push. Anyone who wishes to add their applets to this repo or submit bug fixes to mine may feel free to do so. All you need to do is simply fork this repo and send me a pull request.


<br/>

### Built Using

* [Python 3.8](https://www.python.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)
* [PyAutoGUI](https://github.com/asweigart/pyautogui)

<br/>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running you must follow these simple steps.

### Prerequisites

In order to use these applets you must first ensure the correct version of Python is installed alongside the correct 3rd party libraries.

<br/>

* Python 3.8
```sh
sudo apt-get install python3.8
```
* PySimpleGUI (for using the email applet's UI)
```
pip3 install pysimplegui
```
* PyAutoGUI (for using the automated mouse applet)
```
pip3 install pyautogui
```
* PyTest (for testing your answers on python challenges)
```
pip3 install pytest
```

<br/>

### Installation

1. Clone the repo to your local machine
```sh
git clone https://github.com/EdwinHuitz/python-applets.git
```

2. Change to the appropriate directory where the applet is located by using your console
```sh
cd python_applets/covid
```

3. Use your console to run the appropriate script of which you'd like to use*
```sh
python covid_ui.py
```

_*Each applet can be run with or without using the User Interface. But I strongly reccomend using the UI in order for you to have the most optimal experience_

<br/>

<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<br/>

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/EdwinHuitz/python-applets/issues) for a list of proposed features (and known issues).

<br/>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<br/>

<!-- LICENSE -->
## License

Distributed under the GNU General Public License. See `LICENSE` for more information.

<br/>

<!-- CONTACT -->
## Contact

Edwin Huitz - Twitter [@EdwinHuitz](https://twitter.com/EdwinHuitz) or via [LinkedIn](https://www.linkedin.com/in/edwin-huitz)

Project Link: [https://github.com/EdwinHuitz/python-applets](https://github.com/EdwinHuitz/python-applets)

<br/>

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Othneil Drew for Best-README-Template](https://github.com/othneildrew/Best-README-Template)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-round&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/edwin-huitz/

[issues-shield]: https://img.shields.io/github/issues/EdwinHuitz/python-applets
[issues-url]: https://github.com/EdwinHuitz/python-applets/issues

[license-shield]: https://img.shields.io/github/license/EdwinHuitz/python-applets
[license-url]: https://github.com/EdwinHuitz/python-applets/blob/main/LICENSE.txt

[forks-shield]:https://img.shields.io/github/forks/EdwinHuitz/python-applets
[forks-url]:https://github.com/EdwinHuitz/python-applets/forks

[twitter-shield]:https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FEdwinHuitz
[twitter-url]:https://twitter.com/EdwinHuitz

[product-screenshot]: images/screenshot.png
