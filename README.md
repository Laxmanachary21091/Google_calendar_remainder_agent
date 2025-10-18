🗓️ Google Calendar Agent with CrewAI + OpenAI
🔍 Overview

This project is an AI-powered Google Calendar Assistant built using the CrewAI framework and integrated with OpenAI’s GPT model.
It connects with your Google Calendar, fetches important events, stores them in a local database, and reminds you — even with voice alerts.

🚀 Features

✅ Fetches all events from your Google Calendar
✅ Detects and stores important events (based on keywords)
✅ Gives voice reminders for upcoming important events
✅ Saves events into a SQLite database (events.db)
✅ Fully customizable .env file for API keys and configuration
✅ Uses CrewAI for modular AI orchestration

🧠 Example

Input (from Google Calendar):

Date: 25-10-2025  
Event: ServiceNow Interview Meet


Output:

Reminder 🔔
"Hey Laxman! You have an important event: ServiceNow Interview Meet today (25-10-2025)"


(Voice reminder is played using pyttsx3)

⚙️ Project Structure
calendar_agent/
│
├── calendar_agent.py            # Main script
├── google_calendar_service.py   # Handles Google Calendar API connection
├── reminder_scheduler.py        # Handles reminder scheduling and voice alerts
├── database.py                  # Stores event data in SQLite
├── .env.example                 # Example environment file
├── requirements.txt             # Python dependencies
└── README.md                    # Documentation (this file)

🧩 Requirements

Python 3.8 or higher

Google Cloud Console account

OpenAI API key

CrewAI framework installed
