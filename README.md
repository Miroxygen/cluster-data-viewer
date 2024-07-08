# Cluster Data Viewer

## Features

- Fetch clustered blog data from a k-means service.
- Display clusters interactively, allowing users to expand and collapse each cluster for detailed view.
- Front-end interface built with HTML, CSS, and JavaScript.
- Back-end server implemented with Express.js.
- K-means clustering performed by a Python service.

## Installation

1. Clone the repository:

2. Install Node.js dependencies:

- npm install

3. Install Python dependencies:

- pip install -r requirements.txt

4. Set up the environment variables by creating a .env file in the root directory. Add the following environment variables:

- SESSION_SECRET=your-session-secret
- PORT=your-server-port

## Usage

1. Start the Python k-means clustering service:
 
 - python src/python/server.py

2. Start the Express.js server:

 - npm start

3. Open your browser and navigate to http://localhost:your-server-port to access the application.


## How It Works

### Frontend

The front end is built using HTML, CSS, and JavaScript. It provides a simple interface for fetching and displaying clustered data. The index.js file contains event listeners for toggling the visibility of clusters.

### Backend

The backend is implemented using Express.js. It serves the front-end files and provides endpoints for fetching k-means clustered data. The main server logic is defined in server.js and the routes are handled in router.js.

### K-means Clustering Service

The k-means clustering algorithm is implemented in Python. The server.py file sets up an HTTP server that provides clustered data when requested. The clustering logic and related functions are defined in the functions directory.

## License

This project is licensed under the MIT License.
