## imports library
import pandas as pd
import streamlit as st
import altair as alt
import requests
from numerize import numerize

## setting page size
st.set_page_config(layout='wide')

## csv files
# file_uang = 'data\data_keuangan_202306101536.csv'
file_daily_visit = 'data\daily_visit_202306100001.csv'
file_monthly_visit = 'data\monthly_visit_202306101437.csv'
file_monthly_sale = 'data\pendapatan_tahun_bulan_202306101645.csv'


## setting to datasets
# df_uang = pd.read_csv(file_uang)
df_visit = pd.read_csv(file_daily_visit)
df_month_visit = pd.read_csv(file_monthly_visit)
df_month_sale = pd.read_csv(file_monthly_sale)

## change the text format to date
# df_uang['REG_DATE'] = pd.to_datetime(df_uang['REG_DATE'])
# df_uang['INV_DATE'] = pd.to_datetime(df_uang['INV_DATE'])


## setting current year and previous year
# CURR_YEAR = max(df_uang['REG_DATE'].dt.year)
# PREV_YEAR = CURR_YEAR - 1



st.title("DASHBOARD - Helix Lab & Klinik Cabang Kartini")
st.write("Catatan sejak 2021-05-01 hingga 2023-06-01")

mx_total_kunjungan, mx_max_kunjungan, mx_test= st.columns(3)

with mx_total_kunjungan:
    sum_kunjungan = df_visit['daily_visit'].sum()
    st.metric(label='Total Kunjungan', value=sum_kunjungan)

with mx_max_kunjungan:
    max_visit_row = df_month_visit.loc[df_month_visit['monthly_visit'].idxmax()]
    
    year_month = max_visit_row['year_month_visit']
    monthly_visits = int(max_visit_row['monthly_visit'])
    
    st.metric(label="Kunjungan terbanyak terdapat pada", value=year_month, delta=monthly_visits)

with mx_test:
    max_sale_row = df_month_sale.loc[df_month_sale['jumlah_pembelian'].idxmax()]
    
    year_month_sale = max_sale_row['LIST_TEST']
    monthly_sale = int(max_sale_row['jumlah_pembelian'])
    
    st.metric(label="Pemeriksaan terbanyak di bulan tersebut", value=year_month_sale, delta=monthly_sale)

mx_grafik_kunjungan, mx_komparasi= st.columns([2,1])

with mx_grafik_kunjungan:
    st.subheader('Jumlah Kunjungan per Tahun-Bulan')
    
    grafik_kunjungan_garis = alt.Chart(df_month_visit).mark_line().encode(
    x=alt.X("year_month_visit", title='Tahun dan Bulan Kunjungan'),
    y=alt.Y("monthly_visit", title='Jumlah Pengunjung'),
    ).properties(width=900).interactive()
    
    grafik_kunjungan_titik = alt.Chart(df_month_visit).mark_point().encode(
    x=alt.X("year_month_visit", title='Tahun dan Bulan'),
    y=alt.Y("monthly_visit", title='Jumlah Pengunjung'),
    ).properties(width=900).interactive()

    grafik_kunjungan = grafik_kunjungan_garis + grafik_kunjungan_titik
    grafik_kunjungan

with mx_komparasi:
     # Menghitung total kunjungan dari 2021-05 hingga 2022-05
    total_visit_before = df_month_visit[(df_month_visit['year_month_visit'] >= '2021-05') & (df_month_visit['year_month_visit'] <= '2022-05')]['monthly_visit'].sum()

    # Menghitung total kunjungan dari 2022-06 hingga 2023-06
    total_visit_after = df_month_visit[(df_month_visit['year_month_visit'] >= '2022-06') & (df_month_visit['year_month_visit'] <= '2023-06')]['monthly_visit'].sum()

    # Calculate the delta (difference)
    delta_kunjungan_tahun = int(total_visit_after) - int(total_visit_before)

    # Menampilkan hasil menggunakan metric widget
    st.metric(label='Total kunjungan hingga Juni 2022', value=total_visit_before)
    st.metric(label='Total kunjungan hingga Juni 2023', value=total_visit_after, delta=delta_kunjungan_tahun)

    st.write(
        '''
        Oleh karena Helix Lab & Klinik lebih dikenal karena pelayanan PCR dan Antigen Covid-19,
        ketika di tahun 2022-2023 terjadi penurunan jumlah kasus baru, maka ikut menurun pula jumlah kunjungan.\n
        Strategi yang diupayakan Helix kemudian adalah menawarkan promo Medical Check-Up agar Helix lebih dikenal.
        '''
    )

## showing the dataset
st.subheader('Dataset Pendapatan')
df_month_sale
# st.subheader('Dataset Pembayaran')
# df_uang



## changelog
st.subheader('Changelogs')

st.write('ver 0.1 (2023/06/10) --> first time uploading to github repositories')