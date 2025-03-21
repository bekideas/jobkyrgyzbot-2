import logging

def log_action(user_id: int, action: str):
    logging.info(f"User {user_id} - {action}")
