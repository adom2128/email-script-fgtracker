# FGTracker

Capstone project for Ada Developers Academy - Cohort 19.

## Project Description & Links

FGTracker is designed to simplify the process of managing survey submissions and focus group participation. With FGTracker, you can effortlessly keep tabs on the surveys you've submitted, enabling you to gauge your success rates more effectively. Additionally, FGTracker tracks your participation history, ensuring you know exactly when it's appropriate to reapply. The platform also offers insights into payment status, balances, and expiration dates.


**Repository Links**

- [Front End](https://github.com/adom2128/front-end-fgtracker)
- [Back End](https://github.com/adom2128/back-end-fgtracker)
- [Chrome Extension](https://github.com/adom2128/extension-fgtracker)
- [Email Script](https://github.com/adom2128/email-script-fgtracker)

## Demo

[Recorded Demo](https://youtu.be/jAu6PywxjrU)

## Features

- User authentication with Auth0
- Display all survey entries as well as those that resulted in completed focus group participation
- Add, edit, view, and delete survey entries
- View payments with available balances, with links to the digital gift card
- Gift card balances are automatically updated using an email-checking script
- Chrome extension to conveniently add survey entries to the database

## Tech Stack

**Back-End**
- Python
- Flask
- SQLAlchemy
- PostgreSQL
- Axios


**Front-End**
- Typescript
- React - Router Dom, Bootstrap, Auth0, Datepicker


**Extension**
- Google Chrome API
- Webpack

## Dependencies

**Front-End**
```
    "@auth0/auth0-react": "^2.2.0",
    "@fortawesome/fontawesome-free": "^6.4.0",
    "@fortawesome/fontawesome-svg-core": "^6.4.0",
    "@fortawesome/free-brands-svg-icons": "^6.4.2",
    "@fortawesome/free-solid-svg-icons": "^6.4.0",
    "@fortawesome/react-fontawesome": "^0.2.0",
    "@testing-library/jest-dom": "^5.14.1",
    "@testing-library/react": "^13.0.0",
    "@testing-library/user-event": "^13.2.1",
    "@types/jest": "^27.0.1",
    "@types/node": "^16.7.13",
    "@types/react": "^18.0.0",
    "@types/react-datepicker": "^4.15.0",
    "@types/react-dom": "^18.0.0",
    "axios": "^1.4.0",
    "babel-plugin-macros": "^3.1.0",
    "bootstrap": "^5.3.1",
    "date-fns": "^2.30.0",
    "react": "^18.2.0",
    "react-bootstrap": "^2.8.0",
    "react-datepicker": "^4.16.0",
    "react-dom": "^18.2.0",
    "react-loading": "^2.0.3",
    "react-router-dom": "^6.14.2",
    "react-scripts": "5.0.1",
    "typescript": "^4.4.2",
    "web-vitals": "^2.1.0"
```

**Back-End**
```
    alembic==1.5.4
    attrs==21.2.0
    autopep8==1.5.5
    certifi==2020.12.5
    chardet==4.0.0
    click==7.1.2
    Flask==1.1.2
    Flask-Cors==3.0.10
    Flask-Migrate==2.6.0
    Flask-SQLAlchemy==2.4.4
    gunicorn==20.1.0
    idna==2.10
    iniconfig==1.1.1
    itsdangerous==1.1.0
    Jinja2==2.11.3
    Mako==1.1.4
    MarkupSafe==1.1.1
    packaging==20.9
    pluggy==0.13.1
    psycopg2-binary==2.9.5
    py==1.11.0
    pycodestyle==2.6.0
    pyparsing==2.4.7
    pytest==7.1.1
    python-dateutil==2.8.1
    python-dotenv==0.15.0
    python-editor==1.0.4
    requests==2.25.1
    six==1.15.0
    SQLAlchemy==1.3.23
    toml==0.10.2
    urllib3==1.26.4
    Werkzeug==1.0.1
```

**Chrome extension**
```
    "copy-webpack-plugin": "^11.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
```

## Contact

Alejandra Dominguez - adom2128@gmail.com
