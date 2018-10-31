#coding:utf-8
#!/usr/bin/python

import sys

def if_in(host):
	with open(file2) as f:
		file2_str = f.read()
	file2_list  = file2_str.split('\n')
	file2_host_list = list()
	for item in file2_list:
		file2_host_list.append(item.split(',')[0])
	if host in file2_host_list:
		return file2_list[file2_host_list.index(host)]
	return None

if __name__ == '__main__':
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	output = sys.argv[3]

	result  = list()

	with open(file1) as f1:
		file1_str = f1.read()
	file1_list = file1_str.split('\n')
	for item in file1_list:
		host = item.split(',')[0].strip()
		r = if_in(host)
		if r is not None:
			result.append(str(item).strip() + ',' + str(r).strip())
		else:
			result.append(str(item).strip())
	with open(output, 'w') as f:
		for item in result:
			f.write(item + '\n')

