def userEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "name": item["name"],
        "task": item["task"],
        "start_date": item["start_date"],
        "end_date": item["end_date"]
    }
def usersEntity(entity) -> list:
    return[userEntity(item) for item in entity]