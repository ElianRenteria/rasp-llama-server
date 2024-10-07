
# Rasp LLaMA Server

**Rasp LLaMA Server** is a project developed by Elian Renteria. This repository contains the source code and documentation for a Flask-based API server running on a Raspberry Pi that uses the tinyllama LLM model via the Ollama library.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Rasp LLaMA Server is a Flask API server designed to run on a Raspberry Pi, allowing users to send chat messages and receive responses generated by the tinyllama LLM model. This server uses the Ollama library to handle language model interactions, making it ideal for lightweight conversational AI applications.

## Features

- Lightweight conversational AI server
- Uses the tinyllama LLM model for responses
- Flask-based API with a `/chat` endpoint
- Optimized for Raspberry Pi

## Installation

To install and set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ElianRenteria/rasp-llama-server.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rasp-llama-server
   ```
3. Install the necessary dependencies:
   ```bash
   pip install flask ollama
   ```

## Usage

After installation, you can start the API server with the following command:

```bash
python app.py
```

By default, the server will run on `http://0.0.0.0:8120`. To send a chat message, make a POST request to the `/chat` endpoint with a JSON payload containing a `message` key.

Example:

```bash
curl -X POST http://localhost:8120/chat -H "Content-Type: application/json" -d '{"message": "Hello"}'
```

## API Endpoints

- `POST /chat`: Sends a message to the tinyllama model and receives a response.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact [Elian Renteria](mailto:elianrenteriadevelopment@gmail.com).
