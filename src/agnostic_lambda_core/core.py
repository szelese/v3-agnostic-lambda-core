def process_data(payload: dict) -> dict:
    user = payload.get("user", "Pilot")
    # environment-agnostic logic with no external dependencies
    return {
        "message": f"Hello {user}! All OK!",
        "status": "works", 
        "subsystem": "agnostic-core-v3"
    }