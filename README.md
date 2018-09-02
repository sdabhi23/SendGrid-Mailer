# SendGrid Mailer

A starter project to deploy a mailing service for static sites using sendgrid and python on Heroku.

> The code for deploying to Hasura cluster has been moved to [hasura branch](https://github.com/sdabhi23/SendGrid-Mailer/tree/hasura) and will no longer be maintained.

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
$ git clone https://github.com/sdabhi23/SendGrid-Mailer.git
$ cd SendGrid-Mailer
```

**Step 4:** Create a new heroku app
```bash
$ heroku create
Creating app... done, ⬢ morning-depths-68125
https://morning-depths-68125.herokuapp.com/ | https://git.heroku.com/morning-depths-68125.git
```

## Setup

* Get a free account from https://signup.sendgrid.com/

* Setup an API key ([Instructions](https://sendgrid.com/docs/User_Guide/Settings/api_keys.html#-Creating-an-API-key))

* Add the API key as a config var to your app using the following command:
```bash
$ heroku config:set SENDGRID_KEY=<your api key>
Adding config vars and restarting myapp... done, v12
SENDGRID_KEY: <your api key>
```
Alternatively you can use any other method described at https://devcenter.heroku.com/articles/config-vars#managing-config-vars

* Add your email address at line 20 in `server.py`
```python
"to": [
    {
         "email": "" # add your email address here
    }
],
```
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
  method: 'POST',
    body: formData
}).then(res => res.json())
.catch(error => console.error('Error:', error))
.then(response => console.log('Success:', response));
```
