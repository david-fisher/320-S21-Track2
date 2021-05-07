

# [320-S21-Track2](https://github.com/david-fisher/320-S21-Track2/)


Ethisim is a website that allows you to easily create and assign ethics
simulations. Run them for a participation grade, or
develop them further into longer discussions for class.

## Guide to Docker & Ethisim:
### Installing:
* [Install Docker](https://docs.docker.com/get-docker/) on your machine. 
### Building:
* From the remote server, navigate to the Ethisim directory and run 'docker-compose build'
### Running:
* From the remote server, navigate to the Ethisim directory and run 'docker-compose up --detach'
### Stopping:
* From the remote server, navigate to the Ethisim directory and run 'docker-compose down'

## Continuous Integration & Deployment:
* Each push to the GitHub repository will trigger a GitHub Action that tests whether or not the application can be built. 
* Pushes to the `main` and `build-and-deploy` branches will trigger a GitHub Action that builds the static application and deploys it to the server.
* If neither frontend's source code was changed, it will not test or rebuild the frontend.

## Cloning the Ethisim Application:
1. Download a copy of the project from the server
2. Fill out the env-template and save as '.env'
3. Add ssl certs (/eti/pki/tls/certs/) to ./ssl/certs
4. Add ssl private keys (/eti/pki/tls/private/) to ./ssl/private
5. Add shibboleth config files to ./shib_conf
6. Follow the above instructions for building and running the Docker containers

## Setting up Shibboleth:
Follow instructions in the [Shibboleth Install Guide](shib_install.md)

## Database:
[Schema Diagram](https://github.com/david-fisher/320-S21-Track2/blob/main/ZOOMba/Zoomba_Schema.sql)

## API Endpoints and Rest Documentation:
You can find the list of endpoints here:
[Editor Backend](https://docs.google.com/document/d/1QSiUe21Z_TgT5XZKyR0twevRM864_AswxzVdYLwqW1I/edit?usp=sharing),
[Simulator Backend](https://docs.google.com/document/d/1iL5RgbVrZR_w7PUNcr92rXpdHn7GSKCuI8v04Ba1xGY/edit?usp=sharing)

## Running Ethisim on your Local Machine:
### How to get the Editor Front-end Running:
1. Download node.js version 12.18.4 and [npm](https://www.npmjs.com/get-npm)
2. Clone the GitHub repository
3. In the terminal, navigate to the ethisim folder
4. Run `npm install`. This should install all dependencies (if not, install modules manually using `npm install <module>`)
5. Follow respective instructions to install [Prettier](https://prettier.io/docs/en/install.html), [Eslint](https://www.npmjs.com/package/eslint), and [Husky](https://www.npmjs.com/package/husky) 
6. Use `npm start` to run the development build at localhost:3000

### How to get the Editor Back-end Running:
1. Install [python3](https://www.python.org/downloads/) and follow the setup instructions
2. Clone the GitHub repository
3. In the terminal, navigate to `/moral_kombat_backend/` and install the Django packages using `pip install -r requirements.txt`
4. Navigate to `/moral_kombat_backend/lead/` and run `python manage.py runserver`
  **Running Repository Locally**
     - Navigate to the docker desktop dashboard
        - Find the container with the same name as the repo, expand that
        - Find the container named **Back** and hover over this until 5 circles appear on the right.
        - Click the first one and this should open a browser to the [localhost](http://localhost) address of the backend
  **Migrating on the Backend**
        - Navigate to the docker desktop dashboard
        - hover over the container named **back** until 5 circles appear on the right
        - click the second dot that says **CLI** (Command Line Interface). This should open a terminal.
        - Once here you can direct yourself into the lead folder
        - Run the command:
            "python3 manage.py makemigrations"
            
### How to get the Simulator Front-end Running:
1. Download [node.js](https://nodejs.org/en/download/)
2. Clone the GitHub Repository
3. After cloning repo, navigate to simulator/frontend: `cd ./simulator/frontend`
4. Install all dependencies using `npm install`
5. To run simulator, use `npm start`. This should open a tab in your browser and direct you to `http://localhost:3000`. If not, open a browser tab and go to that url. NOTE: We suggest putting data into the database and running it at the same time as the simulator frontend. This will allow the simulator to actually load in data.

### How to get the Simulator Back-end Running:
1) Be sure that python3 is installed and in the Environment Variable (Pip works better for Django than Conda)
2) Clone the project to your machine `git clone https://github.com/david-fisher/320-S21-Track2.git`
3) Navigate to the "320-S21-Track2\segfault" folder in terminal and install the dependencies (django, djangorestframework, and psycopg2) by running `pipenv shell` then `pipenv install -r requirements.txt` ("requirements.txt" has django, djangorestframework, and psycopg2. The versions of those might change in the future, so you can update this txt file with the new versions if you want)
4) If there have been changes made to the database, run `python manage.py makemigrations` then `python manage.py migrate` (It is harmless to run these even if there haven't been any database changes)
5) Make sure you're connected the correct database (Done through "320-S21-Track2\segfault\segfault", refer to Django documentation for more details)
6) Run the server `python manage.py runserver` ( The default port is at localhost:8000, this can be changed through `python manage.py runserver 0.0.0.0:<port number>`) 
7) To access the endpoints, put "/api" after the "localhost:8000" in the URL


# Differential Team database: how to build
1. Install postgreSQL:  
https://www.postgresql.org/download/

2. Add `PostgreSQL/[version, either 12 or 13]/bin` and `PostgreSQL/[version, either 12 or 13]/lib` to PATH (on Windows) or make it an environment variable on Mac/Linux

3. in command prompt or terminal, call `psql -U postgres -f [full filepath to database_setup.sql]`.
note: The file `database_setup.sql` can currently be found in the `erd-implementation` branch in the `database` folder.**

# Additional notes

Since django is not compatible with composite keys, we made an ID column which is the primary key, and every column that was a part of the original composite key now is unique.

Everything in the DB is functional. Frontend was unable to complete their work.

# Simulator Backend Note
### **To run the Moral Kombat Backend:**

The editor backend is located in the `Moral Kombat Backend` folder. 
The main files to take note of are the `[models.py](http://models.py)`, 
`[serials.py](http://serials.py)` , `views.py` and the `[urls.py](http://urls.py)` .

`[models.py](http://models.py)` - this file is used to represent the database schema on our backend so we can properly modify our data in the database
`[serializer.py](http://serializer.py)` - This file is used to stitch our code in the [views.py](http://views.py) to our code in the models.py
`[urls.py](http://urls.py)` - This file is where we store the routes that our endpoints can be accessed.
`[views.py](http://views.py)` - This is where you store the logic behind all the views and how it all works


# Table purposes

students: links to demographics, student_times, responses and students_to_courses and stores the information of the student (spire id is primary key)
demographics: links to students and stores information regarding student demographics
Professors: Any non-student staff member is stored here, has a professor column (spire id) and name columns.
Scenarios: links a scenario to issues, stakeholders, professors, pages, courses, responses, and student_times. Documents all relevant information about the version of a scenario.
courses: links to professors_to_courses, students_to_course, scenarios_for and responses and stores information regarding a course
Professors_to_courses: Links professors/staff to a course that they teach
Professors_to_scenario: links professors to scenarios. Documents what professor(s) have access to certain scenarios and what permissions they have.
students_to_course: links students to courses
Student_times: links students to courses and scenarios. Documents date/time a scenario was taken
Pages: links responses, scenarios, action_page, generic_page, reflection_questions, and stakeholder_to_page. Documents all relevant information of every frontend page of a scenario. 
Pages_to_scenario: links pages to scenarios
Responses: Stores a student’s response to a page. Documents all information regarding the student’s responses/decisions in a page.
Stakeholders: links scenarios, stakeholder_to_page, conversations, response_to_conversations. Documents relevant information about a stakeholder
Questions: stores all relevant information about a question asked by a stakeholder
stakeholders_to_questions: links questions to stakeholders
Reflections_taken: links a reflection to a response
Issues: links scenarios to coverage. Documents issue name and stores importance scores associated with a specific scenario
Coverage: Links stakeholder to an issue with a coverage score. Links to stakeholder
conversations: links to stakeholders and documents what conversations stakeholders have. Stores a question and answer between a student and a stakeholder. 
Responses_to_conversations: Links a response to a conversation
reflection_questions: links to pages and has questions to reflect
reflection_questions_to_page: links questions to reflect to a page
Stakeholder_to_page: links stakeholder to a page
Generic_page: page that has text to display
Action_page: Page where the user gets to select a choice
Response_to_action_page: links a response to an action page
Scenarios_for: links scenarios and courses. Documents what course a scenario is for.
Courses_to_scenario:  Links courses (and therefore course staff) to a scenario with a certain permission level (0=read vs 1=read and write)
