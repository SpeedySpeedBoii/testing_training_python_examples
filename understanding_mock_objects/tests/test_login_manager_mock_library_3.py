from mock import Mock
from understanding_mock_objects.login_manager_with_mock import LoginManagerWithMock
from understanding_mock_objects.interfaces.logger import ILogger, LoggerException
from understanding_mock_objects.interfaces.web_service import IWebService
from understanding_mock_objects.login_manager_with_mock_and_stub import LoginManagerWithMockAndStub


def test__is_login_ok__when_called__writes_to_log():
    mock_log = Mock(spec=ILogger)
    login_manager = LoginManagerWithMock(mock_log)

    login_manager.is_login_ok("", "")

    # In the C# example, this expectation is specified in the 'arrange' step of the test.
    mock_log.write.assert_called_once_with("yo")


def test__is_login_ok__logger_throws_exception__writes_to_web_service():
    stub_log = Mock(spec=ILogger)
    mock_service = Mock(spec=IWebService)
    stub_log.write.side_effect = LoggerException
    login_manager = LoginManagerWithMockAndStub(stub_log, mock_service)

    login_manager.is_login_ok("", "")

    # In the C# example, this expectation is specified in the 'arrange' step of the test.
    mock_service.write.assert_called_once_with("got exception")
