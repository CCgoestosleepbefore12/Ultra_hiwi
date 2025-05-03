import pandas as pd

file_path = r"C:\Users\34696\Desktop\2025WinterSemester\hiwi\Data_preprocessing\tkgl-smallpedia_edgelist.csv"
df = pd.read_csv(file_path)

df_sorted = df.sort_values(by=["head", "tail", "relation_type", "ts"]).reset_index(drop=True)
df_shuffled = df_sorted.sample(frac=1, random_state=42).reset_index(drop=True)

# 将 ts 列移到最后
cols = [col for col in df_shuffled.columns if col != "ts"] + ["ts"]
df_shuffled = df_shuffled[cols]


total_len = len(df_shuffled)
train_size = int(total_len * 0.7)
valid_size = int(total_len * 0.15)
test_size = total_len - train_size - valid_size

train_df = df_shuffled.iloc[:train_size]
valid_df = df_shuffled.iloc[train_size:train_size + valid_size]
test_df = df_shuffled.iloc[train_size + valid_size:]

train_txt_path = r"C:\Users\34696\Desktop\2025WinterSemester\hiwi\Data_preprocessing\Smallpedia\train.txt"
valid_txt_path = r"C:\Users\34696\Desktop\2025WinterSemester\hiwi\Data_preprocessing\Smallpedia\valid.txt"
test_txt_path  = r"C:\Users\34696\Desktop\2025WinterSemester\hiwi\Data_preprocessing\Smallpedia\test.txt"

train_df.to_csv(train_txt_path, sep='\t', index=False, header=False)
valid_df.to_csv(valid_txt_path, sep='\t', index=False, header=False)
test_df.to_csv(test_txt_path, sep='\t', index=False, header=False)


