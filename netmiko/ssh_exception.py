from paramiko.ssh_exception import SSHException
from paramiko.ssh_exception import AuthenticationException


class NetmikoTimeoutException(SSHException):
    """SSH session timed trying to connect to the device."""

    pass


class NetmikoAuthenticationException(AuthenticationException):
    """SSH authentication exception based on Paramiko AuthenticationException."""

    pass


NetMikoTimeoutException = NetmikoTimeoutException
NetMikoAuthenticationException = NetmikoAuthenticationException
class PatternNotFoundException(Exception):
    """Raise when Send_command received pattern not found"""

    def __init__(self, *args: list, output: str='', **kwargs: dict) -> None:
        '''
        @param output: output of the send_command.
        This output can help caller to analyze what was wrong with pattern
        '''
        self.output = output
        super().__init__(*args, **kwargs)
