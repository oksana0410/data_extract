import pandas as pd


def bidfloor_value(body: str):
    if not isinstance(body, str):
        return None

    start_index = body.find("bidfloor")

    if start_index == -1:
        return None

    start_index += len("bidfloor\":")
    end_index = body.find(",", start_index)

    if end_index == -1:
        return None

    return body[start_index:end_index]


df = pd.read_excel("Logs.xlsx")
df["D"] = df["Body"].apply(bidfloor_value)
