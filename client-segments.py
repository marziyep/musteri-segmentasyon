import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Veri yükleme
df = pd.read_csv("musteri_segmentasyonu.csv")

# Kullanılacak özellikler
X = df[["Yıllık Gelir (bin TL)", "Harcama Skoru (1-100)", "Ziyaret Sıklığı (ay/kez)", "Sadakat Süresi (yıl)"]]

# Veriyi ölçekleme
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Kümelerin sayısını belirlemek için Elbow yöntemi
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init="auto")
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Elbow grafiği
plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Yöntemi ile Optimal Küme Sayısı")
plt.xlabel("Küme Sayısı")
plt.ylabel("WCSS")
plt.grid(True)
plt.show()

# K = 4 ile model
kmeans = KMeans(n_clusters=4, random_state=42, n_init="auto")
df["Segment"] = kmeans.fit_predict(X_scaled)

# Sonuçları görselleştir
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="Yıllık Gelir (bin TL)",
    y="Harcama Skoru (1-100)",
    hue="Segment",
    palette="Set2",
    s=80
)
plt.title("K-Means ile Müşteri Segmentasyonu")
plt.xlabel("Yıllık Gelir (bin TL)")
plt.ylabel("Harcama Skoru")
plt.legend(title="Segment")
plt.grid(True)
plt.tight_layout()
plt.show()

# Segmentlere göre istatistiksel özet
segment_ozet = df.groupby("Segment").mean(numeric_only=True)
print("Segment Bazlı Ortalama Değerler:\n", segment_ozet)