#   1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность
# сетевых узлов. Аргументом функции является список, в котором каждый сетевой узел должен быть представлен
# именем хоста или ip-адресом. В функции необходимо перебирать ip-адреса и проверять их доступность с
# выводом соответствующего сообщения («Узел доступен», «Узел недоступен»). При этом ip-адрес
# сетевого узла должен создаваться с помощью функции ip_address().

import locale
import platform
from subprocess import Popen, PIPE
from ipaddress import ip_address


def host_ping(ips):
    for ip in ips:
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
    ip_list = []
    address_bytes = [int(x) for x in ip.split('.')]

    if 255 - address_bytes[3] < iters - 1:
        print('error: You can only change the last act of IP')
    else:
        for i in range(0, iters):
            ip_list.append(ip_address(ip) + i)

        host_ping(ip_list)


if __name__ == '__main__':
    enter_ping()

# Пример выполнения
# (venv) sasha@air-sasha pyQt % python3 main.py
# Введите IP: 0.0.0.0 (Личный IP был заменён на вымышленный без изменения результатов выполнения)
# Введите кол-во адресов, которое необходимо проверить: 20
# ping 0.0.0.0: Узел не доступен
# ping 0.0.0.1: Узел не доступен
# ping 0.0.0.2: Узел не доступен
# ping 0.0.0.3: Узел не доступен
# ping 0.0.0.4: Узел не доступен
# ping 0.0.0.5: Узел не доступен
# ping 0.0.0.6: Узел не доступен
# ping 0.0.0.7: Узел доступен
# ping 0.0.0.8: Узел не доступен
# ping 0.0.0.9: Узел не доступен
# ping 0.0.0.10: Узел доступен
# ping 0.0.0.11: Узел доступен
# ping 0.0.0.12: Узел не доступен
# ping 0.0.0.13: Узел не доступен
# ping 0.0.0.14: Узел не доступен
# ping 0.0.0.15: Узел не доступен
# ping 0.0.0.16: Узел не доступен
# ping 0.0.0.17: Узел не доступен
# ping 0.0.0.18: Узел не доступен
# ping 0.0.0.19: Узел не доступен
