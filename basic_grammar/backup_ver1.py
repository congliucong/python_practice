import os
import time

# 1.	需要备份的文件与目录将被
# 指定在一个列表中。
source = ['"D:\\My Documents\\text.txt"', 'D:\\My Documents']

# 2.	备份文件必须存储在一个
# 主备份目录中
target_dir = 'D:\\Backup'

# 3.备份文件将打包压缩成	zip	文件。
# 4.zip	压缩文件的文件名由当前日期与时间构成。
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

print('target is ', target)

# 	5.	我们使用	zip	命令将文件打包成	zip	格式
zip_command = 'zip	-r	{0}	{1}'.format(target, ' '.join(source))
# 运行备份
print('Zip	command	is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful	backup	to', target)
else:
    print('Backup	FAILED')
