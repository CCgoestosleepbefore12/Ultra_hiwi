import pandas as pd

file_path = r"C:\Users\34696\Desktop\2025WinterSemester\hiwi\Data_preprocessing\tkgl-smallpedia_edgelist.csv"
df = pd.read_csv(file_path)

cols = [col for col in df.columns if col != "ts"] + ["ts"]
df = df[cols]

unique_ts = sorted(df['ts'].unique())
train_ts = set(unique_ts[:98])
valid_ts = set(unique_ts[98:108])
test_ts  = set(unique_ts[108:])

train_df = df[df['ts'].isin(train_ts)]
valid_df = df[df['ts'].isin(valid_ts)]
test_df  = df[df['ts'].isin(test_ts)]

train_txt_path = r"C:\Users\34696\Desktop\2025WinterSemester\hiwi\Data_preprocessing\SmallpediaInd\train.txt"
valid_txt_path = r"C:\Users\34696\Desktop\2025WinterSemester\hiwi\Data_preprocessing\SmallpediaInd\valid.txt"
test_txt_path  = r"C:\Users\34696\Desktop\2025WinterSemester\hiwi\Data_preprocessing\SmallpediaInd\test.txt"

train_df.to_csv(train_txt_path, sep='\t', index=False, header=False)
valid_df.to_csv(valid_txt_path, sep='\t', index=False, header=False)
test_df.to_csv(test_txt_path, sep='\t', index=False, header=False)

for name, path in [("train", train_txt_path), ("valid", valid_txt_path), ("test", test_txt_path)]:
    with open(path, "r", encoding="utf-8") as f:
        num_lines = len(f.readlines())
    print(f"{name}.txt 中共有 {num_lines} 行")


