# SendGrid Mailer

A starter project to deploy a mailing service for static sites using sendgrid and python on Hasura k8s platform

## Clone & Deploy

**Step 1:** Install the hasura CLI: [installation instructions](https://docs.hasura.io/0.15/manual/install-hasura-cli.html)

**Step 2:** Create a hasura project on your machine
```bash
$ # 1) Run the quickstart command
$ hasura quickstart sdabhi23/sendgrid-mailer
```

**Step 3:** Deploy the project to your free cluster!
```bash
$ # 2) Git add, commit & push to deploy to your cluster
$ cd sendgrid-mailer
$ git add . && git commit -m 'First commit'
$ git push hasura master
```

**Note:** Your **free cluster** got automatically created when you ran the `quickstart` command.

## Setup

* Get a free account from https://signup.sendgrid.com/
* Setup an API key ([Instructions](https://sendgrid.com/docs/User_Guide/Settings/api_keys.html#-Creating-an-API-key))
* Add the key as a secret to your project using the following command:
```bash
$  hasura secrets update sendgrid.key <your api key>
```
* Add your email address at line 20 in `server.py`
```python
"to": [
    {
         "email": "" # add your email address here
    }
],
```
* Push all the  changes to your cluster and your API will be up and running at `/contact` in a few minutes!

## Usage

* Using fetch in JavaScript
```JavaScript
var url = 'https://app.<cluster name>.hasura-app.io/contact';
var formData = new FormData();
formData.append("name", "Tester");
formData.append("email", "tester@hasura.io");
formData.append("subject", "Testing");
formData.append("message", "This is a test mail");

fetch(url, {
  method: 'POST',
    body: formData
}).then(res => res.json())
.catch(error => console.error('Error:', error))
.then(response => console.log('Success:', response));
```