import requests
from datetime import datetime


file_path = 'log_file.txt'


def get_log_path(path):
    def get_logfile(some_function):
        def foo(*args, **kwargs):
            result = some_function(*args, **kwargs)
            file_line = ('***<{}> Функция:<{}> Args:<{}> Kwargs:<{}> Результат:<{}>\n'.format(datetime.now().strftime
                                                ("%d %B %Y, %H:%M:%S"), some_function.__name__, args, kwargs, result))
            with open(path, 'a+', encoding='utf-8') as file:
                file.write(file_line)
            return result
        return foo
    return get_logfile


@get_log_path(file_path)
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://netology.ru')