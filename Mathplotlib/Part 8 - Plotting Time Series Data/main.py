import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt 
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')
# Small exemple as usual 
"""
dates = [
    datetime(2019,5,24),
    datetime(2019,5,25),
    datetime(2019,5,26),
    datetime(2019,5,27),
    datetime(2019,5,28),
    datetime(2019,5,29),
    datetime(2019,5,30),
    datetime(2019,5,31)
]

y = [0,2,5,1,4,8,1,7]

plt.plot_date(dates, y, linestyle = 'solid')
plt.gcf().autofmt_xdate() # Autoformate les dates pour plus de lisibilité

# Changer les formats de dates
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

date_format = mpl_dates.DateFormatter('%b, %d, %Y')
plt.gca().xaxis.set_major_formatter(date_format)

"""

data = pd.read_csv(("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-Python\\Mathplotlib\\Data\\bitcoin.csv"))
# price_date = data['Date']
# price_date = price_date.sort_values()
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle = 'solid')
plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlegend('Date')
plt.ylegend('Closing Price')



plt.tight_layout()

plt.show()