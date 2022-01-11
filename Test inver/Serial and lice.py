
import subprocess

win_key = subprocess.check_output('wmic path softwarelicensingservice get oa3xoriginalproductkey').decode().split('\n')[1].strip()
serial_number = subprocess.check_output('wmic bios get serialnumber').decode().split('\n')[1].strip()


# win_key= 'Раз, два, три, четыре, пять\n'
# serial_number = 'Я иду сервак ломать...\n'

f = open('sereal and lice.txt', 'w', encoding='UTF-8')
f.write('1.Win ключ: ' + win_key + '\n')
f.write('2.Cерийный номер: ' + serial_number + '\n')
f.close()

print('1.Win ключ:', win_key)
print('2.Cерийный номер: ', serial_number)



# print('ты получишь два параметра компьютера:')
#
# import subprocess
# code = subprocess.call(["tracert", "www.yahoo.com"])
# .decode().split('\n')[1].strip()