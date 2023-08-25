from understanding_mock_objects.login_manager_with_mock_and_stub import LoginManagerWithMockAndStub
from understanding_mock_objects.interfaces.logger import ILogger, LoggerException
from understanding_mock_objects.interfaces.web_service import IWebService
from typing import Optional


class FakeLogger2(ILogger):
    def __init__(self):
        self.to_throw: Optional[Exception] = None
        self.text: Optional[str] = None

    def write(self, text: str) -> None:
        self.text = text
        if self.to_throw is not None:
            raise self.to_throw


class FakeWebService(IWebService):
    def __init__(self):
        self.message: Optional[str] = None

    def write(self, message: str) -> None:
        self.message = message


def test__is_login_ok__logger_throws_exception__writes_to_web_service():
    stub_log = FakeLogger2()
    stub_log.to_throw = LoggerException("fake exception")

    mock_service = FakeWebService()

    login_manager = LoginManagerWithMockAndStub(stub_log, mock_service)
    login_manager.is_login_ok("", "")

    assert mock_service.message == "got exception"
