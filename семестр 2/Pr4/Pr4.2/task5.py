def require_role(required_role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != required_role:
                raise PermissionError(f"Доступ заборонено! Очікується роль: {required_role}")
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_system_files(user_role):
    print("Системні файли успішно видалено.")

delete_system_files("admin")
delete_system_files("guest")