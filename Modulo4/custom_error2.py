class CustomException(Exception):
    def __init__ (self, _code = 500, _message = 'Internal Server Error') -> None:
        self.code = _code
        self.message = _message

try:
    raise CustomException
except Exception as error:
    print(error.code)
    print(error.message)

try:
    raise CustomException (400, 'Bad Request')
except Exception as error:
    print(error.code)
    print(error.message)
