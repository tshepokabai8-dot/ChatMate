print("🔄 UPDATE SYSTEM LOADED")

CURRENT_VERSION = "1.0"


def check_update():
    latest_version = "1.0"

    if CURRENT_VERSION == latest_version:
        return "ChatMate is up to date ✅"

    else:
        return "A new version is available 🚀"