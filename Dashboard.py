import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
hour_data_df = pd.read_csv("https://raw.githubusercontent.com/maliqueaa/AnalisisDataAQI/main/dataframe.csv")

# Preprocess data
Date_columns = ["Date"]
hour_data_df.sort_values(by="Date", inplace=True)
hour_data_df.reset_index(inplace=True)

for column in Date_columns:
    hour_data_df[column] = pd.to_datetime(hour_data_df[column])

min_Date = hour_data_df["Date"].min()
max_Date = hour_data_df["Date"].max()

# Streamlit app
st.set_option('deprecation.showPyplotGlobalUse', False)

with st.sidebar:
    st.header("Selamat Datang!")
    st.image("https://raw.githubusercontent.com/maliqueaa/AnalisisDataAQI/main/awan.jpg")
    
    start_Date, end_Date = st.date_input(
        label='Rentang Waktu', min_value=min_Date,
        max_value=max_Date,
        value=[min_Date, max_Date]
    )

main_df = hour_data_df[(hour_data_df["Date"] >= str(start_Date)) & 
                        (hour_data_df["Date"] <= str(end_Date))]

st.title("Visualisasi Kualiatas Angin💨")

st.text("")
st.text("")
st.text("")

st.header("Kualitas Angin Terbersih :sparkles:")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Huairou")
with col2:
    st.subheader("2017")

st.text("")
st.text("")

st.header("Kualitas Angin Terkotor ♨️")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Wanliu")
with col2:
    st.subheader("2014")

st.text("")
st.text("")
st.text("")

st.subheader("Visualisasi kualitas angin berdasarkan tempat")

st.text("Informasi yang bisa kita ambil dari chart diatas sebagai berikut :")

st.text("- kategori Baik terbanyak: Dingling dengan total 27.065.")

st.text("- Kategori Sedang terbanyak: Gucheng dengan total 14.355.")

st.text("- Kategori Buruk terbanyak: Nongzhanguan dengan total 1.072.")

data_stasiun = {
    'station': ['Aotizhongxin', 'Aotizhongxin', 'Aotizhongxin', 'Changping', 'Changping', 'Changping', 
                'Dingling', 'Dingling', 'Dingling', 'Dongsi', 'Dongsi', 'Dongsi', 
                'Guanyuan', 'Guanyuan', 'Guanyuan', 'Gucheng', 'Gucheng', 'Gucheng', 
                'Huairou', 'Huairou', 'Huairou', 'Nongzhanguan', 'Nongzhanguan', 'Nongzhanguan', 
                'Shunyi', 'Shunyi', 'Shunyi', 'Tiantan', 'Tiantan', 'Tiantan', 
                'Wanliu', 'Wanliu', 'Wanliu', 'Wanshouxigong', 'Wanshouxigong', 'Wanshouxigong'],
    'kualitas_udara': ['Baik', 'Sedang', 'Buruk'] * 12,
    'count': [20932, 13255, 790, 23770, 10700, 443, 27065, 7668, 180, 20630, 13664, 686, 
              20525, 13600, 852, 19806, 14355, 737, 25213, 9322, 219, 20140, 13768, 1072, 
              23103, 11044, 425, 21558, 12926, 496, 20198, 13735, 1002, 20205, 13937, 837]
}

df_visual_stasiun = pd.DataFrame(data_stasiun)

fig, ax = plt.subplots(figsize=(16, 10))
sns.barplot(x='station', y='count', hue='kualitas_udara', data=df_visual_stasiun, ax=ax)

ax.set_title('Distribusi Kualitas Udara Berdasarkan Stasiun')
ax.set_xlabel('Stasiun')
ax.set_ylabel('Jumlah')
ax.legend(title='Kualitas Udara')

ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig)

st.subheader("Visualisasi kualitas angin berdasarkan waktu")

st.text("Informasi yang bisa kita ambil dari chart diatas sebagai berikut :")

st.text("- kategori Baik terbanyak: Tahun 2016 dengan total 72.066.")

