# 貨櫃號碼的偵測與辨識
## 背景
本專案從頭開始訓練YOLOv4，並建置一套貨櫃車編號偵測流程，其中YOLOv4使用了許多大型模型以及遷移學習的訓練技巧，如：Mosaic資料增強法、凍結訓練、單循環餘弦衰減策略等等，在YOLOv4取得物件位置後，本專案針對該位置圖片進行前處理後再使用OCR偵測該區文字，最後進行後處理調整即可得到所需之編號。專案使用bubbliiiing在Github上提供的Keras版本YOLOv4作為基底，再根據YOLOv4的論文做適當修改。  
## 環境需求
tensorflow-gpu==1.13.1  
keras==2.2.4  
pillow==8.4.0  
opencv==4.4.0  
numpy==1.19.5  
pytesseract==0.3.10
## 系統摘要
專案大致可分為兩個部分，分別為YOLO偵測編號的位置與OCR辨識貨櫃編號，因此本專案將先訓練YOLO模型，再使用偵測的結果去進行OCR辨識。根據官方文件所述，YOLOv4的預訓練權重為通用權重，可以有效避免訓練時間過長的問題，因此本專案將基於YOLOv4的通用預訓練權重接著做訓練，整個訓練流程如下圖所示。  
![GITHUB](https://i.imgur.com/4WP6taM.png)  
訓練並評估完成後，即可使用YOLOv4的偵測功能抓取貨櫃上編號的位置並使用OCR辨識貨櫃編號，本專案使用現成OCR套件做辨識，雖然有重新訓練OCR這一做法，但此方法相對耗時許多，故選擇使用此一較為快速的作法，但仍須針對OCR的辨識做前處理以及後處理，流程如下圖。  
![GITHUB](https://i.imgur.com/DVqZnim.png)  
## 流程
詳細的訓練流程可參考「背景」章節之參考連結，此處概述本專案的訓練流程。
### 1.資料集準備
本文使用VOC格式進行訓練，使用課程所提供之貨櫃編號影像組合成資料集，資料在進行完標註後擺放於根目錄之Data資料夾中，資料夾內容如下所示。  
```
├── Data  
│   ├── train 
│   │   ├── train_img
│   │   │   ├── 1.jpg  
│   │   │   ├── 2.jpg  
│   │   │   ├── 3.jpg   
│   │   │   ├── ...  
│   │   ├── train_xml
│   │   │   ├── 1.xml 
│   │   │   ├── 2.xml  
│   │   │   ├── 3.xml  
│   │   │   ├── ...  
│   │   ├── Main 
│   │   ├── list 
│   ├── test
│   │   ├── test_img
│   │   │   ├── 1.jpg  
│   │   │   ├── 2.jpg  
│   │   │   ├── 3.jpg   
│   │   │   ├── ...  
│   │   ├── test_xml
│   │   │   ├── 1.xml 
│   │   │   ├── 2.xml  
│   │   │   ├── 3.xml  
│   │   │   ├── ...
```
### 2.資料集處理
在完成資料集的擺放之後，需要執行voc_annotation.py獲得訓練用的train.txt和val.txt檔案。此外，cls_classes.txt檔案內容包含了所需預測類別，本專案已修改為僅有ContainerNum一項類別。
完成後便可執行voc_annotation.py。
```python
python voc_annotation.py
```
### 3.開始訓練
本專案將訓練流程修改為Python的Jupyter Notebook形式(ipynb檔)，方便了解各個區塊的執行工作及結果，細部程式碼功用以註解進行標註。
```
train.ipynb
```
執行train.ipynb開始訓練，在訓練多個epoch後權重檔會產生在logs資料夾中。
### 4.OCR處理及預測
OCR預測流程同樣為Python的Jupyter Notebook形式(ipynb檔)，細部程式碼功用以註解進行標註。
```
predict.ipynb
```
## 參考結果
![GITHUB](https://i.imgur.com/Izemoyq.png)
## 來源
https://github.com/bubbliiiing/yolov4-keras
