# Hello World Python Flask App

This Flask application displays "Hello World" fetched from a MySQL database hosted on Google Cloud. You can find the infrastructure code for deploying this application at the [iddotmeiac GitHub Repository](https://github.com/sonamawachar0110/iddotmepython).

### Key Points:

- **Database Connection**: The app connects to a Cloud SQL database to retrieve the "Hello World" message.
- **Dockerfile**: Configures the application to run with Gunicorn.
- **app.py**: Contains the logic for creating the database table and inserting data.
- **secrets.yml**: Manages database credentials, securely fetched from Google Cloud SQL.
- **sql.py**: Implements the database connection using SQLAlchemy ORM.

Make sure the application is properly set up to connect to the Cloud SQL instance and display the "Hello World" message.
