from flask import Blueprint,request
from Book.Naverbookapi import Naverbook
from Book.Naverbookapiauth import Naverbookauth
from Book.Weather import Weather
import json
from Book import db
from Book.models import webhook
from flask import Blueprint
from Book.dialogflowapi import dialogflow_chat


bp = Blueprint('dialogapi', __name__, url_prefix='/dialogapi/')


@bp.route('/dialogflowtest')
def dialogflowtest():
    result = dialogflow_chat('투표')
    return result.query_result.fulfillment_text