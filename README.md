# archeun

This repository containes the code of the core archeun platform, which includes,

- User account and organization provisioning
- Authentication service
- oAuth platform for other archeun services

### Development

#### Pre-requisites

- Python 3.9.x (tested on 3.9.x version only) version installed. A virtual environment setup is recommended.
- A mysql database server

#### Setting up the development environment
Please follow the below instructions on how to setup the system for development

1. Clone the repository.
   ```
   git clone https://github.com/archeun/archeun

2. Install the python dependencies by running the below command inside the codebase root.
   ```
   pip install -r requirements.txt

3. Navigate to the <codebase>/archeun/client directory and install the required client-side libraries
    ```
   npm install
   
4. Make sure the database connection settings match your local values. The default settings can be found in `<codebase>/archeun/archeun/settings.yml`
   You can setup your own values here. 
   ```
   DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'archeun',
            'USER': 'root',
            'PASSWORD': '1234',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

5. Start the mysql server and create an empty database with the value you specified for the `NAME` attribute in the above settings

6. Prepare and push the migrations into the database by running the below 2 commands inside the codebase root
    ```
   python manage.py makemigrations
   python manage.py migrate
   
7. Create a super user who can log into the admin site. Follow the prompts by giving necessary information.
    ```
   python manage.py createsuperuser   

8. If everything goes well, spin up the development server by running the below command
    ```
   python manage.py runserver
   
9. This will start the development server and, the system can be accessed at `http://127.0.0.1:8000/`. The home page will not work at the moment.

10. Navigate to the `http://127.0.0.1:8000/admin/login` and log into the system by providing the super user credentials we created in step 7.

#### User provisioning related urls

You can use the below screens for provisioning users (create accounts, password reset, etc.)

Authentication related routes are defined under `core/auth`
1. `core/auth/create-account/`
   > Form to create user accounts
2. `core/auth/login/`
   > Login form
3. `core/auth/password-reset`
   > Password reset form

User related routes are defined under `core/user`. These screens are only accessible by a logged-in user
4. User profile: `core/user/profile`

#### OpenID Connect related functionality

1. Once the super user logs into the admin site, there will be a section called `OPENID CONNECT PROVIDER`
2. Under that section there will be 4 sub menues,
    1. Authorization Codes		
    2. Clients
    3. RSA Keys
    4. Tokens
3. For now, we will click on the Add button beside the `Clients` menu item and try to create a new OIDC enabled client.
4. Fill the form with the below information
   - **Name:** Provide a name for the client
   - **Owner:** Keep blank or select a user
   - **Client Type:** Select the client type that matches your use case (Confidential clients are capable of maintaining the confidentiality of their credentials. Public clients are incapable.)
   - **Response Types:** Select the appropriate ones. For development purposes select all
   - **Redirect URIs:** Specify the urls to be used as the login success callbacks of your client app
   - **JWT Algorithm:** This is the algo used to encode ID Tokens. Select RS256 as the default.
5. Save the form
6. Now, from the client, setup a url like below, which upon clicking on, will redirect the user to the archeun login page.
    ```
   <archeun-site-url>/core/openid/authorize?client_id=<oidc-client-id>>&redirect_uri=<client-callback-url>&response_type=code&scope=openid<space-separated-scopes>>&state=<state-value>

   for eg:
   
   http://127.0.0.1:8000/core/openid/authorize?client_id=200889&redirect_uri=http://localhost:5000/archeun-client&response_type=code&scope=openid email profile&state=123123
   
