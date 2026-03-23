# sampling-alias-demo

サンプリングとエイリアシングを直感的に学ぶための、Streamlit製ミニデモです。

## できること
- 信号周波数 `f_signal` を変更
- サンプリング周波数 `fs` を変更
- 元の波形とサンプル点を比較
- エイリアシング時の見かけの周波数を確認

## 実行方法

### 1. 仮想環境を有効化
```powershell
.\.venv\Scripts\Activate.ps1
```
### 2. ライブラリをインストール
```powershell
pip install -r requirements.txt
```
### 3. アプリを起動
```powershell
streamlit run app.py
```
## 学べること
- サンプリング周波数とナイキスト周波数の関係
- なぜ高い周波数が低い周波数に見えるのか
- エイリアシングの直感的なイメージ