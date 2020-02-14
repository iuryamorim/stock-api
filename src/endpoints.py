"""
Provide implementation of endpoints.
"""
from flask import Blueprint

from src.views.finance import (
    get_close_price,
    get_dividends,
    get_recommendations,
)

blueprint = Blueprint(name='blueprint', import_name=__name__)

blueprint.add_url_rule(rule='/stocks/dividends/', view_func=get_dividends)
blueprint.add_url_rule(rule='/stocks/close/', view_func=get_close_price)
blueprint.add_url_rule(rule='/stocks/recommendations/', view_func=get_recommendations)
