import pandas as pd
from fbprophet import Prophet

df = pd.read_csv('dummyDataset20200617_150932.csv')
df.drop(["plaka","marka","model","uretim_tarihi","km","parca_fiyat"],axis =1, inplace=True)
df = df.rename(columns={'tarih' : 'ds', 'iscilik_fiyat' : 'y'})
df.drop(df.loc[3000:24000].index, inplace=True)

m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=365)
future.tail()
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)

