from pathlib import Path

directory_dict = dict({'data': r'.\data', 'output': r'.\output','cache':r'.\cache','helper':r'.\helper','logs':r'.\logs'})

for idx in directory_dict:
    p=Path(directory_dict[idx])
    p.mkdir(exist_ok=True)
