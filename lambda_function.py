import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

from utils import generate_session_id, handle_conversation_voiceflow


def make_response(handler_input: HandlerInput, speak_output: str) -> Response:
    return handler_input.response_builder.speak(speak_output).ask(speak_output).response


class LaunchRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        session_id = generate_session_id()
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr["session_id"] = session_id
        speak_output = handle_conversation_voiceflow(session_id, "init via alexa")
        return make_response(handler_input, speak_output)
    

class FallbackIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input) \
            or ask_utils.is_intent_name("ResponseIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> bool:
        session_attr = handler_input.attributes_manager.session_attributes
        session_id = session_attr["session_id"]
        prompt = handler_input.request_envelope.request.intent.slots["prompt"].slot_value.value
        speak_output = handle_conversation_voiceflow(session_id, prompt)
        return make_response(handler_input, speak_output)


class CatchAllExceptionHandler(AbstractExceptionHandler):

    def can_handle(self, handler_input: HandlerInput, exception: Exception) -> bool:
        return True

    def handle(self, handler_input: HandlerInput, exception: Exception) -> Response:
        logger.error(exception, exc_info=True)
        speak_output = "Tut mir Leid. Etwas ist schief gelaufen. Bitte versuche es erneut. Fehler: " + str(exception)
        return make_response(handler_input, speak_output)


class SessionEndedRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "Der Intent " + intent_name + " wurde gewählt."
        return handler_input.response_builder.speak(speak_output).response
    

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())
sb.add_request_handler(IntentReflectorHandler())
lambda_handler = sb.lambda_handler()
