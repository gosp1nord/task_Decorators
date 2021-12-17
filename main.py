from datetime import datetime
import os

PATH = 'Logs'

def creater_decor(path):
    def decor_any_func(func):
        def log_call_func(*args, **kwargs):
            if os.path.isfile(f'{path}\\log.txt'):
                pass
            else:
                with open(f'{path}\\log.txt', 'w', encoding="utf-8") as f:
                    pass

            call_time = datetime.now()
            res_return = func(*args, **kwargs)
            if res_return is None:
                res_return = "Нет"
            if len(args) == 0:
                args = "Нет"
            if len(kwargs) == 0:
                kwargs = "Нет"
            res = f"[{call_time.day}-{call_time.month}-{call_time.year} {call_time.hour}:{call_time.minute}:{call_time.second}] " \
                  f"Вызвана функция {func.__name__}, в которой:\n" \
                  f"позиционные аргументы: {args}\n" \
                  f"именованные аргументы: {kwargs}\n" \
                  f"возвращаемое значение: {res_return}\n"
            with open(f'{path}\\log.txt', 'a', encoding="utf-8") as file:
                file.write(res)
            return res_return
        return log_call_func
    return decor_any_func


if __name__ == "__main__":
    @creater_decor(PATH)
    def any_func(num, num2, num3, num4=1000):
        print(f"Тестовая функция {num} - {num2} - {num3} - {num4}")

    any_func(None, 4, 76, num4=236)
