# 2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться
# должен только последний октет каждого адреса. По результатам проверки должно выводиться соответствующее
# сообщение.

import locale
import platform
from multiprocessing import Process
from subprocess import Popen, PIPE
from ipaddress import ip_address


def host_ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '1', ip.__str__()]
    reply = Popen(args, stdout=PIPE, stderr=PIPE)
    code = reply.wait()
    if code == 0:
        print(f"ping {ip.__str__()}: Узел доступен")
    else:
        print(f"ping {ip.__str__()}: Узел не доступен")


def enter_ping():
    ip = input('Введите IP: ')
    iters = int(input('Введите кол-во адресов, которое необходимо проверить: '))
    address_bytes = [int(x) for x in ip.split('.')]

    if 255 - address_bytes[3] < iters - 1:
        print('error: You can only change the last act of IP')
    else:
        for i in range(0, iters):
            proc = Process(target=host_ping, args=(ip_address(ip) + i,))
            proc.start()


if __name__ == '__main__':
    enter_ping()
