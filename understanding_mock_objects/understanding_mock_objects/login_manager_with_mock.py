from understanding_mock_objects.interfaces.logger import ILogger


class LoginManagerWithMock:
    def __init__(self, logger: ILogger) -> None:
        self._log = logger
        self._users = {}

    def is_login_ok(self, user: str, password: str) -> bool:
        self._log.write("yo")
        return user in self._users and self._users[user] == password
