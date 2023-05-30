# バグフィックスチャレンジ

`bug-fix-challenge`は、コードに含まれたバグを発見・修正することを目的にしています。制限時間は30分です。

## セットアップ

1. 以下のコマンドでリポジトリをクローンしてください。

```bash
git clone https://github.com/yuijiro473/bug-fix-challenge-sample
```

2. 以下の規則に従い、ブランチを作成してください。

   ブランチ名：`{ユーザー名}-bug-fix`

## 問題

1. `buggy_flight_booking.py`という名前のファイルにバグが存在します。このバグを見つけて修正してください。

2. 修正した内容は、`fixed_flight_booking.py`に保存します。このファイルは既にリポジトリに存在しています。

## テスト

1. `test_flight_booking.py`というファイルにはバグのあるコードに対するテストが含まれています。ローカルでテストを実行し、ターミナルに`課題クリア`の表示が出ることを確認してください。

```bash
python -m unittest test_flight_booking.py
```

## 提出

1. ターミナルに`課題クリア`が表示されたら、修正したファイルをリポジトリにプッシュします。
