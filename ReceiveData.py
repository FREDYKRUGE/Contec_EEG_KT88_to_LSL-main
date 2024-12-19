"""
Tha's an example row of what is the output from line 26
21084.1634367 [-69.69999694824219, 27.100000381469727, 20.399999618530273, -24.5, -204.8000030517578, -15.899999618530273, -0.800000011920929, -204.8000030517578, -198.60000610351562, -139.10000610351562, 26.299999237060547,
104.4000015258789, -204.8000030517578, -74.9000015258789, -23.600000381469727, -158.89999389648438, 79.0, -204.8000030517578, -5.400000095367432, -28.299999237060547, -11.899999618530273, 21.700000762939453, 15.0, 110.30000305175781,
4.199999809265137, 32.599998474121094]
"""

from pylsl import resolve_stream, StreamInlet
# from django import urls



# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample, timestamp = inlet.pull_sample()
    print(timestamp, sample)