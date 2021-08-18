'''

import os

#current working directory
print(os.getcwd())


import os
os.mkdir('newpython')
print('Folder created')



import os
os.rmdir('newpython')
print('Folder removed')




import os
os.rename('Data.txt','NewData.txt')
print('File Renamed...')


import os
os.remove('NewData.txt')
print('File removed')



#to check existance of file or folder
import os
print(os.path.exists('EmpData.txt'))



import os
#wondows-nt
print(os.name)



import os
d=os.listdir('Desktop\Python')
print(d)


'''












