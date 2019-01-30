import  re
import collections
from pandas import  read_csv
import pandas as pd
from collections import Counter
import csv

list_data = []
with open("/home/sindhu/PycharmProjects/sindhu/oracle/oracle.ora") as tns_file:
    with open("test_tns.ora", 'w+') as output:
        lines =tns_file.read()
        lines =re.sub(r'[^\w\s]','',lines.lower())
        d = collections.defaultdict(list)
        lines = lines.split()
        key_index = []
        for k,s in enumerate(lines):
            if s =='description':
                key_index.append(k)
        key_index=key_index+[len(lines)]
        start_key =key_index[1:]
        end_key = key_index[:-1]
        for i in zip(end_key,start_key):
            start, end = i
            extracted_data = lines[start:end]
            list_data.append(extracted_data)

host = []
port = []
default_database = []
list_fi = []
for l in list_data:
    list_dic = []
    host_ = []
    port_ = []
    default_database_ = []
    for i,v in enumerate(l):

        if v == 'host':
            next_value=l[i+1]
            host_.append(next_value)
            # list_dic.append({'host': next_value})
        elif v == 'port':
            next_value = l[i + 1]
            port_.append(next_value)
            # list_dic.append({'host': next_value})
        elif v == 'service_name' or v == 'sid':
            next_value = l[i + 1]
            # list_dic.append({'default_database':next_value})
            default_database_.append(next_value)
    list_fi.append([host_,port_,default_database_])
for i in list_fi:
    if len(i[0]) != len(i[2]):
        i[2] = i[2] +i[2]
        host.append(i[0])
        port.append(i[1])
        default_database.append(i[2])
    else:
        host.append(i[0])
        port.append(i[1])
        default_database.append(i[2])
# host = [y for x in host for y in x ]
host_ = []
exodata = []
for x in host:
    for y in x:
        if y.startswith('edw'):
            exodata.append("YES")
            host_.append(y)
        else:
            exodata.append("NO")
            host_.append(y)

port = [y for x in port for y in x ]
default_database = [y for x in default_database for y in x ]


with open('oracle.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    data = list(zip(host_, port,default_database,exodata))
    for row in data:
        row = list(row)
        spamwriter.writerow(row)

name_=['service_name', 'port','default_database','exo_data']
df = pd.read_csv('oracle.csv',names=name_)
df_ = df.to_csv('oracle.csv', index=None)
print('programmed successfully')



        # host = []
        # port = []
        # default_database = []
        # for i,v in enumerate(lines):
        #     # print(i,v)
        #     if v == 'host':
        #         next_value=lines[i+1]
        #         host.append(next_value)
        #     elif v == 'port':
        #         next_value = lines[i + 1]
        #         port.append(next_value)
        #     elif v == 'service_name' or v == 'sid':
        #         print(v,i)
        #         next_value = lines[i + 1]
        #         print(next_value,i+1)
        #         default_database.append(next_value)
        # print(host)
        # print(port)
        # print(default_database)
        # import csv
        #
        # with open('oracle.csv', 'w', newline='') as csvfile:
        #     spamwriter = csv.writer(csvfile, delimiter=',',
        #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #
        #     data = list(zip(host, port,default_database))
        #     for row in data:
        #         row = list(row)
        #         spamwriter.writerow(row)
        # print("Program completed")
        #



