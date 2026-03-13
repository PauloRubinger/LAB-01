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

# Tempo desde última atualização (horas)
df["hours_since_update"] = (pd.Timestamp.now(tz="UTC") - df["updated_at"]).dt.total_seconds() / 3600

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
plt.ylabel("Quantidade de repositórios")
plt.savefig("reports/figures/age_distribution.png", dpi=300)
plt.close()

# =========================
# RQ02
# Contribuição externa
# =========================

print("\nRQ02 — Pull Requests aceitas:")
print(df["merged_prs"].describe())

median_prs = df["merged_prs"].median()
print("Mediana:", median_prs)
plt.figure()

plt.scatter(df["stars"], df["merged_prs"], s=10, alpha=0.5)

plt.title("Estrelas vs Pull Requests aceitas")
plt.xlabel("Stars")
plt.ylabel("Merged PRs")

plt.savefig("reports/figures/stars_vs_prs.png", dpi=300)
plt.close()

# =========================
# RQ03
# Releases
# =========================

print("\nRQ03 — Releases:")
print(df["releases"].describe())

median_releases = df["releases"].median()
print("Mediana:", median_releases)

plt.figure()
plt.scatter(df["stars"], df["releases"], s=10, alpha=0.5)
plt.title("Estrelas vs Releases")
plt.xlabel("Stars")
plt.ylabel("Releases")
plt.savefig("reports/figures/stars_vs_releases.png", dpi=300)
plt.close()

# =========================
# RQ04
# Atualização
# =========================

print("\nRQ04 — Horas desde última atualização:")
print(df["hours_since_update"].describe())

median_update = df["hours_since_update"].median()
print("Mediana:", median_update)

plt.figure()
df["hours_since_update"].hist(bins=80)

plt.title("Tempo desde a última atualização")
plt.xlabel("Horas desde a última atualização")
plt.ylabel("Quantidade de repositórios")

plt.tight_layout()
plt.savefig("reports/figures/update_time_hours.png", dpi=300)
plt.close()

# =========================
# RQ05
# Linguagens mais populares
# =========================

top_languages = df["language"].value_counts().head(10)

print("\nRQ05 — Linguagens mais populares:")
print(top_languages)

plt.figure()
sns.barplot(x=top_languages.values, y=top_languages.index)
plt.title("Linguagens principais mais utilizadas")
plt.xlabel("Quantidade de repositórios")
plt.ylabel("Linguagem principal")
plt.tight_layout()
plt.savefig("reports/figures/top_languages.png", dpi=300)
plt.close()

# =============================
# RQ06
# Percentual de issues fechadas
# =============================

print("\nRQ06 — Percentual de issues fechadas:")
print(df["closed_issues_ratio"].describe())

median_closed_ratio = df["closed_issues_ratio"].median()
print(f"Mediana da razão de issues fechadas: {median_closed_ratio:.2f}")

plt.figure()
df["closed_issues_ratio"].hist(bins=30)
plt.title("Distribuição da razão de issues fechadas")
plt.xlabel("Razão")
plt.ylabel("Quantidade de repositórios")
plt.savefig("reports/figures/closed_issues_ratio.png", dpi=300)
plt.close()

# =========================
# RQ07 (BÔNUS)
# Métricas por linguagem
# =========================

# metrics_by_language = df.groupby("language").agg({
#     "merged_prs": "mean",
#     "releases": "mean",
#     "hours_since_update": "mean"
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
# metrics_by_language.head(10)["hours_since_update"].plot(kind="bar")
# plt.title("Tempo médio desde atualização por linguagem")
# plt.ylabel("Horas")

medians = {
    "metric": [
        "age_years",
        "merged_prs",
        "releases",
        "hours_since_update",
        "closed_issues_ratio"
    ],
    "median": [
        round(df["age_years"].median(), 2),
        round(df["merged_prs"].median(), 2),
        round(df["releases"].median(), 2),
        round(df["hours_since_update"].median(), 2),
        round(df["closed_issues_ratio"].median(), 2)
    ]
}

median_df = pd.DataFrame(medians)

median_df.to_csv("data/processed/medians.csv", index=False)

plt.figure(figsize=(6,3))

plt.axis("off")

metric_names = {
    "age_years": "Idade do repositório (anos)",
    "merged_prs": "Pull Requests aceitas",
    "releases": "Número de releases",
    "hours_since_update": "Horas desde última atualização",
    "closed_issues_ratio": "Razão de issues fechadas"
}

median_df["metric"] = median_df["metric"].replace(metric_names)
median_df = median_df.rename(columns={
    "metric": "Métrica",
    "median": "Mediana"
})

table = plt.table(
    cellText=median_df.values,
    colLabels=median_df.columns,
    loc="center"
)

table = plt.table(
    cellText=median_df.values,
    colLabels=median_df.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.6)

plt.title("Mediana das métricas analisadas")
plt.savefig("reports/figures/medians_table.png", bbox_inches="tight", dpi=300)
plt.close()