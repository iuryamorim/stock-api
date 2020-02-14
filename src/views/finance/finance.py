"""
Provide implementation for finance views.
"""
from http import HTTPStatus
from typing import (
    Any,
    Dict,
    List,
    Tuple,
    Union,
)

from flask import (
    jsonify,
    request,
)

from src.services.finance import Finance

finance: Finance = Finance()


def get_dividends() -> Tuple[Any, HTTPStatus]:
    request_data= request.args

    dividends = finance.get_dividends(
        ticker=request_data.get('ticker'),
        start=request_data.get('start'),
        end=request_data.get('end'),
    )

    return jsonify({'result': dividends}), HTTPStatus.OK


def get_close_price() -> Tuple[Any, HTTPStatus]:
    request_data = request.args

    dividends = finance.get_close_price(
        ticker=request_data.get('ticker'),
        start=request_data.get('start'),
        end=request_data.get('end'),
    )

    return jsonify({'result': dividends}), HTTPStatus.OK


def get_recommendations() -> Tuple[Any, HTTPStatus]:
    request_data = request.args

    dividends = finance.get_recommendations(
        ticker=request_data.get('ticker'),
        start=request_data.get('start'),
        end=request_data.get('end'),
    )

    return jsonify({'result': dividends}), HTTPStatus.OK
