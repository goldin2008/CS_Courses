from collections import OrderedDict

# CREATE table
fhand = open('table.txt')
# table = dict()
table = OrderedDict()   # Use old version dict() whose element order is sortable
# print table
cnt = 0
for line in fhand:
    cnt = cnt + 1
    if (not line or len(line) == 1):
        continue
    else:
        # line = line.upper()
        line = line.replace('\\', ' ')
        # print line
        delimiter = ':'
        # node_name, node_value = line.split(delimiter)
        line = line.split(delimiter)
        node_name = line[0]
        line[1] = line[1].lstrip()
        line[1] = line[1].rstrip()
        node_value = line[1].split(', ')
        for value in node_value:
            # print 'a = ', value, 'type: ', type(value)
            # print 'start = ', value[0]
            if value[0].isalpha():
                # print 'value = ', value
                # value = value[1:]
                # node_value.replace(value, value[1:])
                index = node_value.index(value)  # Find the index of the old value
                node_value[index] = value[1:]   # Replace the old value with the new one

        table[node_name] = node_value   # table is dict()
        # print line.split(delimiter)

# print 'Line Count:', cnt
# print table
# print len(table)

# for key in table:
#     print key, table[key], len(table[key])


# READ sample informaiton
fhand = open('DNA-database.txt')
count = 0
for line in fhand:
    count = count + 1
    # if (line):
    #     print 'No. ', count, 'Length', len(line), ' ', line
    # else:
    #     print 'Empty'

    if (not line or len(line) == 2):
        continue
    elif (line[0] == '>'):
        print '\nSample Name: ', line
        # pass
    else:
        # Construct sample list
        # line = line.upper()
        line = line.rstrip()
        sample = line.split(' ')
        # print sample
        # print len(sample)
        for each in sample:
            if each[0].isalpha():
                index = sample.index(each)
                sample[index] = each[1:]
        # print 'new sample: ', sample
        # print len(sample)
        ##########################
        # com_value = 0 # Stop HERE, Need to Continue
        max_value = 0
        stop = 0
        ##########################
        node_freq = dict()
        # print node_freq
        print 'Mutations Found: '
        # Check each node in the tree
        label = ''
        for key in table:
            com_value = 0
            # Check each value in the node
            for value in table[key]:
                if value in sample: # if the sample contains this value, com_value increment by 1
                    com_value = com_value + 1
            if com_value > max_value:
                max_value = com_value
                node_freq[key] = max_value
                label = key
            else:
                continue
        # items = [(v, k) for k, v in node_freq.items()]
        # items.sort()
        # items.reverse()             # so largest is first
        # node_freq = [(k, v) for v, k in items]
        # print node_freq   # This method change node_freq from dict() to list already
        print '\nClassification: ', max(node_freq, key = node_freq.get)
        print '\nClassification (label): ', label
# print 'Line Count:', count

