from os.path import split

import cv2, os
import numpy as np
import matplotlib.pyplot as plt

class Model:
    def __init__(self):
        self.img_dimensions, self.img_count, self.img_ori = None, None, None
        self.x_point, self.y_point = [],[]
        self.path_img_save = "img_tmp"

    def morp_opr(self, path):
        img = cv2.imread(path)
        self.img_dimensions, self.img_count, self.img_ori = img.copy(), img.copy(), img.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        img_mop = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (50, 50)))
        img_mop = cv2.morphologyEx(img_mop, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1)))

        # switch objek detection
        img_morp = img_mop.copy()
        for i in range(0, img_morp.shape[0]):
            for j in range(0, img_morp.shape[1]):
                px = 255 if img_morp[i][j] == 0 else 0
                img_morp[i][j] = px

        # konvert ke BGR agar gambar morphologi memiliki channel(warna)
        img_morp = cv2.cvtColor(img_morp, cv2.COLOR_GRAY2BGR)

        return  img_morp

    def labelling(self, switch_obj):
        # canny digunakan untuk deteksi garis luar sel
        canny = cv2.Canny(switch_obj, 100, 200)

        # deteksi sel
        kontur1, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # gambar garis luar sel ke dalam gambar original
        cv2.drawContours(self.img_count, kontur1, -1, (0, 255, 0), 5)
        cv2.drawContours(self.img_dimensions, kontur1, -1, (0, 255, 0), 5)
        return cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

    def count_wide_cell(self, morph):
        # img_switch = cv2.imread(f"{self.path_img_save}/img_processing/switch-obj.png")
        gray = cv2.cvtColor(morph, cv2.COLOR_BGR2GRAY)
        threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # membuat matriks 3 x 3 dengan tipe uint8
        kernel = np.ones((3, 3), np.uint8)

        mop_open = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel, iterations=2)

        # dilate = cv2.dilate(mop_open, kernel, iterations=2)
        # deteksi diameter sel dgn cara memperkecil sel tsb
        distance_trans = cv2.distanceTransform(mop_open, cv2.DIST_L2, cv2.DIST_MASK_5)
        dist_thres = cv2.threshold(distance_trans, 0.24 * distance_trans.max(), 255, cv2.THRESH_BINARY)[1]

        img_gray = cv2.convertScaleAbs(dist_thres)   # konvert dari gambar CV_32FC1 (32 bit float, satu channel) ke CV_8UC1 (img grayscale atau biner dgn 8 bit per channel)
        kontur2, _ = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # mc = 264.5833  # 1 px = 264.5833 micrometer
        mm = 0.264  # 1 px = 0.2645833333 milimeter

        # total sel
        total_cell = f" Total Cell : {len(kontur2)} "
        # loop untuk menghitung diameter & nomor sel
        for i in range(0, len(kontur2)):
            ((x, y), r) = cv2.minEnclosingCircle(kontur2[i])
            diameter = cv2.contourArea(kontur2[i], False)
            if diameter == 0: continue
            # cv2.putText(self.image_original, f"{int(wide)}px", (int(x) - 4, int(y)), cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 0, 255), 1)
            cv2.putText(self.img_count, f"{int(i + 1)}", (int(x) - 15, int(y)), cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 0, 255), 1)
            cv2.putText(self.img_dimensions, "{:.2f}mm".format(diameter * mm), (int(x) - 15, int(y)), cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 0, 255), 1)
            self.x_point.append(int(i + 1))
            self.y_point.append(int(diameter * mm))
        return total_cell

    def crop_img(self, dir_path, img_path):
        # jumlah potongan gambar
        jmh_crop = 4

        # gambar yg sudah di labeling
        img = cv2.imread(img_path)
        height, width = img.shape[:2]

        # menghitung ukuran gambar untuk dipotong
        row_start, row_end = self.count_crop_img(jmh_crop, height)
        col_start, col_end = self.count_crop_img(jmh_crop, width)

        # img_save_path = f"{dir_path}/count_cell.png"

        self.checkDir(dir_path)

        for i in range(0, jmh_crop):
            for j in range(0, jmh_crop):
                # memotong gambar
                cropped = img[row_start[i]:row_end[i], col_start[j]:col_end[j]]

                # menyimpan gambar
                cv2.imwrite(f"{dir_path}/img_crop_{i + 1}_{j + 1}.png", cropped)

        return img

    def checkDir(self, path_dir):
        paths_disr = path_dir.split('/')
        dirs = ""
        for path in paths_disr:
            dirs += f"{path}/"
            if (os.path.exists(f"{dirs}")):
                if (os.path.isdir(f"{dirs}")):
                    os.system(f"rm -R {dirs}")
                    os.mkdir(f"{dirs}")
            else:
                os.mkdir(f"{dirs}")

    def count_crop_img(self, jmh_crop, size_img):
        # menghitung dimensi gambar yg akan dipotong sesuai kebutuhan
        start_crop = []
        end_crop = []

        # perhitungan ukuran potongan gambar
        size_crop = int(size_img / jmh_crop)
        for i in range(0, jmh_crop + 1):
            # fungsi append untuk menambahkan nilai list
            end_crop.append(i * size_crop)
            start_crop.append(end_crop[i] - size_crop)

        # fungsi pop untuk menhapus list index 0
        start_crop.pop(0)
        end_crop.pop(0)
        return start_crop, end_crop

    def graph(self):    # untuk grafik
        # self.checkDir(f"{self.path_img_save}")
        self.checkDir(f"{self.path_img_save}")

        plt.plot(self.x_point, self.y_point)
        plt.xlabel("Total Cells")
        plt.ylabel("Width Cells")

        plt.savefig(f"{self.path_img_save}/graph.png")

        img_graph = cv2.imread(f"{self.path_img_save}/graph.png")
        img_graph = cv2.cvtColor(img_graph, cv2.COLOR_BGR2RGB)
        plt.close('all')

        return img_graph