def get_profile(name, age, *args, **kwargs):
    if not isinstance(age, int):
        raise ValueError('Age must be of type <int>')
    if len(args) > 5:
        raise ValueError('Maximally 5 sports are allowed')
    dct = {'name': name, 'age': age}
    if args:
        dct['sports'] = list(sorted(args))
    if kwargs:
        dct['awards'] = kwargs
    return dct

