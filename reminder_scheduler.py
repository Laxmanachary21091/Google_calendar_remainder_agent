from apscheduler.schedulers.background import BackgroundScheduler
from voice_reminder import speak
from datetime import datetime
import time

scheduler = BackgroundScheduler()

def schedule_reminder(date_str, title, time_str):
    dt_str = f"{date_str} {time_str}"
    reminder_time = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    scheduler.add_job(lambda: speak(f"Hey! Reminder: You have {title} now!"), 'date', run_date=reminder_time)

def start_scheduler():
    scheduler.start()
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
