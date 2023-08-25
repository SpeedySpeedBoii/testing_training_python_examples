from understanding_mock_objects.interfaces.logger import ILogger
from understanding_mock_objects.login_manager_with_mock import LoginManagerWithMock
from typing import Optional


class FakeILogger(ILogger):
    def __init__(self):
        self.text: Optional[str] = None

    def write(self, text: str) -> None:
        self.text = text


def test__is_login_ok__when_called__writes_to_log():
    mock_log = FakeILogger()
    login_manager = LoginManagerWithMock(mock_log)

    login_manager.is_login_ok("", "")

    assert mock_log.text == "yo"
