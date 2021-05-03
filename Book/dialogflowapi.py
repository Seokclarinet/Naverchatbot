import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

# 파이썬 환경변수 선언
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "helpbot-r9vc-40b591de0184.json"

# 프로젝트 ID 등록 (Reservationbot)
DIALOGFLOW_PROJECT_ID = 'helpbot-r9vc'
DIALOGFLOW_LANGUAGE_CODE = 'ko'

session_client = dialogflow.SessionsClient()

def dialogflow_chat(text, session_id='me'):
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    return response