
# 320-S21-Track2
https://github.com/david-fisher/320-S21-Track2/

BELOW IS THE README FROM LAST SEMESTER'S TRACK III REPO 


Ethisim is a website that allows you to easily create and assign ethics
simulations. Run them for a participation grade, or
develop them further into longer discussions for class.

This is Track III's repository containing code for both the front-end and back-end of Ethisim. This README provides instruction on how to install and setup both the front-end and back-end in order to get the software running.

## How to get the Front-end Running
1. Download node.js version 12.18.4 and npm https://www.npmjs.com/get-npm
2. Clone the Github repository
3. cd into the ethisim folder
4. Run npm install, This should install all dependencies if this doesn't work see section below
5. To run the front-end, use npm start to run the development build at local host:3000
6. You are done, but note that you will need to have the back-end running as well for the front-end to connect to the database and see current scenarios on the dashboard

### You can complete all of these steps by just using npm install
#### Install Dependencies
    - npm install react@16.13.1
    - npm install react-device-detect@1.14.0
    - npm install react-dom@16.13.1
    - npm install react-flow-renderer@6.1.3
    - npm install react-router-dom@5.2.0
    - npm install react-scripts@3.4.4
    - npm install @material-ui/core@4.11.0
    - npm install @material-ui/icons@4.9.1
    - npm install @material-ui/lab@4.0.0-alpha.56
    - npm install @testing-library/jest-dom@5.11.4
    - npm install @testing-library/react@11.0.4
    - npm install @testing-library/user-event@12.1.6
    - npm install axios@0.21.0
    - npm install start@5.1.0
    - npm install suneditor-react@2.14.2

#### How to install Prettier, Eslint and Husky
    1. Npm install --save-dev --save-exact prettier will install prettier
    2. Make sure to install eslint before installing eslint-config-prettier which allows prettier and eslint to work together nicely
    3. Npm install eslint --save-dev will install eslint
    4. Run npx eslint --init to set up an configuration file
       - Questions will appear and the directions tell you to use arrow keys to select an answer even though the arrow keys don’t work.
       Think of the options presented to you in each question as an array starting at 0 or 1.
       If you want for example option one out of three for the second question,
       then type in 0 to the command line and press enter and that should select the answer that you want.
       - Answer all the questions before moving forward, if you mess up on one of the answers, just press Ctrl^C and re-run the npx eslint --init command
    5. You might also need to install eslint-plugin-react@latest, if so follow the directions on the command line after finishing the previous step
    6. Make sure prettier and eslint are both installed  before we run npm install --save-dev eslint-config-prettier so prettier and eslint will work together nicely with each other
    7. Then, add eslint-config-prettier to the "extends" array in your .eslintrc.* file. Make sure to put it last, so it gets the chance to override other configs. It might already be there.
    { "extends": [ "some-other-config-you-use", "prettier"]}
    8. To install Husky Make sure Prettier is installed and is in your devDependencies before you proceed and then run npx mrm lint-staged
    9. This will install husky and lint-staged, then add a configuration to the project’s package.json that will automatically format supported files in a pre-commit hook. After this step you are done


## How to get the Back-end Running
### On MAC
1. Install python3
2. sudo pip3 install pipenv (do it globally)
3. clone https://github.com/david-fisher/320-F20-Track-III.git
4. Navigate to moral_kombat_backend folder
5. pipenv shell
6. pipenv install -r requirements.txt
7. cd lead
8. python3 manage.py runserver


#### How to run server on MAC:
1. Go to moral_kombat_backend directory
2. pipenv shell
3. cd lead
4. python3 manage.py runserver

### On WINDOWS
1. https://www.python.org/downloads/ (Checkmark all optional features, add Python to environment variables)
2. clone https://github.com/david-fisher/320-F20-Track-III.git
3. Navigate to moral_kombat_backend folder
4. Open Terminal (IF RUN INTO ERRORS INSERT py -m before each command)
5. pip install -r requirements.txt
6. cd lead
7. python manage.py runserver
8. Might need to download https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

#### How to run server on Windows:
1. Go to moral_kombat_backend directory
2. cd moral_kombat_backend
3. cd lead
4. py -m manage.py runserver

### TEST The back-end:
Download postman

### Database:
Used ElephantSQL (postgreSQL)
Schema Diagram: https://dbdiagram.io/d/5f8326e63a78976d7b772f0c


## API Endpoints and Rest Documentation
You can find the list of endpoints here at:
https://docs.google.com/document/d/1QSiUe21Z_TgT5XZKyR0twevRM864_AswxzVdYLwqW1I/edit?usp=sharing

To see REST Documentation run both the front-end and back-end and type http://localhost:8000
=======
# 320-S21-Track2

BELOW IS THE README FOR SIMULATOR SETUP

# 320-F20-Track-II

# Differential Team database: how to build
1. Install postgreSQL:  
https://www.postgresql.org/download/

2. Add `PostgreSQL/[version, either 12 or 13]/bin` and `PostgreSQL/[version, either 12 or 13]/lib` to PATH (on Windows) or make it an environment variable on Mac/Linux

3. in command prompt or terminal, call `psql -U postgres -f [full filepath to database_setup.sql]`.
note: The file `database_setup.sql` can currently be found in the `erd-implementation` branch in the `database` folder.

# how to connect to database from react.js
1. run `npm install all` within the directory containing `package.json` to install all dependencies for the pg package, which is the library used to communicate between the PostgreSQL database and the react.js app, as well as all other dependencies outlined in the `package_lock.json` file

2. In `goon-universe`, the app can be run with `node app.js`.

3. Using the functions outlined in `queries.js`, which implements the REST API enumerated in `app.js`, frontend teams can now interact with the database from their React.js app as usual.

4. Worth noting: the `pg` package's use depends on certain user credentials used to access a common database (namely, the username/password for the postgresql database which you've set up using `database_setup.sql`). Since the git repository is public, it's a security risk to store these credentials in public on the clear web. Thus, we are using a .env file (locally, for now) to store these credentials. **You will not be able to access the database from the React app without a properly configured .env file!**

# how to run the frontend react app
1. Install Node.js:  
https://nodejs.org/en/download/

2. Go into the folder `frontend` in the command line: `cd ./simulator/frontend/`

3. Run `npm install` in the command line to install all dependencies required to run the app.

4. We recommend setting up the backend and filling the database with some data so you can see the data loaded into the frontend.

4. Run `npm start` in the command line to start the app. This should open your browser and send you to `http://localhost:3000`. If not, go to your browser and go to that url. 

# Tip to not drive everyone on your track insane.

If a file is for configuring something on your local machine to run, like config.js or settings.py, do not commit those changes to GitHub. If you do, you will mess up everyone elses local configuration when they pull the latest changes. 
