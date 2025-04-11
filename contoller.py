import sys
import os
import shutil

import cv2
from PyQt5.QtWidgets import QApplication, QFileDialog

from rev_ui import Ui_Form
from model import Model

class Controller:
    def __init__(self, view, model):
        super().__init__()
        self.ui = view
        self.model = model
        self.render_image = False   # variabel agar tidak bisa load img ketika sudah ada img
        self.path_img_save = "img_tmp"
        self.setSylesheet()

    def setSylesheet(self):
        self.ui.btn_load.clicked.connect(lambda: self.load_image(0))
        self.ui.btn_clear.clicked.connect(lambda: self.clearImg())
        self.ui.btn_save.clicked.connect(lambda: self.save_img())
        self.ui.btn_crop.clicked.connect(lambda : self.load_image(1))

    def load_image(self, condition):
        if self.render_image:
            self.ui.message("Please clear images")
            return    # kalo true bakal kembali
        path_img = QFileDialog.getOpenFileName(filter="Image (*.png *.jpg *.apng *.avif *.gif *.jpeg *.svg *.tiff *.webp)")[0]
        # path_img = './img_crop_1_1.png'
        if path_img != '':
            self.render_image = True
            if condition == 0:
                self.kondisi_ui(0)
                self.show_to_ui_img_1(path_img)
            else:
                self.kondisi_ui(1)
                self.show_to_ui_img_crop(path_img)

    def kondisi_ui(self, condisi):
        if condisi == 0:
            self.ui.frame_19.hide()
            self.ui.frame_2.show()
        else:
            self.ui.frame_2.hide()
            self.ui.frame_19.show()

    def show_to_ui_img_1(self, path_img):
        # resolution = [400, 700, 900]
        # size = resolution[self.ui.comboBox.currentIndex()]

        morp = self.model.morp_opr(path_img)
        self.canny = self.model.labelling(morp)
        total_cells = self.model.count_wide_cell(morp)
        self.graph = self.model.graph()

        dst = "img_tmp"
        cv2.imwrite(f"{dst}/corner.png", self.canny)
        cv2.imwrite(f"{dst}/count.png", self.model.img_count)
        cv2.imwrite(f"{dst}/diameter.png", self.model.img_dimensions)
        cv2.imwrite(f"{dst}/graph.png", self.graph)

        self.ui.totalCell.setText(total_cells)
        self.ui.update_img(self.model.img_ori, self.ui.img_ori)
        self.ui.update_img(self.canny, self.ui.img_canny)
        self.ui.update_img(morp, self.ui.img_dist)
        self.ui.update_img(self.model.img_dimensions, self.ui.img_label)
        self.ui.update_img(self.model.img_count, self.ui.img_count)
        self.ui.update_img(self.graph, self.ui.img_grafik)


    def show_to_ui_img_crop(self, img_path):
        dir_img_save_path = f"{self.path_img_save}"
        # resolution = [660, 800, 1000]
        # size = resolution[self.ui.comboBox.currentIndex()]
        # self.checkDir(dir_img_save_path)

        img = self.model.crop_img(dir_img_save_path, img_path)
        self.ui.update_img(img, self.ui.img_crop)
        self.ui.message("The image is temporarily stored in the img folder \"img_tmp\"!!!")

    def save_img(self):
        import datetime

        if self.render_image == False:
            self.ui.message("There is no image to save, do something first!!!")
            return

        if not os.path.exists("img_tmp"):
            self.ui.message("Images are stored in \"img_save\" directory.")
        else:
            if not os.path.exists("img_save"):
                os.mkdir("img_save")

            file_name = datetime.datetime.now()
            file_name = file_name.strftime("%H-%M-%S_%d-%m-%Y")

            shutil.move("img_tmp", "img_save")
            os.rename("img_save/img_tmp", f"img_save/{file_name}")

            self.ui.message("Images are stored in \"img_save\" directory.")

    def clearImg(self):
        self.ui.img_ori.clear()
        self.ui.img_count.clear()
        self.ui.img_dist.clear()
        self.ui.img_label.clear()
        self.ui.img_grafik.clear()
        self.ui.img_canny.clear()
        self.ui.img_crop.clear()
        self.model.x_point, self.model.y_point = [], []
        self.ui.totalCell.setText(" Total Cell : ")
        self.render_image = False

        if (os.path.isdir(f"img_tmp")):
            os.system(f"rm -R img_tmp")

def main():
    app = QApplication(sys.argv)

    ui = Ui_Form()
    model = Model()
    Controller(ui, model)

    ui.setWindowTitle('Histologi')
    ui.resize(3500, 1600)
    # ui.resize(1080, 720)

    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
