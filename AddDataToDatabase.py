import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://sandyface-804db-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {   # The details for the students
    "12345":
        {
            "name": "Santhosh",
            "major": "IT std",
            "starting_year": 2021,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "54321":
        {
            "name": "Samuel Roysten;",
            "major": "IT std",
            "starting_year": 2021,
            "total_attendance": 10,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "108481":
        {
            "name": "Azhar Alauddin",
            "major": "Informatics",
            "starting_year": 2018,
            "total_attendance": 4,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "76543":
        {
            "name": "Godwin",
            "major": "Medical",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "A",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "11559":
        {
            "name": "Nithyanantham",
            "major": "NASA",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "A",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "1153559":
        {
            "name": "Hero man",
            "major": "safeguard",
            "starting_year": 2023,
            "total_attendance": 109,
            "standing": "e",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        } 

}

# JSON in Python is Dictionary
for key, value in data.items():
    ref.child(key).set(value)

    print("The file Upload has been done")