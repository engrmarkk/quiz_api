# Quiz_Api

<!-- Back to Top Navigation Anchor -->

<a name="readme-top"></a>


<!-- https://user-images.githubusercontent.com/100721103/200149633-373db975-c47f-43a7-9288-f6cbd16e0410.mp4 -->

<br><br>
<!-- Project Shields -->
<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Twitter][twitter-shield]][twitter-url]
[![Twitter][twitter-shield2]][twitter-url2]

</div>

<br />

<div>
  <p align="center">
    <a href="https://github.com/engrmarkk/Quiz_Api#readme"><strong>Explore the docs »</strong></a>
    <br />
    ·
    <a href="https://github.com/engrmarkk/Quiz_Api/issues">Report Bug</a>
    ·
    <a href="https://github.com/engrmarkk/Quiz_Api/issues">Request Feature</a>
  </p>
</div>

---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-Quiz_Api">About the project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#exposure">Exposure</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
         <li><a href="#user's-endpoints">User's endpoints</a></li>
      </ul>
    <!-- <li><a href="#shots">Shots</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the Blog -->

## About Quiz_Api

The Quiz API project is a cutting-edge platform that provides a comprehensive solution for creating and delivering quizzes. This Quiz API offers a range of features,
such as database of questions on a variety of topics, and the ability to track results and progress. It also ensures that users won't be able to take the quiz twice,
providing a secure and reliable experience.


<p align="right"><a href="#readme-top">back to top</a></p>

### Built With:

![Python][python]
![Flask][flask]
![SQLite][sqlite]

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Lessons from the Project -->

## Exposure

Creating this project got me more exposed to:

- Debugging
- Team work
- Collaboration
- Database Management
- Authentication
- Authorization
- Endpoint restriction


<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- GETTING STARTED -->

## Usage

To get a local copy up and running, follow the steps below.

### Prerequisites

