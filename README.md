
# Trading Economics - Python

[![PyPI version](https://img.shields.io/pypi/v/tradingeconomics.svg)](https://pypi.org/project/tradingeconomics/) ![Unit Tests](https://github.com/tradingeconomics/tradingeconomics-python/actions/workflows/tests.yml/badge.svg) 

The Trading Economics Application Python package provides direct access to millions of time series with economic data, financial markets quotes, commodity prices, crypto currencies data and much more. It also allows you to query Trading Economics  real-time economic calendar and to subscribe to updates. 

#

## Installation


Install the latest version directly from GitHub
```bash
git clone https://github.com/RynhAleh/tradingeconomics-python.git
```

```bash
cd tradingeconomics-python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 flask_app_min/runner.py
```

#

## Authentication

Protect your credentials! Please set your keys as environment variables before you launch your application. This lets you share your code without disclosing your credentials.

### Windows

In Windows, you can permanently set environment variables using a settings window - just type "environment variables" on windows search to locate it. As an alternative, you can temporarily set them using the command line terminal.

```bash
# windows command line
set apikey='guest:guest'
```
### Linux / Mac

```bash
export apikey='guest:guest'
```
### Login - the secure way

```python
import tradingeconomics as te
te.login()
```

### Login - the easy way

```python
import tradingeconomics as te
te.login('guest:guest')
```
Please replace guest:guest with your API key or we will be returning sample data.

#

## Sample Usage

```python
te.getCalendarData()
te.getIndicatorData(country=['mexico', 'sweden'], output_type='df')
te.getMarketsData(marketsField = 'commodities')
te.getMarketsBySymbol(symbols='aapl:us')
te.getFinancialsData(symbol = 'aapl:us', output_type = 'df')
```

## More examples

https://github.com/tradingeconomics/tradingeconomics-python/tree/main/examples

#

## Docker

Try our python interface in a container without installing anything

```bash
docker run -it --name te-python tradingeconomics-python:latest
```
#

## Documentation

https://docs.tradingeconomics.com


#

## Learn More

https://tradingeconomics.com/analytics/api.aspx

