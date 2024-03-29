
# Email Automation

A python program to send customised email to many clients.


## Run Locally

Clone the project

```bash
  git clone https://github.com/ShahDishank/email_automation
```

Go to the project directory

```bash
  cd email_automation
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Make .env file

```bash
  from = "from-email@gmail.com"
  password = "your-google-app-password"
```
**see how to create google app password: https://www.youtube.com/watch?v=lSURGX0JHbA**

- Add details of the clients emails in data.csv file

- Make html template of body message in body.html file

- Give arguments in msg.add_alternative function call in mail.py file
```bash
msg.add_alternative(body.format(data = html.format(FirstName = fn, LastName = ln)),subtype="html",)
// write the values of variables of body.html file here
```

- Write subject in send_email function call in mail.py file
```bash
  send_email("Demo Email")  // write your subject here
```

Run the program

```bash
  python mail.py
```


## Feedback

If you have any feedback, please reach out to me at shahdishank24@gmail.com


## Tech Stack

**Language:** Python
## Author

- [@shahdishank](https://www.github.com/ShahDishank)

