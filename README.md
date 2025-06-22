# Django_PDFScanner
* document_upload PDFファイルのアップロード、ファイル管理、PDFからテキスト・表データの抽出
* financial_data 損益計算書や決算データのモデル定義、データベースへの保存と管理
* analysis データ分析、グラフ生成、可視化（PlotlyやMatplotlibなどによるインタラクティブ表示）
* users ユーザー管理・認証
* reports レポート生成、分析結果のダウンロードや共有機能
```
document_upload
PDFファイルのアップロード受け付け
PDFからテキストや表データの抽出（Adobe Extract APIやpdfminer.sixなど利用）
抽出したデータをfinancial_dataアプリへ渡す

financial_data
損益計算書、貸借対照表、キャッシュフロー計算書などのモデル定義
抽出データの正規化とデータベース保存
データの検索・取得機能

analysis
データの可視化（売上高・利益率・財務指標などのグラフ表示）
インタラクティブなグラフ（Plotlyなど）による分析

users
ユーザー登録・ログイン・権限管理

reports
分析結果のレポート生成（PDFやHTML出力）
レポートのダウンロード・メール送信
```
