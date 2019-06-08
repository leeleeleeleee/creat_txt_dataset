import os
#分三级目录，如A/B/a.jpg
#input为一级目录；
#
def creat_filelist(input_path):
#创建三级目录
    dir_image1 = [] #二级目录
    file_list = [] #三级目录
    for dir1 in os.listdir(input_path):
        dir_image1_temp = input_path + '/' + dir1 + '/'
        dir_image1.append(dir_image1_temp)
        for dir2 in os.listdir(dir_image1_temp):
            dir_image2_temp = dir_image1_temp + '/' + dir2
            file_list.append(dir_image2_temp)

    return file_list

def creat_txtfile(output_path, file_list):

    with open(output_path, 'w') as f:
        for list in file_list:
            print(list)
            f.write(list + '\n')

def main():
    dir_image0 = 'E:/A_DL/实习学习/Age and gender classification/aligned'
    file_list = creat_filelist(dir_image0)
    output_path = './creat_txt.txt'

    creat_txtfile(output_path, file_list)

if __name__ == '__main__':
    main()