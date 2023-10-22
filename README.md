# Data-Storage-Service

This project is a simple key-value store implemented in Python with a RESTful API using Flask. It allows users to store and retrieve key-value pairs through HTTP requests and serves as a basic database for small-scale applications.

## Features

- **Key-Value Storage**: The project provides a simple key-value storage system to store and manage data efficiently.

- **RESTful API**: It offers a RESTful API for adding, retrieving, and deleting data. Users can interact with the key-value store through HTTP requests.

- **Data Persistence**: Data is persisted to a JSON file, ensuring that data remains available between application restarts.

- **Cross-Platform Compatibility**: The project is designed to be accessible from applications written in various programming languages through HTTP requests.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

1. **Clone the Repository**: Clone this repository to your local machine using `git clone`.

   ```bash
   git clone https://github.com/your-username/custom-key-value-project.git
   ```

2. **Install Dependencies**: Install the required dependencies. Ensure you have Python and Flask installed.

3. **Run the Application**: Start the Flask application.

4. **Access the API**: The key-value store API should be accessible at `http://localhost:5000`.

## API Endpoints

- `GET /get/<key>`: Retrieve a value for a given key.
- `POST /set?key=<key>&value=<value>`: Set a key-value pair.
- `DELETE /delete/<key>`: Delete a key from the store.
