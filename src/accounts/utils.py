from django.core.validators import RegexValidator


def profile_upload_location(instance, filename):
    try:
        extension = filename.split(".")[1].lower()
        extension = "." + extension
    except Exception as e:
        print(e, "Handled")
        extension = ""
    filename = str(instance)
    filename = filename.replace(" ", "-")
    filename = filename + extension
    location = "article/images/"
    return '%s/%s' % (location, filename)


mobile_regex = RegexValidator(regex=r'^\d{10,10}$',
                              message="Phone number must be exact 10 digits.")
