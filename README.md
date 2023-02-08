# suade-report-API

## Installation
### I. Clone this repository: <br>
    ```
    git clone https://github.com/alicialawjy/suade-report-API.git
    ```

### II. Set up virtual environment
    ```
    pip3 install virtualenv
    virtualenv ./backendenv
    source backendenv/bin/activate
    python3 -m pip install -r requirements.txt
    ```

### III. Run flask app
    ```
    python3 -m flask run
    ```

## Example of using the API
    Key in the date as a query in the url:
    ```
    http://127.0.0.1:5000/get_summary?date=2019-08-01
    ```

## Test
Due to lack of time, I created a simplified unit testing that assesses the functionalities of the summary code.
This is located in `app/test.py`. </br>
To run the code, use: </br>

    ```
    python3 test.py
    ```