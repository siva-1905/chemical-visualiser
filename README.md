# Chemical Visualiser

Full-stack application with a Django backend, React web frontend, and Tkinter desktop frontend.

The app uploads CSV equipment data, generates analytics, charts, and PDF reports.

---

## Features

* CSV upload API
* Equipment summary analytics
* Chart visualization
* PDF report generation
* Web frontend
* Desktop frontend
* Shared Django backend

---

## Backend Setup (Django)

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## Web Frontend Setup

```bash
cd frontend
npm install
npm start
```

Web app runs at:

```
http://localhost:3000
```

---

## Desktop App Setup

```bash
python desktop_app.py
```

Make sure Django backend is running first.

---

## Sample CSV Format

```
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump A,Pump,20,5,100
Pump B,Pump,25,6,110
Valve A,Valve,15,4,90
```

---

## Author

Siva Priya A

