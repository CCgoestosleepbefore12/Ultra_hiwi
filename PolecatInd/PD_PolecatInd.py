import pandas as pd

file_path = r"c:\Users\Chengcheng\Desktop\2025Sommersemester\hiwi\data_preprocessing\tkgl-polecat_edgelist.csv"

df = pd.read_csv(file_path)


# 调整列顺序：将 relation_type 和 tail 换位置
cols_order = df.columns.tolist()
rel_idx, tail_idx = cols_order.index("relation_type"), cols_order.index("tail")
cols_order[rel_idx], cols_order[tail_idx] = cols_order[tail_idx], cols_order[rel_idx]
df = df[cols_order]

cols = [col for col in df.columns if col != "date"] + ["date"]
df = df[cols]


unique_date = sorted(df['date'].unique())
train_date = set(unique_date[:1193])
valid_date = set(unique_date[1193:1522])
test_date  = set(unique_date[1522:])

train_df = df[df['date'].isin(train_date)]
valid_df = df[df['date'].isin(valid_date)]
test_df  = df[df['date'].isin(test_date)]

train_txt_path = r"C:\Users\Chengcheng\Desktop\2025Sommersemester\hiwi\data_preprocessing\PolecatInd\train.txt"
valid_txt_path = r"C:\Users\Chengcheng\Desktop\2025Sommersemester\hiwi\data_preprocessing\PolecatInd\valid.txt"
test_txt_path  = r"C:\Users\Chengcheng\Desktop\2025Sommersemester\hiwi\data_preprocessing\PolecatInd\test.txt"

train_df.to_csv(train_txt_path, sep='\t', index=False, header=False)
valid_df.to_csv(valid_txt_path, sep='\t', index=False, header=False)
test_df.to_csv(test_txt_path, sep='\t', index=False, header=False)

for name, path in [("train", train_txt_path), ("valid", valid_txt_path), ("test", test_txt_path)]:
    with open(path, "r", encoding="utf-8") as f:
        num_lines = len(f.readlines())
    print(f"{name}.txt 中共有 {num_lines} 行")



