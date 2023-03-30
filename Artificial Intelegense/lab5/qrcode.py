import os.path
import random

import segno
import io

#  макс длина при минимальном весе это 9 знаков
#random.seed(42)
# с сохранением в файл
test_str = "afafafafa"


qrcode = segno.make(test_str)
qrcode.save("qr.png")
qrcode.save("qr.txt")
size = os.path.getsize("qr.txt")
print(size, len(test_str))
# вывод массива "пикселей" через plt # рекомендуется пользоваться массивами numpy
import matplotlib.pyplot as plt

plt.imshow([[1, 2, 4, 3], [5, 4, 6, 3]])


