# XDoG-OpenCV-Sample

カラー画像に対するヒストグラム平坦化のOpenCVサンプルです。<br>
画像をRGBからYUVに変換し、Y(輝度情報)のヒストグラム平坦化を実施することで、<br>カラー画像に対しヒストグラム平坦化を行っています。

<img src="https://user-images.githubusercontent.com/37477845/105632740-35778f80-5e98-11eb-839f-27bf13b5091c.png" width="40%"> <b>→</b> <img src="https://user-images.githubusercontent.com/37477845/105632746-390b1680-5e98-11eb-841e-daf68ee5ce06.png" width="40%">

# Requirement 
* OpenCV 3.4.2 or later

# Demo
サンプル画像でのデモの実行方法は以下です。
```bash
python color_equalize_hist.py
```

また、Webカメラを用いたデモの実行方法は以下です。
デモ実行時には、以下のオプションが指定可能です。
* --device<br>カメラデバイス番号の指定 (デフォルト：0)
* --width<br>カメラキャプチャ時の横幅 (デフォルト：960)
* --height<br>カメラキャプチャ時の縦幅 (デフォルト：540)
* --use_CLAHE<br>ヒストグラム平坦化にCLAHEを用いるか (デフォルト：未指定)<br>※コントラスト制限適応ヒストグラム平坦化(CLAHE, Contrast Limited Adaptive Histogram Equalization)
```bash
python sample.py
```

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
color-equalize-hist-sample is under [Apache-2.0 License](LICENSE).

また、サンプルの画像は[フリー素材ぱくたそ](https://www.pakutaso.com)様の写真を利用しています。
