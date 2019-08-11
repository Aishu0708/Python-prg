def main():
    print('Sample Input Data')
    print('Tom,19,80\n', 'John,20,90\n',\
        'Jony,17,91\n', 'Jony,17,93\n', 'Json,21,85\n')
    rows = []
    print 'Enter Data : '
    while True:
        rawData = raw_input('') 
        if not rawData:
            break
        tpl = tuple(rawData.split(','))
        rows.append(tpl)
    print 'sorted List'
    return sorted(rows)
if __name__ == '__main__':
    print main()
