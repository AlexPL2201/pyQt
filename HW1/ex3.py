# 2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться
# должен только последний октет каждого адреса. По результатам проверки должно выводиться соответствующее
# сообщение.

import platform
from multiprocessing import Process, Pipe
from subprocess import Popen, PIPE
from ipaddress import ip_address
from tabulate import tabulate


def host_ping(ip, conn):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '1', ip.__str__()]
    reply = Popen(args, stdout=PIPE, stderr=PIPE)
    code = reply.wait()
    conn.send(code)


def enter_ping():
    ip = input('Введите IP: ')
    iters = int(input('Введите кол-во адресов, которое необходимо проверить: '))
    address_bytes = [int(x) for x in ip.split('.')]

    if 255 - address_bytes[3] < iters - 1:
        print('error: You can only change the last act of IP')
    else:
        results = []
        for i in range(0, iters):
            parent_pipe, child_pipe = Pipe()
            ip_v4 = ip_address(ip) + i
            proc = Process(target=host_ping, args=(ip_v4, child_pipe,))
            proc.start()
            code = parent_pipe.recv()
            # Не сумел придумать, как работать с результатом, сохранив идею многопроцессорности. Метод host_ping
            # вызывается каждую итерацию в разных дочерних процессах, но итерация не завершится до тех пор
            # пока в конвеер не поступят данные
            if code == 0:
                results.append([ip_v4.__str__(), ''])
            else:
                results.append(['', ip_v4.__str__()])
        print(results)
        print(tabulate(results, headers=['Reachable', 'Unreachable']))


if __name__ == '__main__':
    enter_ping()
