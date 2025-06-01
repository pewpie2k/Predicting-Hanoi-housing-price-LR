import tkinter as tk
from tkinter import ttk
from tkinter import *

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# Load dữ liệu từ file CSV
def load_data(filename):
    data = pd.read_csv('VN_housing_dataset_vecto_final.csv')
    return data


# Xây dựng mô hình Linear Regression
def build_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, X_test, y_test


# Tính toán dự đoán và hiển thị kết quả
def predict_price(model, X_test, y_test, input_features):
    features = np.array(input_features).reshape(1, -1)
    predicted_price = model.predict(features)[0]
    true_price = y_test.iloc[0]
    return predicted_price, true_price

quan_mapping = {
    'Quận Ba Đình':1,
    'Quận Hoàn Kiếm':2,
    'Quận Tây Hồ':3,
    'Quận Long Biên':4,
    'Quận Cầu Giấy':5,
    'Quận Đống Đa':6,
    'Quận Hai Bà Trưng':7,
    'Quận Hoàng Mai':8,
    'Quận Thanh Xuân':9,
    'Quận Hà Đông':10,
    'Quận Bắc Từ Liêm':11,
    'Quận Nam Từ Liêm':12,
    'Thị xã Sơn Tây':13,
    'Huyện Ba Vì':14,
    'Huyện Chương Mỹ':15,
    'Huyện Đạn Phượng':16,
    'Huyện Đông Anh':17,
    'Huyện Gia Lâm':18,
    'Huyện Hoài Đức':19,
    'Huyện Mê Linh':20,
    'Huyện Mỹ Đức':21,
    'Huyện Phú Xuyên':22,
    'Huyện Phúc Thọ':23,
    'Huyện Quốc Oai':24,
    'Huyện Sóc Sơn':25,
    'Huyện Thạch Thất':26,
    'Huyện Thanh Oai':27,
    'Huyện Thanh Trì':28,
    'Huyện Thường Tín':29
}
loaihinh_mapping = {
    'Nhà biệt thự': 1,
    'Nhà mặt phố, mặt tiền': 2,
    'Nhà ngõ, hẻm': 3,
    'Nhà phố liền kề': 4,
    'Không rõ': 5,
}
giayto_mapping = {
    'Đã có sổ': 1,
    'Đang chờ sổ': 2,
    'Giấy tờ khác': 3,
    'Không rõ': 4,
}


# Giao diện ứng dụng

def create_gui():
    def predict():
        try:
            input_features = [int(quan_mapping[f1_combobox.get()]), int(loaihinh_mapping[f2_combobox.get()]), int(giayto_mapping[f3_combobox.get()]), float(f4_entry.get()), float(f5_entry.get()), float(f6_entry.get()), float(f7_entry.get()), float(f8_entry.get()), float(f9_entry.get())]
            predicted_price, true_price = predict_price(model, X_test, y_test, input_features)
            result_label.config(text=f"Giá dự đoán: {predicted_price*1000000:.2f}VND\nGiá thực tế: {true_price*1000000}VND")
        except ValueError:
            result_label.config(text="Vui lòng nhập các giá trị hợp lệ.")

    # Load dữ liệu
    data = load_data('VN_housing_dataset_vecto_final.csv')
    X = data[['f1','f2','f3','f4','f5','f6','f7','f8','f9']]
    y = data['f10']

    # Xây dựng mô hình
    model, X_test, y_test = build_model(X, y)

    # Tạo giao diện đồ họa
    window = tk.Tk()
    window.title("Dự đoán giá nhà đất")
    window.geometry('300x700')

    # scroll_bar = tk.Scrollbar(window)
    # scroll_bar = Scrollbar(window)

    f1_label = ttk.Label(window, text="Quận:")
    f1_label.pack(pady=5)
    f1_combobox = ttk.Combobox(window, values=list(quan_mapping.keys()))
    f1_combobox.pack(pady=5)

    f2_label = ttk.Label(window, text="Loại hình nhà ở:")
    f2_label.pack(pady=5)
    f2_combobox = ttk.Combobox(window, values=list(loaihinh_mapping.keys()))
    f2_combobox.pack(pady=5)

    f3_label = ttk.Label(window, text="Giấy tờ pháp lý:")
    f3_label.pack(pady=5)
    f3_combobox = ttk.Combobox(window, values=list(giayto_mapping.keys()))
    f3_combobox.pack(pady=5)

    f4_label = ttk.Label(window, text="Số tầng:")
    f4_label.pack(pady=5)
    f4_entry = ttk.Entry(window)
    f4_entry.pack(pady=5)

    f5_label = ttk.Label(window, text="Số phòng khách:")
    f5_label.pack(pady=5)
    f5_entry = ttk.Entry(window)
    f5_entry.pack(pady=5)

    f6_label = ttk.Label(window, text="Nhà để xe oto:")
    f6_label.pack(pady=5)
    f6_entry = ttk.Entry(window)
    f6_entry.pack(pady=5)

    f7_label = ttk.Label(window, text="Số phòng wc:")
    f7_label.pack(pady=5)
    f7_entry = ttk.Entry(window)
    f7_entry.pack(pady=5)

    f8_label = ttk.Label(window, text="Số phòng ngủ:")
    f8_label.pack(pady=5)
    f8_entry = ttk.Entry(window)
    f8_entry.pack(pady=5)

    f9_label = ttk.Label(window, text="Diện tích:")
    f9_label.pack(pady=5)
    f9_entry = ttk.Entry(window)
    f9_entry.pack(pady=5)

    predict_button = ttk.Button(window, text="Dự đoán giá", command=predict)
    predict_button.pack(pady=10)

    result_label = ttk.Label(window, text="")
    result_label.pack(pady=10)

    window.mainloop()


# Chạy ứng dụng
if __name__ == "__main__":
    create_gui()
