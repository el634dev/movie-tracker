## Movie Tracker
> Movie tracker app that helps users track their favorite movies and directors

<div align="center">
<!-- Badges -->
<p>
  <a href="https://github.com/Louis3797/awesome-readme-template/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/el634dev/movie-tracker" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/el634dev/movie-tracker" alt="last update" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/issues/">
    <img src="https://img.shields.io/github/issues/el634dev/movie-tracker" alt="open issues" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/Made%20with-Flask-1f425f.svg" alt="license" />
  </a>
</p>
   
<h4>
    <a>View Demo</a>
  <span> · </span>
    <a href="https://github.com/el634dev/movie-tracker/README.md">Documentation</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
## Table of Contents
- [Screenshot](#screenshot)
  * [Tech Stack](#tech-stack)
  * [Features](#features)
  * [Environment Variables](#environment-variables)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Run Locally](#run-locally)
- [Usage](#usage)
- [License](#license)
- [Live Demo](#demo)
  

<!-- About the Project -->
## Screenshot
<div align="center"> 
  <img width="1047" alt="Screenshot 2024-03-03 at 7 22 49 PM" src="https://github.com/el634dev/movie-tracker/assets/84924260/882216a4-e56c-4d74-b646-4e285ad840a7">
</div>

<!-- TechStack -->
## Tech Stack
<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://jinja.palletsprojects.com/en/2.10.x/">Jinja</a></li>
    <li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://flask.palletsprojects.com/en/2.3.x/quickstart/">Flask</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.sqlalchemy.org/">SQLAlchemy</a></li>
  </ul>
</details>

<!-- Env Variables -->
## Environment Variables
To run this project, you will need to add the following environment variables to your .env file before running `python app.py`

`DATABASE_URL` - set this as the url to your database, start with sqlite:///
>
`SECRET_KEY` - set this to something secure

<!-- Getting Started -->
## Getting Started

<!-- Prerequisites -->
### Prerequisites
This project uses pip as package manager which comes pre-installed with Python

<!-- Installation -->
### Installation

<!-- Run Locally -->
### Run Locally
Clone the project using

```bash
  git clone
```

Go to the project directory

```bash
  cd movie-tracker-main
```

Create a virtual enivornment then activate inside of the project directory(folder)
> Note this helps create a seperate environment from the global enviornment
```bash
  python3 -m venv venv
  source venv/bin/activate
```

Install dependencies

```bash
   pip3 install -r requirements.txt 
```

Start the server

```bash
  python3 app.py
```

<!-- Project Status -->
## Project Status
Project is: __completed__

<!-- Usage -->
## Usage
- `When a user navigates to the homepage, the user can see other users (usernames) and a list of movies and directors`
- `A user can click unto a movie which links to the movie detail page and they can edit the details`
- `A user can click unto a director which links to the director detail page and they can edit the details`
-  `A user can also create a director or movie through the Create Director or Create Movie button when a user signs in`
-  `A user can also add their favorite movies and unfavorite them at anytime and see a list of their favorite movies in their profile`

## Features:
- Authenication
- CRUD Functionality
- User Profile

<!-- License -->
## License
Distributed under no License.

<!-- Demo -->
## Demo
Project Link: [https://github.com/el634dev/movie-tracker](https://github.com/el634dev/movie-tracker)
