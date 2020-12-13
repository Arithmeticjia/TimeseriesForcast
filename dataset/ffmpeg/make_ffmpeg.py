import pandas as pd

collectd = pd.read_csv("./collectd-ffmpeg.csv")
pdu = pd.read_csv("./pdu-ffmpeg.csv")

n_collectd = collectd.loc[1:]
n_pdu = pdu[["epoch", "power"]]

file = pd.merge(collectd, n_pdu, on="epoch")

csv_df = file.set_index('epoch', drop=True)
csv_df.to_csv("./collectd_pdu_ffmpeg.csv", index=False)

