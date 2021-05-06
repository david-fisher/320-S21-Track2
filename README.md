
# [320-S21-Track2](https://github.com/david-fisher/320-S21-Track2/)

Ethisim is a website that allows you to easily create and assign ethics
simulations. Run them for a participation grade, or
develop them further into longer discussions for class.

## Guide to Docker & Ethisim:
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

### How to get the Simulator Front-end Running:
1. Download [node.js](https://nodejs.org/en/download/)
2. Clone the GitHub Repository
3. After cloning repo, navigate to simulator/frontend: `cd ./simulator/frontend`
4. Install all dependencies using `npm install`
5. To run simulator, use `npm start`. This should open a tab in your browser and direct you to `http://localhost:3000`. If not, open a browser tab and go to that url. NOTE: We suggest putting data into the database and running it at the same time as the simulator frontend. This will allow the simulator to actually load in data.

### How to get the Simulator Back-end Running:
1. Install [python3](https://www.python.org/downloads/) and follow the setup instructions
2. Clone the GitHub repository
3. In the terminal, navigate to `/segfault/` and install the Django packages using `pip install -r requirements.txt`
4. Run `python manage.py runserver`



