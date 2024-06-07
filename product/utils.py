def verify_admin(user):
    if user.is_superuser or user.is_staff:
        
        return True
    return False

