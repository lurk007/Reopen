# -*-coding:utf-8-*-
import itertools
import sys
import time
import zipfile


class ZipBlast(object):
    def __init__(self):
        self.filepath = "target_file/1.zip"
        self.uncompress_path = "success_file"
        # 密码位数(Number of password digits)
        self.pwd_digits_list = [4]
        # 暴力破解全排列的字典(Violent cracking of fully arranged dictionaries)
        # self.pwd_dic = "abcdefghijklmnopqrstuvwxyz"
        # self.pwd_dic = "abcdefghijklmnopqrstuvwxyz0123456789"
        # self.pwd_dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # self.pwd_dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        # self.pwd_dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+-=<>."
        self.pwd_dic = "0123456789"

    def uncompress(cls, filepath, password):
        try:
            with zipfile.ZipFile(filepath) as zFile:
                zFile.extractall(cls.uncompress_path, pwd=password.encode("utf-8"))
            return True
        except:
            return False

    def run(cls):
        count = 0
        start_time = time.time()
        for pwd_num in cls.pwd_digits_list:
            for c in itertools.product(cls.pwd_dic, repeat=pwd_num):
                count += 1
                password = "".join(c)
                if count % 10000 == 0:
                    print("已尝试破解", count, "次")
                    print("Attempted to crack ", count, " times")
                result = cls.uncompress(cls.filepath, password)
                if result:
                    print("用时：", (time.time() - start_time), "秒")
                    print((time.time() - start_time), "seconds")
                    print("一共尝试了", count, "次")
                    print("tried a total of ", count, " times")

                    print("解压成功，", cls.filepath, "密码是：", password)
                    print("Successfully decompressed! password of ", cls.filepath, " is: ", password)
                    sys.exit(1)


if __name__ == '__main__':
    obj = ZipBlast()
    obj.run()
