####################################################
#
#   RegSum レジサム
#
#
######################################################

# --- モジュールのインポート -------------------------- #
import streamlit as st
import pandas as pd

# --- アプリのタイトル -------------------------------- #
st.title('合計金額を表示します')

# --- 合計金額表示用 ---------------------------------- #
# フォームの外で合計金額とデータフレームを表示するためのプレースホルダーを作成
results_placeholder = st.empty()

# --- 商品情報 ---------------------------------------- #
# ユーザーが入力する商品の最大数
max_items = 10

# ユーザーの入力を格納するためのリスト
data = []

with st.form("my_form"):
    # 商品名と金額の入力フィールドを動的に作成
    for i in range(max_items):
        # 前の商品名と金額が入力されているかチェック
        if i == 0 or (data[i-1][0] and data[i-1][1] > 0):
            col1, col2 = st.columns(2)
            with col1:
                # 商品名の入力
                item_name = st.text_input(f"商品名 {i+1}", key=f"name{i}")
            with col2:
                # 金額の入力
                item_price = st.number_input(f"金額 {i+1}", min_value=0.0, format='%f', key=f"price{i}")
            # 入力をリストに追加
            data.append([item_name, item_price])
        else:
            # 前の商品の情報がまだない場合はループを中断
            break
    
    # 送信ボタン
    submitted = st.form_submit_button('合計を計算')


# --- 合計を算出ボタンを押した後の処理 ----------------------------------- #

if submitted:
    # データフレームの作成
    df = pd.DataFrame(data, columns=['商品名', '金額'])

    # 合計金額の計算
    total_price = int(df['金額'].sum())

    # 結果をプレースホルダーに表示
    st.write(df)  # 入力された商品情報を表示
    results_placeholder.write(f'合計金額: {total_price} 円')  # 合計金額を表示