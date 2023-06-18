try:
    raise Exception ('rut', '12.345.678-9', 'Invalidate Rut Format')
except Exception as error:
    print(type(error))
    print(error.args)
    print(error)

    key, value, message = error.args

    print('key ->', key)
    print('value ->', value)
    print('message ->', message)

