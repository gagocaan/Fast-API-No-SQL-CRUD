# import os

# import motor.motor_asyncio
# from bson.objectid import ObjectId

# MONGO_DETAILS = os.environ.get("DB_HOST")

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database = client.students

# student_collection = database.get_collection("students_collection")
from google.cloud import ndb

client = ndb.Client()


class Student(ndb.Model):
    fullname = ndb.StringProperty()
    email = ndb.StringProperty()
    course_of_study = ndb.StringProperty()
    year = ndb.IntegerProperty()
    gpa = ndb.FloatProperty()


# helpers
def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }


# Retrieve all students present in the database
async def retrieve_students():
    students = []
    # async for student in student_collection.find():
    #     students.append(student_helper(student))
    with client.context():
        query = Student.query()
        for s in query:
            student = s.to_dict()
            student["_id"] = s.key.id()
            students.append(student_helper(student))
    return students


# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    # student = await student_collection.insert_one(student_data)
    # new_student = await student_collection.find_one({"_id": student.inserted_id})
    with client.context():
        student = Student(
            fullname=student_data["fullname"],
            email=student_data["email"],
            course_of_study=student_data["course_of_study"],
            year=student_data["year"],
            gpa=student_data["gpa"],
        ).put()
        student_data["_id"] = student.id()
        new_student = student_data
    return student_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# Delete a student from the database
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True
