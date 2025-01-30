import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    r = players.shape[0]
    c = players.shape[1]
    return [r, c]