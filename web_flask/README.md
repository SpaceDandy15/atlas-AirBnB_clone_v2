# Flask Web Application for HBNB

This repository contains two Flask web applications that demonstrate the basics of routing in Flask. The applications respond to HTTP requests with simple text messages.

## Assignments Overview

### Assignment 0: Hello Flask!

- **Purpose**: Create a basic Flask web application.
- **Main Route**: 
  - `"/"` - Returns **"Hello HBNB!"**.
- **Listening on**: `0.0.0.0` at port `5000`.
- **Testing**: 
  - You can test the application by running `curl http://127.0.0.1:5000` in the terminal.

### Assignment 1: HBNB Route

- **Purpose**: Extend the Flask application with an additional route.
- **Routes**: 
  - `"/"` - Returns **"Hello HBNB!"**.
  - `"/hbnb"` - Returns **"HBNB"**.
- **Listening on**: `0.0.0.0` at port `5000`.
- **Testing**: 
  - You can test the new route by running `curl http://127.0.0.1:5000/hbnb` in the terminal.

## Requirements

- Python 3.8.5 or higher
- Flask
- Ensure your firewall settings allow connections to port `5000`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/atlas-AirBnB_clone_v2.git
   cd atlas-AirBnB_clone_v2/web_flask
