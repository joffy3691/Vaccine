
# Covid Vaccine Enrollment

Our project is built to solve the current logistical problem of Covid vaccination. People can
use our platform to book vaccination slots from hospitals. Our website partners with the
hospitals to display the number of available vaccines in each hospital, so that the people can
book a slot according to their convenience. Our platform also takes into consideration the
vulnerability of senior citizens, people with comorbidities to covid and prioritises their
vaccination above others, by the use of our ML Algorithm.

## Run Locally

Clone the project

```bash
  git clone https://github.com/PratypartyY2K/Vaccine.git
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Go to the project directory

```bash
  cd covid
```

Enable virtual environment
```bash
  source ./venv/Scripts/activate
```

Start the server

```bash
  python3 manage.py runserver
```

Change admin details

[Django Tutorial Part 4: Django admin site](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site#creating_a_superuser)

  
## Authors

- [@PratypartyY2K](https://github.com/PratypartyY2K)
- [@joffy2691](https://github.com/joffy3691)


  
## Documentation

[Documentation](https://docs.google.com/document/d/1CBZSqrzypt07gS55vXSNMAxyukRMsL4qNWYOFcsDocA/edit?usp=sharing)

  
## Tech Stack

**Client:** HTML5, CSS3, JavaScript, Bootstrap v4.0

**Server:** Django

**Database:** MySQLite DB Browser

  
## Screenshots

**Landing Page**
![Landing Page](/screenshots/landing-page.png)

**Login Page**
![Login Page](/screenshots/login-page.png)

**Patient Home Page**
![Patient Home Page](/screenshots/patient-landing-page.png)

**Choose Hospital**
![Choose Hospital](/screenshots/choose-hospital.png)

**Allotment Status**
![Allotment Status](/screenshots/allotment-status.png)

**Hospital Landing Page**
![Hospital Landing Page](/screenshots/hospital-landing-page.png)

**Vaccine Inventory**
![Vaccine Inventory](/screenshots/update-inventory.png)
