all_data={}
for ticker in ['AAPL','IBM','MSFT']:
         all_data[ticker]=web.get_data_yahoo(ticker,'1/1/2010','1/1/2013')
price = DataFrame({tic:data['Adj Close'] for tic, data in all_data.iteritems()})
volume = DataFrame({tic:data['Volume'] for tic, data in all_data.iteritems()})
returns = price.pct_change()

returns.MSFT.cov(returns.IBM)
returns.cov()
plt.imshow(Z);plt.colorbar()
