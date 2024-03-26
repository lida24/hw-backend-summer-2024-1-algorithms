__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    if 0 <= seconds < 60:
        return f"{seconds:02d}s"
    elif 60 <= seconds < 3600:
        return f"{seconds // 60:02d}m{seconds % 60:02d}s"
    elif 3600 <= seconds < 86400:
        return f"{seconds // 3600:02d}h{seconds % 3600 // 60:02d}m{seconds % 3600 % 60:02d}s"
    return f"{seconds // 86400:02d}d{seconds % 86400 // 3600:02d}h{seconds % 86400 % 3600 // 60:02d}m{seconds % 86400 % 3600 % 60:02d}s"
