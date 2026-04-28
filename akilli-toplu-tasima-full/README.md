# Akıllı Toplu Taşıma ve Navigasyon Sistemi

## Proje Konusu

Bu proje, Veri Yapıları dersi kapsamında verilen **Proje Konu 5: Akıllı Toplu Taşıma ve Navigasyon Sistemi** için hazırlanmıştır.

Projede şehir toplu taşıma ağı sadeleştirilmiş biçimde modellenmiştir. Duraklar graf düğümü, duraklar arası bağlantılar ise ağırlıklı kenar olarak temsil edilir.

Sistem şu işlemleri yapar:

- Harita üzerinde durakları gösterir.
- Kullanıcının seçtiği konuma en yakın K durağı bulur.
- Başlangıç ve hedef durak arasında en kısa rotayı hesaplar.
- Rota sonucunu web arayüzünde görselleştirir.

---

## Ekip Üyeleri

- Sukru
- Emin
- Ali
- Taha
- Kerem

> Not: Değerlendirme şartına uygun olması için kod ve dokümantasyonda Türkçe karakter kullanılmamıştır.

---

## Kullanılan Veri Yapıları

### KD-Tree

Durak koordinatlarını saklamak ve kullanıcının konumuna en yakın K durağı bulmak için kullanılır.

Ortalama arama karmaşıklığı:

```text
O(log N)
```

En kötü durum:

```text
O(N)
```

### Graph / Multigraph

Toplu taşıma ağı graf olarak modellenmiştir.

- Düğümler: Duraklar
- Kenarlar: Duraklar arası bağlantılar
- Kenar bilgileri: süre, mesafe, hat bilgisi

### Min-Heap

Dijkstra algoritmasında en düşük maliyetli düğümü seçmek için kullanılır.

```text
Ekleme: O(log N)
Çıkarma: O(log N)
```

### Hash Table

Durak ID değerinden durak bilgisine hızlı erişmek için kullanılır.

```text
Ortalama erişim: O(1)
```

---

## Kullanılan Algoritmalar

### KNN

Kullanıcının seçtiği koordinata en yakın K durağı bulur.

### Dijkstra

Başlangıç ve hedef durak arasındaki en düşük maliyetli rotayı hesaplar.

```text
O((V + E) log V)
```

---

## Proje Mimarisi

```text
akilli-toplu-tasima-full/
|
├── backend/
|   ├── app.py
|   ├── data/
|   |   └── sample_city.json
|   ├── structures/
|   |   ├── graph.py
|   |   ├── hash_table.py
|   |   ├── kd_tree.py
|   |   └── min_heap.py
|   ├── algorithms/
|   |   └── dijkstra.py
|   └── requirements.txt
|
├── frontend/
|   ├── index.html
|   ├── style.css
|   └── script.js
|
├── Dockerfile
├── docker-compose.yml
├── README.md
└── RAPOR.md
```

---

## Çalıştırma

Docker kuruluysa:

```bash
docker-compose up --build
```

Tarayıcıdan aç:

```text
http://localhost:8080
```

Backend API:

```text
http://localhost:5000
```

---

## Görev Dağılımı

### Sukru

Frontend arayüz, harita çizimi ve rota görselleştirme.

### Emin

Backend API, Flask bağlantıları ve veri okuma işlemleri.

### Ali

Graph veri yapısı, Dijkstra algoritması ve Min-Heap entegrasyonu.

### Taha

KD-Tree yapısı ve KNN en yakın durak sorgusu.

### Kerem

Hash Table, Docker yapılandırması, test ve dokümantasyon.

---

## Branch Planı

```text
main
feature/frontend-ui
feature/backend-api
feature/graph-dijkstra
feature/kdtree-knn
feature/docs-docker
```

---

## Demo Senaryosu

1. Web arayüzü açılır.
2. Duraklar harita üzerinde görüntülenir.
3. Kullanıcı harita üzerinde bir noktaya tıklar.
4. Sistem seçilen noktaya en yakın K durağı KD-Tree ile bulur.
5. Kullanıcı başlangıç ve hedef durağı seçer.
6. Dijkstra algoritması en kısa rotayı hesaplar.
7. Rota harita üzerinde yeşil çizgi ile gösterilir.