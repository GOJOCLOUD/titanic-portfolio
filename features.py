# ===========================
# 特征工程 Feature Engineering
# ===========================

# 1. 家庭大小 FamilySize = SibSp + Parch + 1 (自己也算进去)
train_data["FamilySize"] = train_data["SibSp"] + train_data["Parch"] + 1
test_data["FamilySize"]  = test_data["SibSp"] + test_data["Parch"] + 1

# 2. 是否独自一人 IsAlone (1=独自一人, 0=有人陪伴)
train_data["IsAlone"] = (train_data["FamilySize"] == 1).astype(int)
test_data["IsAlone"]  = (test_data["FamilySize"] == 1).astype(int)

# --- 可选: 打印检查一下 ---
print("FamilySize (train):\n", train_data["FamilySize"].value_counts().sort_index().head())
print("IsAlone (train):\n", train_data["IsAlone"].value_counts())
print(train_data[["SibSp", "Parch", "FamilySize", "IsAlone"]].head())
