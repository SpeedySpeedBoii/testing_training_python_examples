from understanding_mock_objects.interfaces.logger import ILogger, LoggerException
from understanding_mock_objects.interfaces.web_service import IWebService


class LoginManagerWithMockAndStub:
    def __init__(self, logger: ILogger, service: IWebService) -> None:
        self._log = logger
        self._service = service
        self._users = {}

    def is_login_ok(self, user: str, password: str) -> bool:
        try:
            self._log.write("yo")
        except LoggerException as e:
            self._service.write("got exception")
            print(e)

        return user in self._users and self._users[user] == password
