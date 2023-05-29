import sys

clients = [
    {
        'name': 'irwin',
        'company': 'neksys',
        'email': 'irwinet@gmail.com',
        'position': 'Software engenier'
    },
    {
        'name': 'juan',
        'company': 'twitter',
        'email': 'juan@twitter.com',
        'position': 'Software engenier'
    }
]

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')

def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'],
        ))

def update_client(client_id, update_client):
    global clients
    if len(clients) - 1 >= client_id:
        clients[client_id] = update_client
    else:
        print('Client is not in clients list')

def delete_client(client_id):
    global clients
    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

def search_client(client_name):
    global clients
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b            

def _add_comma():
    global clients
    clients+=','

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client

def _print_welcome():
    print("WELCOME TO PLATZI VENTAS")
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('[F]ibonacci')

def _get_client_field(field_name, message= 'What is the client {}?'):
    field = None 
    while not field:
        field = input(message.format(field_name))
    return field

def _get_client_name():
    client_name = None
    
    while not client_name:
        client_name = input('What si the client name? ')
        if client_name == 'exit':
            client_name = None
            break
    
    if not client_name:
        sys.exit()

    return client_name

if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    elif command == 'F':
        fib1 = fibonacci(10)
        fib_nums = [num for num in fib1]
        print(fib_nums)
    else:
        print('Invalid command')