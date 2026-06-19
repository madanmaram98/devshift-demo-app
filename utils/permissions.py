def is_admin(user) -> bool:
    # BUG: returns True even for None user
    return user["role"] == "admin"

def require_admin(user):
    if not is_admin(user):
        raise Exception("forbidden")   # bare Exception, should be a proper HTTP error
