from src.tvdata import TvDatafeed, Interval

if __name__ == "__main__":
    
    tv = TvDatafeed()

    print(
        tv.get_hist(
            "EICHERMOT",
            "NSE",
            interval=Interval.in_daily,
            n_bars=100,
            extended_session=True,
        )
    )