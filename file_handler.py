def file_handler():
    with open('example.txt', 'rt') as f:
        data = f.read()
        data = data.replace('placement', 'screening')
    with open('example.txt', 'wt') as fw:
        fw.write(data)


file_handler()