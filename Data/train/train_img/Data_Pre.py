import shutil
i = 1
while i <= 500:
    source=r'C:/Users/Chou/Desktop/DataSet/train_xml/' + str(i) + '.xml'
    destination=r'C:/Users/Chou/Desktop/DataSet/train_xml/' + str(i+20) + '.xml'
    shutil.copyfile(source, destination)
    i=i+1