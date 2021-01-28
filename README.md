# XDoG-OpenCV-Sample
XDoG(Extended Difference of Gaussians)アルゴリズムを用いた線画抽出のサンプルです。

<img src="https://user-images.githubusercontent.com/37477845/106139516-e17aec80-61b0-11eb-96bd-d8bb3c66f2e9.png" width="40%"> <b>→</b> <img src="https://user-images.githubusercontent.com/37477845/106139534-e6d83700-61b0-11eb-8eae-8f0ae72d0fb7.png" width="40%">

# Requirement 
* OpenCV 3.4.2 or later

# Demo
サンプル画像でのデモの実行方法は以下です。
```bash
python XDoG.py
```

# Demo(Web Camera & GUI)
また、Webカメラを用いたデモの実行方法は以下です。<br>
デモ実行時には、以下のオプションが指定可能です。<br>
XDoGのパラメータは各トラックバーを変更することで調整可能です。
* --device<br>カメラデバイス番号の指定 (デフォルト：0)
* --width<br>カメラキャプチャ時の横幅 (デフォルト：960)
* --height<br>カメラキャプチャ時の縦幅 (デフォルト：540)
```bash
python sample.py
```
<img src="https://user-images.githubusercontent.com/37477845/106143007-87305a80-61b5-11eb-9366-5a97fb34b461.gif" width="80%">

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
color-equalize-hist-sample is under [MIT License](LICENSE).
[Dovyski/cvui](https://github.com/Dovyski/cvui) is under [MIT License](LICENSE).

また、サンプルの画像は[フリー素材ぱくたそ](https://www.pakutaso.com)様の写真を利用しています。
