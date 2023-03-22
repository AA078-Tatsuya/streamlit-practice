import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image


st.title('ソフトブレーン株式会社 課題')

st.write('Interravtive Widgets')

# タイムバーを表示させる
'start!!'
latest_iterarion = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iterarion.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)
'done!!'

# カラムを2つに分割し、表示する
left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# 問い合わせをクリックすると回答がプルダウン表示される
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

text = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

# 画像を表示する
st.write('Display Image')

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)

'あなたの好きな数字は、', option,'です。'

# チェックボックスを入れると画像を表示するためのif文
if st.checkbox('Show Image'):
    img = Image.open('galaxy-sample.jpg')
    st.image(img, caption='Galaxy', use_column_width=True)

# データフレームを表示する
st.write('DataFrame')
# 20行3列の乱数行列を作成
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
# 行列のデータからチャートを作成
st.map(df)

# 各列の一番大きい値をハイライト表示する　st.dataframe(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```Python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

