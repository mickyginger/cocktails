def error_handler(errors):
    for key in errors:
        errors[key] = '; '.join(errors[key])

    return errors
