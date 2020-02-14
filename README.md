# Stock API

Stock API is an Api Rest for stock data.

## Dependencies
- Python 3.7
- Docker
- Linux or Mac

## Cloning and entering the project
- To clone the project:
    ```
    git clone git@github.com:iuryamorim/stock-api.git
    ```
- To enter the project:
    ```
    cd stock-api
    ```

## Creating and Activating the Virtual Environment
- To create the virtual environment:
    ```
    pip install virtualenv
    virtualenv -p python3 env
    ```
- To activate the virtual environment:
    ```
    source env/bin/activate
    ```

## Downloading dependencies and running the project
- To download dependencies:
    ```
    pip install -r requirements.txt
    ```

- To run the project:
    ```
    docker-compose -f docker-compose.yml up
    ```


## Routes

### Dividends

```bash
$ curl -X GET http://0.0.0.0:5000/stock/dividends/?ticker=MSFT&start=2019-01-01&end=2019-12-28 | python3 -m json.tool
{
    "result": {
        "2019-01-31 00:00:00": {
            "firm": "Nomura",
            "to_grade": 1
        }
    }
}
```

### Close

```bash
$ curl -X GET http://0.0.0.0:5000/stock/close/?ticker=MSFT&start=2019-01-01&end=2019-12-28 | python3 -m json.tool
{
    "result": {
        "2019-01-31 00:00:00": {
            "firm": "Nomura",
            "to_grade": 1
        }
    }
}
```

### Recommendations

```bash
$ curl -X GET http://0.0.0.0:5000/stock/recommendations/?ticker=MSFT&start=2019-01-01&end=2019-12-28 | python3 -m json.tool
{
    "result": {
        "2019-01-31 00:00:00": {
            "firm": "Nomura",
            "to_grade": 1
        }
    }
}
```