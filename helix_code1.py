import pandas as pd
import streamlit as st
import altair as alt
import requests


st.set_page_config(
    page_title = 'Mari belajar Streamlit',
    layout='wide'
)

st.title("Performa Helix Lab ")
## tab pada tulisan di bawah membuat box text
st.write('''Deskripsi:\n
    Helix Lab merupakan Klinik dan Laboratorium yang dimiliki oleh\n
    PT Heksa Lingkar Diagnostik.\n
    PT ini
    ''')
st.write('''
    Kasus Covid-19 di Indonesia di tahun 2021 hingga 2022 mengalami peningkatan,
    hal ini dapat dilihat pada berita
    \n\n
    kalo begini enter
''')
st.header("Cabang : Kartini Depok")
st.write('''Ditinjau dari 2021 hingga 2023, input data dimulai sejak bulan Mei
             karena selesai mendaftar ke aplikasi LIS,
             padahal operasional klinik sudah berjalan sejak januari 2021''')


file_dv = 'data\daily_visit_202306100001.csv'
file_mv = 'data\monthly_visit_202306101437.csv'

dfdv = pd.read_csv(file_dv)

## change the text format to date
dfdv['REG_DATE'] = pd.to_datetime(dfdv['REG_DATE'])

## setting current year and previous year
CURR_YEAR = max(dfdv['REG_DATE'].dt.year)
PREV_YEAR = CURR_YEAR - 1

st.write(dfdv.head())

chart_daily = alt.Chart(dfdv).mark_line().encode(
    x="REG_DATE",
    y="daily_visit",
).properties(width=1200)

chart_daily

dfmv = pd.read_csv(file_mv)

st.write(dfmv.head())

chart_monthly = alt.Chart(dfmv).mark_line().encode(
    x=alt.X("year_month_visit", title='Tahun dan Bulan Kunjungan'),
    y=alt.Y("monthly_visit", title='Jumlah Pengunjung'),
).properties(width=800)

chart_monthly

## making columns
mx_visits, mx_order, mx_customer, mx_gpm = st.columns(4)

with mx_visits:

    curr_visits = dfdv.loc[dfdv['REG_DATE']==CURR_YEAR, 'daily_visit'].values[0]
    prev_visits = dfdv.loc[dfdv['REG_DATE']==PREV_YEAR, 'daily_visit'].values[0]
    
    visit_diff_pct = 100.0 * (curr_visits - prev_visits) / prev_visits

    st.metric("Visit", value=numerize.numerize(curr_visits), delta=f'{visit_diff_pct:.2f}%')

# with mx_order:
#     st.metric("Number of Order", value=100, delta=10)




## Menggambarkan TOTAL SELURUH kunjungan dari 2021 ke 2023
#### --> digambarkan setiap bulan / hari
#### --> perbandingan antara 2021->2022 dengan 2022->2023
#### --> seberapa sering seorang pasien datang (sudah berapa kali datang) trivia : dapat souvenir dari helix

## menggambarkan bulan-tahun kunjungan terbanyak dari 2 tahun
#### --> kapan layanan tertinggi terjadi ---> kaitkan dengan berita covid / PSBB
#### --> jumlah hasil positif covid
#### --> rasio pasien positif negatif covid 

## menggambarkan layanan apa saja yang paling diminati
#### --> ranking layanan apa saja
#### --> rasio layanan terhadap keseluruhan

## --> Harga layanan yang paling diminati termahal dan termurah --> harga antigen covid 
#### --> jenis pembayaran yang sering digunakan
#### --> jenis PAKET/PROMO pembayaran 
###### 2021 ke 2022 ada perubahan harga, dicek Pay nya beda antara jenis layanan
###### ada CTO 1 2021 beda harga sama CTO 1 2022, CTO 1 2023

#### --> perbandingan pemasukan antara layanan terbanyak dibanding dengan layanan di
####      kelas harga 500 rb, 1 jt, 1.5 jt, 2 jt
#### --> Perubahan harga per bulan, per tahun? --> ambil antigen saja, pcr saja, tidak dengan tes lain




"\n"









# Menulis teks di streamlit

st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

st.write("Hello world!")

st.markdown("## ini ditulis menggunakan _markdown_")

"Hello world!" # <- magic

"_Ini juga hello world_"

"**Ini juga**"

"# Ini adalah header"

"## ini adalah subheader"


st.header("Ini juga header")

st.caption("Langit senja minum kopi")

st.code("import streamlit as st")

st.code('''
import pandas as pd
import streamlit as st # ini untuk memanggil package streamlit
''')
