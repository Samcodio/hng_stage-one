STAGE ONE- Number Classifier Api(Using Fastapi)

This is a FastAPI-based application that classifies numbers based on different mathematical properties. The application provides an HTML form where users can input a number, and it returns various properties such as whether the number is prime, a perfect square, even or odd, and its Armstrong number status. It also fetches a fun fact about the number from numbersapi.com.

Features

Classifies numbers as even/odd and Armstrong numbers.

Checks if a number is prime.

Determines if a number is a perfect square.

Computes the sum of digits.

Fetches a fun fact about the number using numbersapi.com.

Implements CORS for cross-origin access.

Installation

Prerequisites

Ensure you have Python 3.8 or higher installed.

Setup

Clone this repository:

git clone <repository-url>
cd <project-directory>

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Running the Application

Start the FastAPI server by running:

uvicorn main:app --reload

The application will be available at: http://127.0.0.1:8000/

Endpoints

GET /

Returns an HTML page with a form to input a number.

GET /api/classify-number?num=<int>

Returns a JSON response with the following data:

{
    "number": 123,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["odd"],
    "digit_sum": 6,
    "fun_fact": "123 is the emergency telephone number in Colombia."
}

CORS Configuration

This project uses CORSMiddleware to allow cross-origin requests:

from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

Technologies Used

FastAPI for API development

Uvicorn as the ASGI server

Requests for making external API calls

HTML & JavaScript for the frontend

Conclusions

If there is no internet connection, an alert will pop up and the form will not be submitted.
