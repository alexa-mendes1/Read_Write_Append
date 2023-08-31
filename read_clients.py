def main():

    clients = open('clients.txt', 'r')
    i = 1
    for client in clients:
        print(str(i) + '. ' + client.rstrip('\n'))
        i += 1

main()