from AI_services_team_final_with_key import interview_chat
from speech_to_text import speech_to_text


def voice_interview_round(history=None):

    if history is None:
        history = []

    user_text = speech_to_text()

    if not user_text:
        return None, None, history

    if user_text.strip().lower() in ["توقف", "stop", "exit", "quit"]:
        return "توقف", None, history

    ai_response, history = interview_chat(user_text, history)

    return user_text, ai_response, history