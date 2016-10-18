class node:
    name = ''
    ip = ''
    mode = ''

    def __init__(self, name, ip, mode ):
        self.name = name
        self.ip = ip
        self.mode = mode


class host(node):
    def __init__(self, name, ip, mode, port, desc ):
        node.__init__(self, name, ip, mode )
        self.port = port
        self.desc = desc


if __name__ == '__main__':
    n1 = node('cw1', '84.0.191.254', 'N')
    h1 = host('srv1', '84.0.191.1', 'S', 23, 'mail server')

    print( h1. name, h1.ip, h1.desc )

