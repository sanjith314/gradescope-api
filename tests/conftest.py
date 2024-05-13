import pytest
from gradescopeapi.classes.connection import login
from dotenv import load_dotenv
import os

load_dotenv()

"""
Student: enrolled in courses only as a student
Instructor: enrolled in courses only as an instructor
TA: enrolled in different courses as both a student and instructor
"""
GRADESCOPE_CI_STUDENT_EMAIL = os.getenv("GRADESCOPE_CI_STUDENT_EMAIL")
GRADESCOPE_CI_STUDENT_PASSWORD = os.getenv("GRADESCOPE_CI_STUDENT_PASSWORD")
GRADESCOPE_CI_INSTRUCTOR_EMAIL = os.getenv("GRADESCOPE_CI_INSTRUCTOR_EMAIL")
GRADESCOPE_CI_INSTRUCTOR_PASSWORD = os.getenv("GRADESCOPE_CI_INSTRUCTOR_PASSWORD")
GRADESCOPE_CI_TA_EMAIL = os.getenv("GRADESCOPE_CI_TA_EMAIL")
GRADESCOPE_CI_TA_PASSWORD = os.getenv("GRADESCOPE_CI_TA_PASSWORD")


@pytest.fixture
def create_session():
    def _create_session(account_type: str = "student"):
        """Creates and returns a session for testing"""

        match account_type.lower():
            case "student":
                return login(
                    GRADESCOPE_CI_STUDENT_EMAIL, GRADESCOPE_CI_STUDENT_PASSWORD
                )
            case "instructor":
                return login(
                    GRADESCOPE_CI_INSTRUCTOR_EMAIL, GRADESCOPE_CI_INSTRUCTOR_PASSWORD
                )
            case "ta":
                return login(
                    GRADESCOPE_CI_TA_EMAIL, GRADESCOPE_CI_TA_PASSWORD
                )
            case _:
                raise ValueError(
                    "Invalid account type: must be 'student' or 'instructor' or 'ta'"
                )

    return _create_session
