import random
import string



BASE_URL = "https://stellarburgers.education-services.ru"
NAME = "test"
PASSWORD = "lo34pd"
EMAIL_BASE = "eugene_rusakov_50"


def email_generator():
    suffix = f"{random.randint(0, 999):03d}"
    domain = "".join(random.choices(string.ascii_lowercase, k=6))
    return f"{EMAIL_BASE}_{suffix}@{domain}.ru"
