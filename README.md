# Static Site Mailer

An e-mail sending API for static sites using SendGrid and Python on Heroku. It now requires setting a safety token inorder to avoid unauthorised usage and spam messages.

Icons by [Icons8](https://icons8.com/)

## Clone & Deploy

**Step 1:** Install the heroku CLI: [installation instructions](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

**Step 2:** Create a heroku account and login in using the following command:

```bash
$ heroku login
heroku: Enter your login credentials
Email: xzy@abc.com
Password: ********
```

**Step 3:** Clone this repo

```bash
git clone https://github.com/sdabhi23/SendGrid-Mailer.git
cd SendGrid-Mailer
```

**Step 4:** Create a new heroku app

```bash
$ heroku create
Creating app... done, ⬢ morning-depths-68125
https://morning-depths-68125.herokuapp.com/ | https://git.heroku.com/morning-depths-68125.git
```

## Setup

* Get a free account from <https://signup.sendgrid.com/>

* Setup an API key ([Instructions](https://sendgrid.com/docs/User_Guide/Settings/api_keys.html#-Creating-an-API-key))

* Add the API key as a config var to your app using the following command:

```bash
$ heroku config:set SENDGRID_KEY=<your api key>
Adding config vars and restarting myapp... done
SENDGRID_KEY: <your api key>
```

* Add your email address as a config var to your app using the following command:

```bash
$ heroku config:set EMAIL=<your email id>
Adding config vars and restarting myapp... done
EMAIL: <your email id>
```

* Add your website's url as a config var to your app using the following command:

```bash
$ heroku config:set ALLOWED_ORIGINS=<your website url>
Adding config vars and restarting myapp... done
ALLOWED_ORIGINS: <your website url>
```

* Add your safety token as a config var to your app using the following command:

```bash
$ heroku config:set ORIGIN_TOKEN=<your safety token>
Adding config vars and restarting myapp... done
ORIGIN_TOKEN: <your safety token>
```

> **Alternatively you can use any other method described at <https://devcenter.heroku.com/articles/config-vars#managing-config-vars> for setting up config variables**

* Push all the changes to your app using `$ git push heroku master` and your API will be up and running at `/contact` in a matter of minutes!

## Usage

* Using fetch in JavaScript

```JavaScript
var url = 'https://<app name>.herokuapp.com/contact';
// For example: https://morning-depths-68125.herokuapp.com/
var formData = new FormData();
formData.append("name", "Tester");
formData.append("email", "tester@sdabhi23.io");
formData.append("subject", "Testing");
formData.append("message", "This is a test mail");

fetch(url, {
      method: "POST",
      body: formData,
      headers: {
        'x-origin-token': process.env.REACT_APP_ORIGIN_TOKEN
      }
    })
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          throw new Error("Something went wrong");
        }
      })
      .catch(error => console.error('Error:', error))
      .then(response => console.log('Success:', response));
```
