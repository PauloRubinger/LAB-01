import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# Carregar dados
# =========================

df = pd.read_csv("data/raw/repos_1000.csv")

# Converter datas
df["created_at"] = pd.to_datetime(df["created_at"])
df["updated_at"] = pd.to_datetime(df["updated_at"])

# =========================
# Criar métricas derivadas
# =========================

# Idade do repositório em anos
df["age_years"] = (pd.Timestamp.now(tz="UTC") - df["created_at"]).dt.days / 365

# Tempo desde última atualização (dias)
df["days_since_update"] = (pd.Timestamp.now(tz="UTC") - df["updated_at"]).dt.days

# Percentual de issues fechadas
df["closed_issues_ratio"] = df["issues_closed"] / df["issues_total"]

print("\nDataset carregado:")
print(df.head())

# ===============================
# RQ01
# Sistemas populares são antigos?
# ===============================

print("\nRQ01 — Idade média dos repositórios:")
print(df["age_years"].describe())

median_age = df["age_years"].median()
print("Mediana da idade:", median_age)

plt.figure()
df["age_years"].hist(bins=30)
plt.title("Distribuição da idade dos repositórios")
plt.xlabel("Idade (anos)")
plt.ylabel("Quantidade")
plt.savefig("reports/figures/age_distribution.png")

# =========================
# RQ02
# Contribuição externa
# =========================

print("\nRQ02 — Pull Requests aceitas:")
print(df["merged_prs"].describe())

median_prs = df["merged_prs"].median()
print("Mediana:", median_prs)

plt.figure()
sns.scatterplot(data=df, x="stars", y="merged_prs")
plt.title("Stars vs Pull Requests aceitas")
plt.savefig("reports/figures/stars_vs_prs.png")

# =========================
# RQ03
# Releases
# =========================

print("\nRQ03 — Releases:")
print(df["releases"].describe())

median_releases = df["releases"].median()
print("Mediana:", median_releases)

plt.figure()
sns.scatterplot(data=df, x="stars", y="releases")
plt.title("Stars vs Releases")
plt.savefig("reports/figures/stars_vs_releases.png")

# =========================
# RQ04
# Atualização
# =========================

print("\nRQ04 — Dias desde última atualização:")
print(df["days_since_update"].describe())

median_update = df["days_since_update"].median()
print("Mediana:", median_update)

plt.figure()
df["days_since_update"].hist(bins=30)
plt.title("Tempo desde última atualização")
plt.xlabel("Dias")
plt.ylabel("Quantidade")
plt.savefig("reports/figures/days_since_update.png")

# =========================
# RQ05
# Linguagens mais populares
# =========================

top_languages = df["language"].value_counts().head(10)

print("\nRQ05 — Linguagens mais populares:")
print(top_languages)

plt.figure()
sns.barplot(x=top_languages.values, y=top_languages.index)
plt.title("Top 10 linguagens")
plt.xlabel("Quantidade de repositórios")
plt.ylabel("Linguagem")
plt.savefig("reports/figures/top_languages.png")

# =============================
# RQ06
# Percentual de issues fechadas
# =============================

print("\nRQ06 — Percentual de issues fechadas:")
print(df["closed_issues_ratio"].describe())

median_closed_ratio = round(df["closed_issues_ratio"].median(), 2)
print("Mediana da razão de issues fechadas:", median_closed_ratio)

plt.figure()
df["closed_issues_ratio"].hist(bins=30)
plt.title("Distribuição da razão de issues fechadas")
plt.xlabel("Razão")
plt.ylabel("Quantidade")
plt.savefig("reports/figures/closed_issues_ratio.png")

# =========================
# RQ07 (BÔNUS)
# Métricas por linguagem
# =========================

# metrics_by_language = df.groupby("language").agg({
#     "merged_prs": "mean",
#     "releases": "mean",
#     "days_since_update": "mean"
# }).sort_values("merged_prs", ascending=False)

# print("\nRQ07 — Métricas médias por linguagem:")
# print(metrics_by_language.head(10))

# plt.figure()
# metrics_by_language.head(10)["merged_prs"].plot(kind="bar")
# plt.title("Pull Requests médias por linguagem")
# plt.ylabel("PRs aceitas")

# plt.figure()
# metrics_by_language.head(10)["releases"].plot(kind="bar")
# plt.title("Releases médias por linguagem")
# plt.ylabel("Releases")

# plt.figure()
# metrics_by_language.head(10)["days_since_update"].plot(kind="bar")
# plt.title("Tempo médio desde atualização por linguagem")
# plt.ylabel("Dias")
