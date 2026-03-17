def format_message(text: str) -> str:
    border = "*" * (len(text) + 6)
    return f"{border}\n** {text} **\n{border}"