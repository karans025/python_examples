student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Encountered Key Error While trying to get Last Name")
except TypeError as error:
    print("Encountered Type Error While Trying to Add Integer and String")
    print(error)
except Exception:
    print("Unknown Error Encountered")
print("This Code will Execute due to exception handling")
