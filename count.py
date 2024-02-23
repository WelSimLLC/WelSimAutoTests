import os

dir_paths = ['04_GUI', 
             '06_MatEditor', 
             '07_Mesh',
             '08_Result',
             '09_BeamSection',
             '11_FrontISTR', 
             '12_OpenRadioss', 
             '21_SU2', 
             '32_Palace']





def countFiles(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print('Number of files in', dir_path, ':', count)
    return count


sum = 0
for dir in dir_paths:
    sum += countFiles(dir)
print('Total number of files: ', sum)




