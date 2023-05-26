# バグフィックス対決へようこそ！

この対決はあなたのコーディングスキルとデバッグ能力を試すためのものです。

## セットアップ

1. まずはこのリポジトリを自分のGitHubアカウントにフォークしてください。以下のコマンドを使用することができます：

```bash
git clone https://github.com/yuijiro473/bug-fix-challenge-sample
```

## チャレンジの開始

1. `buggy_flight_booking.py`という名前のファイルにバグが存在します。このバグを見つけて修正してください。

2. バグを修正したら、それを`fixed_flight_booking.py`として保存します。このファイルは既にリポジトリに存在します。

```bash
cp buggy_flight_booking.py fixed_flight_booking.py
```

## テスト

1. `test_flight_booking.py`というファイルにはバグのあるコードに対するテストが含まれています。ローカルマシンでこれらのテストを実行し、ターミナルに`OK`の表示が出ることを確認してください。

```bash
python -m unittest test_flight_booking.py
```

## 提出

1. ターミナルに`OK`が表示されたら、修正したファイルを自分のGitHubリポジトリにプッシュします。

```bash
git add fixed_flight_booking.py
git commit -m "Final fix"
git push
```

## 自動テスト

1. プッシュした後、GitHub Actionsが自動的に単体テストを実行します。全てのテストがパスすれば、バグフィックスは成功とみなされます。テストに失敗した場合は、失敗したテストから何が問題だったかを調査し、再度修正を行ってください。