Python3: [Get Python](https://www.python.org/downloads/)

### Installation

1. Clone this repo
   ```sh
   git clone https://github.com/engrmarkk/Quiz_Api.git
   ```
2. Navigate into the directory
   ```sh
   cd Quiz_Api
   ```
3. Create a virtual environment
   ```sh
   python -m venv your_venv_name
   ```
4. Activate the virtual environment on powershell or cmd
   ```sh
   your_venv_name\Scripts\activate.bat
   ```
   On Bash ('Scripts' for windows, 'bin' for linux)
   ```sh
   source your_venv_name/Scripts/activate.csh
   ```
5. Install project dependencies
   ```sh
   pip install -r requirements.txt
   ```
6. Run Flask
   ```sh
   flask run
   ```
7. Open the link generated in the terminal on a browser
    ```sh
   http://127.0.0.1:5000/
   ```
   <br>
### Project structure
   ```
   .
   ├── README.md
   ├── app.py
   ├── .env
   ├── .gitignore
   ├── LICENSE
   ├── quiz
   │   ├── __init__.py
   │   ├── auth
   │   │   ├── __init__.py
   │   │   ├── users.py
   │   └── config
   │   │   ├── __init__.py
   │   │    ├── configuration.py
   │   └── extensions
   │   │   ├── __init__.py
   │   └── models
   │   │   ├── __init__.py
   │   │   ├── answers.py
   │   │   ├── is_answered.py
   │   │   ├── options.py
   │   │   ├── questions.py
   │   │   ├── users.py
   │   └── resources
   │   │   ├── __init__.py
   │   │   ├── answer.py
   │   │   ├── options.py
   │   │   ├── questions.py
   │   └── schemas
   │   │   ├── __init__.py
   │   │   ├── answer.py
   │   │   ├── option.py
   │   │   ├── question.py
   │   │   ├── user.py
   ├── your_venv_name
   ├── requirements.txt
   └── run.py
   ```  


### User's endpoints
<br>
POST (Register) http://127.0.0.1:5000/user/register

REQUEST
```json
{
  "email": "mark@mark.com",
  "password": "password",
  "first_name": "mark",
  "last_name": "mark",
  "username": "mark"
}
```
RESPONSE
```json
{
    "id": 1,
    "email": "mark@mark.com",
    "first_name": "mark",
    "last_name": "mark",
    "username": "mark"
}
```
POST (Login) http://127.0.0.1:5000/users/login

REQUEST
```json
{
  "username": "mark",
  "password": "password"
}
```
RESPONSE
```json
{
    "access_token": "eyJhbGciOiJIUzIEyMjMtNj...................",
    "refresh_token": "eyJhbGciOiJIUzLyADmyXA...................."
}
```
GET (Get all users) http://127.0.0.1:5000/user/users

RESPONSE
```json
[
    {
        "id": 1,
        "email": "mark@mark.com",
        "first_name": "mark",
        "last_name": "mark",
        "username": "mark",
        "scores": 0,
        "is_admin": false,
        "taken": false
    }
]
```
GET (Get specific user) http://127.0.0.1:5000/user/user/1

RESPONSE
```json
{
    "id": 1,
    "email": "mark@mark.com",
    "first_name": "mark",
    "last_name": "mark",
    "username": "mark",
    "scores": 0,
    "is_admin": false,
    "taken": false
}
```

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Sample Screenshot -->

<!-- ## Shots -->

<!-- <br /> -->
<!-- <p>Light Mode</p> -->

<!-- [![My Blog Project Screenshot][Quiz_Api-screenshot]](https://github.com/engrmarkk/Quiz_Api/blob/main/static/images/screen-light.png) -->

<!-- <br/> -->
<!-- <p>Dark Mode</p> -->

<!-- [![My Blog Project Screenshot][Quiz_Api-screenshot2]](https://github.com/engrmarkk/Quiz_Api/blob/main/static/images/screen-dark.png) -->

<br/>

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Contact -->

## Contact

Adeniyi Olanrewaju - [@iamengrmark](https://twitter.com/iamengrmark) - adeniyiboladale@yahoo.com <br>
Gabriel Kalango - [@GabrielKalango](https://twitter.com/GabrielKalango) - kallythegreat11@gmail.com

Project Link: [Quiz Api](https://github.com/engrmarkk/Quiz_Api)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Acknowledgements -->

## Acknowledgements

This project was made possible by:

- [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
- [Gabriel Kalango](https://github.com/Gabreil-kalango)'s Contribution
- [Othneil Drew's README Template](https://github.com/othneildrew/Best-README-Template)
- [Ileriayo's Markdown Badges](https://github.com/Ileriayo/markdown-badges)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Markdown Links & Images -->

[contributors-shield]: https://img.shields.io/github/contributors/engrmarkk/Quiz_Api.svg?style=for-the-badge
[contributors-url]: https://github.com/engrmarkk/Quiz_Api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/engrmarkk/Quiz_Api.svg?style=for-the-badge
[forks-url]: https://github.com/engrmarkk/Quiz_Api/network/members
[stars-shield]: https://img.shields.io/github/stars/engrmarkk/Quiz_Api.svg?style=for-the-badge
[stars-url]: https://github.com/engrmarkk/Quiz_Api/stargazers
[issues-shield]: https://img.shields.io/github/issues/engrmarkk/Quiz_Api.svg?style=for-the-badge
[issues-url]: https://github.com/engrmarkk/Quiz_Apiissues
[license-shield]: https://img.shields.io/github/license/engrmarkk/Quiz_Api.svg?style=for-the-badge
[license-url]: https://github.com/engrmarkk/Quiz_Api/blob/main/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/-@iamengrmark-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/iamengrmark
[twitter-shield2]: https://img.shields.io/badge/-@GabrielKalango-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/GabrielKalango
[twitter-url]: https://twitter.com/iamengrmark
[twitter-url2]: https://twitter.com/GabrielKalango
[Quiz_Api-screenshot]: static/images/screen-light.png
[Quiz_Api-screenshot2]: static/images/screen-dark.png
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[jinja]: https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black
[html5]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[css3]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[javascript]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[bootstrap]: https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white