st.text("- Kategori Sedang terbanyak: Tahun 2014 dengan total 41.965.")

st.text("- Kategori Buruk terbanyak: Tahun 2014 dengan total 2.984.")

data = {
    'year': [2013, 2013, 2013, 2014, 2014, 2014, 2015, 2015, 2015, 2016, 2016, 2016, 2017, 2017, 2017],
    'kualitas_udara': ['Baik', 'Sedang', 'Buruk'] * 5,
    'count': [53804, 32418, 1872, 60156, 41965, 2984, 67318, 35327, 1878, 72066, 31875, 690, 9801, 6389, 315]
}

df_visual = pd.DataFrame(data)

st.set_option('deprecation.showPyplotGlobalUse', False)

fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x='year', y='count', hue='kualitas_udara', data=df_visual, ax=ax)

ax.set_title('Distribusi Kualitas Udara Berdasarkan Tahun')
ax.set_xlabel('Tahun')
ax.set_ylabel('Jumlah')
ax.legend(title='Kualitas Udara')

st.pyplot(fig)

st.subheader("Visualisasi kualitas angin berdasarkan waktu dan tempat")

penjelasan ="""
Informasi yang bisa diambil dari chart ini adalah pada tahun 2014 dan tahun 2015 kualitas udara yang dimiliki cenderung sedang ke buruk, 
sedangkan pada tahun 2016 dan 2017 kualitas udara yang dimiliki terlihat lebih baik dari tahun sebelumnya. 
Dan untuk berdasarkan tempat bisa dilihat daerah Dingling, Huairou, dan Changping memiliki kualitas udara yang baik dari tahun ke tahun, 
sedangkan untuk daerah Nongzhanguan, Wanliu, Wanshouxigong, Ganyuan, dan Gucheng 
memiliki kualitas udara yang cenderung sedang ke buruk dari tahun 2013 ke tahun 2015 dan mulai membaik pada tahun 2016 dan 2017."""

st.write(penjelasan)

data = {
    'station': ['Aotizhongxin']*5 + ['Changping']*5 + ['Dingling']*5 + ['Dongsi']*5 + ['Guanyuan']*5 + ['Gucheng']*5 +
                ['Huairou']*5 + ['Nongzhanguan']*5 + ['Shunyi']*5 + ['Tiantan']*5 + ['Wanliu']*5 + ['Wanshouxigong']*5,
    'Date': [2013, 2014, 2015, 2016, 2017]*12,
    'Baik': [3993, 5058, 5091, 5994, 796,
             5001, 5418, 6150, 6325, 876,
             5846, 6479, 6697, 7070, 973,
             4311, 4596, 5247, 5699, 777,
             4296, 4635, 5272, 5525, 797,
             3992, 4365, 5227, 5460, 762,
             5200, 5797, 6460, 6822, 934,
             4058, 4434, 5198, 5673, 777,
             4908, 5341, 5820, 6264, 770,
             4193, 5019, 5606, 5944, 796,
             4003, 4446, 5215, 5758, 776,
             4003, 4568, 5335, 5532, 767],
    'Buruk': [196, 257, 227, 74, 36,
              94, 183, 106, 33, 27,
              41, 50, 34, 42, 13,
              176, 194, 196, 82, 38,
              183, 363, 218, 69, 19,
              181, 308, 171, 53, 24,
              87, 86, 38, 5, 3,
              249, 384, 283, 108, 48,
              99, 174, 56, 54, 42,
              137, 200, 119, 23, 17,
              220, 437, 213, 107, 25,
              209, 348, 217, 40, 23]
}

df = pd.DataFrame(data)

heatmap_data = df.pivot_table(index='station', columns='Date', values='Buruk')

st.set_option('deprecation.showPyplotGlobalUse', False)

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt='g', linewidths=.5, ax=ax)

ax.set_title('Perubahan Kualitas Udara (Buruk) di Setiap Stasiun dari 2013 hingga 2017')
ax.set_xlabel('Tahun')
ax.set_ylabel('Stasiun')

st.pyplot(fig)