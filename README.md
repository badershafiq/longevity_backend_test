# marketplace-api-assignment
Marketplace API assignment for Longevity Scientific Resort

Added a postman collection for API documentation

## Steps to run

`bash
python3.9 -m venv venv
`

UNIX bases OS: `source venv/bin/activate`

Windows `./venv/scripts/activate`

Clone the repo `git clone https://github.com/jayantamadhav/marketplace-api-assignment.git`

cd into folder `cd marketplace-api-assignment`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

## How to use

http://127.0.0.1:8000/marketplace/ - Homepage with a join us buttons for partners

http://127.0.0.1:8000/marketplace/register/ - Registration page for partners

### API

http://127.0.0.1:8000/marketplace/api/recommendation - Third-party Recommendation service

http://127.0.0.1:8000/marketplace/api/recommendation/interna - Internal Recommendation service for users







