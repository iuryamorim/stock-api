"""
Provide implementation for finance services.
"""
from typing import (
    Dict,
    List,
    Union,
)

import yfinance as yf


class Finance:
    """
    Finance services object implementation.
    """

    msft = yf.Ticker("MSFT")

    def get_dividends(self, ticker: str, start: str, end: str):
        history = yf.Ticker(ticker).history(start=start, end=end)

        dividends = dict((str(index), dividend) for index, dividend in zip(history.index, history.Dividends))

        return dividends

    def get_close_price(self, ticker: str, start: str, end: str):
        history = yf.Ticker(ticker).history(start=start, end=end)

        close_price = dict((str(index), close) for index, close in zip(history.index, history.Close))

        return close_price
    
    def get_recommendations(self, ticker: str, start: str, end: str):
        parser_dict: Dict[str, Union[int, float]] = {
            'Buy': 1,
            'Neutral': 0,
            'Strong Buy': 1.5,
            'Sell': -1,
            'Strong Sell': -1.5,
            'Positive': 1,
            'Negative': -1,
        }

        recommendations = yf.Ticker(ticker).recommendations
        
        recommendations = recommendations[recommendations.index > start]

        recommendations = recommendations[recommendations.index < end]

        recommendations = {
            str(index): {
                'firm': firm,
                'to_grade': parser_dict.get(to_grade, 0),
            }

            for index, firm, to_grade in zip(
                recommendations.index, recommendations.Firm, recommendations['To Grade'],
            )
        }

        return recommendations
