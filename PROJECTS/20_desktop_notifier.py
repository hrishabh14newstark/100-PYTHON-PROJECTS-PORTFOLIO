"""
20: Desktop Notifier
Push OS-level alerts using plyer library.
"""
def send_notification(title, message):
    try:
        from plyer import notification
        notification.notify(title=title, message=message, timeout=5)
        print("Notification sent.")
    except ImportError:
        print(f"[Fallback Alert] {title}: {message}")

if __name__ == "__main__":
    send_notification("Reminder", "Drink water and stretch!")
