from crewai import Agent
from openai import OpenAI
from google_calendar_service import fetch_upcoming_events
from database import init_db, save_event
from reminder_scheduler import schedule_reminder, start_scheduler
import datetime, os
from dotenv import load_dotenv

load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
init_db()

def is_important(title):
    keywords = ["meeting", "interview", "presentation", "important"]
    return any(k.lower() in title.lower() for k in keywords)

def main():
    events = fetch_upcoming_events()
    for e in events:
        title = e['summary']
        start = e['start'].get('dateTime', e['start'].get('date'))
        date_obj = datetime.datetime.fromisoformat(start.replace("Z", "+00:00"))
        date_str = date_obj.strftime("%Y-%m-%d")
        time_str = date_obj.strftime("%H:%M:%S")
        if is_important(title):
            save_event(date_str, title, time_str)
            schedule_reminder(date_str, title, time_str)
            print(f"Saved and scheduled: {title} at {date_str} {time_str}")
    start_scheduler()

if __name__ == "__main__":
    main()
