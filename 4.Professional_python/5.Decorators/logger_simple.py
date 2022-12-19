import requests
from datetime import datetime


def get_logfile(some_function):
    def foo(*args, **kwargs):
        result = some_function(*args, **kwargs)
        file_line = ('<{}> Функция:<{}> Args:<{}> Kwargs:<{}> Результат:<{}>\n'.format(datetime.now().strftime
                                                ("%d %B %Y, %H:%M:%S"), some_function.__name__, args, kwargs, result))
        with open('log_file.txt', 'a+', encoding='utf-8') as file:
            file.write(file_line)
        return result
    return foo


@get_logfile
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://netology.ru')
