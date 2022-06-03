# flask-social-auth

> This application ues Flask-Dance and the GitHub OAuth API to authenticate a user.

[![Website https://flask-react-blog-dev.herokuapp.com/](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://flask-react-blog-dev.herokuapp.com/)
[![security: bandit][bandit-image]][bandit-url]
[![Imports: isort][isort-image]][isort-url]
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)


This application allows a user to register and authenticate themselves using their GitHub credentials. You can read more about it, including how it was developed over at [How to Authenticate and Register a User using Flask-Dance and the GitHub OAuth API.](https://medium.com/@lyle-okoth/how-to-authenticate-and-register-a-user-using-flask-dance-and-the-github-oauth-api-a5aa64edc64b).

![](header.png)

## Installation

### Clone the [Flask Social Auth repo](https://github.com/twyle/flask-social-auth)

```sh
git clone https://github.com/twyle/flask-social-auth.git
```

### Navigate into the cloned repo

```sh
cd flask-social-auth
```

### Create a Python3 Virtual Environment.

OS X & Linux:

```sh
python3 -m venv venv
```

Windows:

```sh
python3 -m venv venv
```

### Activate the Virtual Environment.

OS X & Linux:

```sh
source venv/bin/activate
```

Windows:

```sh
venv\\Scripts\\Activate
```

### Install the Project dependencies.

```sh
make install
```

### Create the project secrets

Navigate to [GitHub OAth API registration](https://github.com/settings/applications/new) and register a new application. At the commandline, create a .env file:

```sh
touch .env
```
Then add the following to the file:

```sh
-   FLASK_ENV=development
-   SECRET_KEY=supersecretkey
-   SQLALCHEMY_DATABASE_URI=sqlite:///users.db
```
Then copy the client id and client secret from the registered app and add them to the file also:
```sh
-   CLIENT_ID=xxxxxxxxxxxxxxxxxxx
-   CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-   OAUTHLIB_INSECURE_TRANSPORT=1
```

### Run the application.

```sh
make run
```

## Usage example

### After the application is run, navigate to http://localhost:5000/home and click on the GitHub Login button:

![](header.png)

### The application will direct to a page that will request you to authorize the app:

![](oauth-authorize.png)

### You will then be redirected to a dashboard that displays your information.

![](oauth-dashboard.png)

## Development setup

Here is how to setup your development environment incase you want to play around with this project.

### Install the development dependencies (make sure you have set up the virtual environment as stated above and are in the project folder)

```sh
make install-dev
```

### Run the unit tests

```sh
make test
```

## Release History

## v0.3.0 (2022-06-02)

### Feat

- added the templates.

## v0.2.0 (2022-06-02)

### Feat

- implemented user data storage.

## v0.1.0 (2022-06-02)

### Feat

- created the authentication workflow.

## v0.0.1 (2022-06-02)

### Fix

- fixed the linting errors.
- fixed isort.

## Meta

Lyle Okoth – [@lylethedesigner](https://twitter.com/lylethedesigner) on twitter – [lyle okoth](https://medium.com/@lyle-okoth) on medium, and my email is lyceokoth@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/twyle/github-link](https://github.com/twyle/)

## Contributing

1. Fork it https://github.com/twyle/flask-social-auth/fork
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[wiki]: https://github.com/yourname/yourproject/wiki

[bandit-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-url]: https://github.com/PyCQA/bandit

[isort-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-url]: https://pycqa.github.io/isort/

[feature-development-image]: https://github.com/twyle/flask-react-blog-simple/actions/workflows/feature-development-workflow.yml/badge.svg?branch=feature%2Fworkflows
[feature-development-url]: https://github.com/twyle/flask-react-blog-simple/actions/workflows/feature-development-workflow.yml

[development-image]: https://github.com/twyle/github-oauth-app/actions/workflows/development-workflow.yml/badge.svg
[development-url]: https://github.com/twyle/github-oauth-app/actions/workflows/development-workflow.yml

[staging-image]: https://github.com/twyle/flask-react-blog-simple/actions/workflows/staging-workflow.yml/badge.svg
[staging-url]: https://github.com/twyle/flask-react-blog-simple/actions/workflows/staging-workflow.yml

[production-image]: https://github.com/twyle/flask-react-blog-simple/actions/workflows/production-workflow.yml/badge.svg
[production-url]: https://github.com/twyle/flask-react-blog-simple/actions/workflows/production-workflow.yml
