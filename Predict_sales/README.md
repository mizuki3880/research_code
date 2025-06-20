# 古着売上予測モデル - ファイル構成

## 推奨される新しい構成

```
Predict_sales/
├── README.md                    # このファイル
├── config/                      # 設定ファイル
│   ├── dictionaries/            # 辞書ファイル
│   │   ├── brands.txt
│   │   ├── categories.yaml
│   │   ├── materials.yaml
│   │   └── seasons/
│   │       ├── spring_summer.txt
│   │       ├── spring_autumn.txt
│   │       └── autumn_winter.txt
│   └── model_config.yaml        # モデル設定
├── data/                        # データファイル
│   ├── raw/                     # 生データ
│   │   ├── rakuten/
│   │   ├── yahoo/
│   │   └── google_trends/
│   ├── processed/               # 前処理済みデータ
│   │   ├── sales_data_merged.csv
│   │   ├── weather_data.csv
│   │   └── trends_data.csv
│   └── final/                   # 最終データセット
│       ├── training_data.csv
│       ├── validation_data.csv
│       └── test_data.csv
├── notebooks/                   # Jupyter notebooks
│   ├── 01_data_collection/      # データ収集
│   │   ├── rakuten_scraping.ipynb
│   │   ├── yahoo_scraping.ipynb
│   │   └── google_trends_download.ipynb
│   ├── 02_data_preprocessing/   # データ前処理
│   │   ├── data_cleaning.ipynb
│   │   ├── feature_engineering.ipynb
│   │   └── data_merging.ipynb
│   ├── 03_exploratory_analysis/ # 探索的分析
│   │   ├── sales_analysis.ipynb
│   │   ├── trend_analysis.ipynb
│   │   └── correlation_analysis.ipynb
│   ├── 04_modeling/            # モデリング
│   │   ├── baseline_model.ipynb
│   │   ├── advanced_model.ipynb
│   │   └── model_evaluation.ipynb
│   └── 05_forecasting/         # 予測
│       ├── sales_forecast.ipynb
│       └── trend_forecast.ipynb
├── src/                        # Pythonスクリプト
│   ├── __init__.py
│   ├── data/                   # データ処理モジュール
│   │   ├── __init__.py
│   │   ├── collectors.py       # データ収集
│   │   ├── preprocessors.py    # データ前処理
│   │   └── validators.py       # データ検証
│   ├── features/               # 特徴量エンジニアリング
│   │   ├── __init__.py
│   │   ├── extractors.py       # 特徴量抽出
│   │   └── transformers.py     # 特徴量変換
│   ├── models/                 # モデル
│   │   ├── __init__.py
│   │   ├── baseline.py         # ベースラインモデル
│   │   ├── advanced.py         # 高度なモデル
│   │   └── ensemble.py         # アンサンブル
│   ├── evaluation/             # 評価
│   │   ├── __init__.py
│   │   ├── metrics.py          # 評価指標
│   │   └── visualization.py    # 可視化
│   └── utils/                  # ユーティリティ
│       ├── __init__.py
│       ├── config.py           # 設定管理
│       └── helpers.py          # ヘルパー関数
├── tests/                      # テスト
│   ├── test_data_processing.py
│   ├── test_models.py
│   └── test_evaluation.py
├── results/                    # 結果
│   ├── models/                 # 保存されたモデル
│   ├── predictions/            # 予測結果
│   └── reports/                # レポート
└── requirements.txt            # 依存関係
```

## 移行手順

1. **バックアップ作成**
2. **新しいディレクトリ構造作成**
3. **ファイルの整理と移動**
4. **重複ファイルの削除**
5. **コードの統合とリファクタリング**

## メリット

- **明確な責任分離**: 各ディレクトリが明確な役割を持つ
- **再利用性向上**: モジュール化されたコード
- **保守性向上**: 整理された構造でメンテナンスが容易
- **拡張性**: 新しい機能の追加が簡単
- **テスト可能性**: 各モジュールのテストが可能
