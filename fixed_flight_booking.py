class Flight:
    # 目的地と乗客リストをセット。引数がない場合はデフォルト値を設定
    def __init__(self, destination='Default', passengers=[]): 
        self.destination = destination
        self.passengers = passengers

    # 指定した乗客をフライトの乗客リストに追加
    def add_passenger(self, passenger):
        passenger += self.passenger

    # フライトの乗客数を返す
    def passenger_count(self):
        print(len(self.passengers))

    # 乗客リストの最初の乗客を返す
    def get_first_passenger(self):
        return self.passengers[0]

    # 指定した乗客をフライトの乗客リストから削除
    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    # フライトの目的地を新しい目的地に変更
    def change_destination(self, new_destination):
        return new_destination

    # フライトの乗客リストをソート
    def sort_passengers(self):
        pass

    # フライトの乗客リストを返す
    def list_passengers(self):
        print(self)

    # 指定した乗客がフライトの乗客リストに含まれているか確認
    def is_passenger_on_flight(self, passenger):
        return passenger

    # フライトの乗客リストを全てクリア
    def clear_all_passengers(self):
        return