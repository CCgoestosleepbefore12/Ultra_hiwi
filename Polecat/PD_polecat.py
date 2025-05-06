import pandas as pd
import os

file_path = r"c:\Users\Chengcheng\Desktop\2025Sommersemester\hiwi\data_preprocessing\tkgl-polecat_edgelist.csv"
df = pd.read_csv(file_path)

df_sorted = df.sort_values(by=["head", "tail", "relation_type", "date"]).reset_index(drop=True)


# 调整列顺序：将 relation_type 和 tail 换位置
cols = df_sorted.columns.tolist()
rel_idx, tail_idx = cols.index("relation_type"), cols.index("tail")
cols[rel_idx], cols[tail_idx] = cols[tail_idx], cols[rel_idx]

# 将 date 列移到最后
cols = [col for col in cols if col != "date"] + ["date"]

df_sorted = df_sorted[cols]

df_shuffled = df_sorted.sample(frac=1, random_state=42).reset_index(drop=True)

# print(df_sorted.head())

total_len = len(df_shuffled)

train_size = int(total_len * 0.7)
valid_size = int(total_len * 0.15)
test_size = total_len - train_size - valid_size

# print(total_len,train_size,valid_size,test_size)

train_df = df_shuffled.iloc[:train_size]
valid_df = df_shuffled.iloc[train_size:train_size + valid_size]
test_df = df_shuffled.iloc[train_size + valid_size:]

# print(train_df.head())
# print(valid_df.head())
# print(test_df.head())
# print("Train size:", len(train_df))
# print("Valid size:", len(valid_df))
# print("Test size:", len(test_df))

train_txt_path = r"C:\Users\Chengcheng\Desktop\2025Sommersemester\hiwi\data_preprocessing\Polecat\train.txt"
valid_txt_path = r"C:\Users\Chengcheng\Desktop\2025Sommersemester\hiwi\data_preprocessing\Polecat\valid.txt"
test_txt_path  = r"C:\Users\Chengcheng\Desktop\2025Sommersemester\hiwi\data_preprocessing\Polecat\test.txt"



train_df.to_csv(train_txt_path, sep='\t', index=False, header=False)
valid_df.to_csv(valid_txt_path, sep='\t', index=False, header=False)
test_df.to_csv(test_txt_path, sep='\t', index=False, header=False)

print("Train file size:", os.path.getsize(train_txt_path), "bytes")
print("Valid file size:", os.path.getsize(valid_txt_path), "bytes")
print("Test file size:", os.path.getsize(test_txt_path), "bytes")