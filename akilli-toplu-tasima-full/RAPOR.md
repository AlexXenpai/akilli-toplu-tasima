# Veri Yapıları Proje Ara Raporu

## Proje Adı

Akıllı Toplu Taşıma ve Navigasyon Sistemi

## Ekip Üyeleri

- Sukru
- Emin
- Ali
- Taha
- Kerem

## Projenin Amacı

Bu projenin amacı, bir şehirdeki toplu taşıma ağını veri yapıları kullanarak modellemek ve kullanıcıya uygun rota hesaplayan bir sistem geliştirmektir.

Duraklar graf düğümü, duraklar arası ulaşım bağlantıları ise ağırlıklı kenar olarak ele alınmıştır. Kullanıcı bir konum seçtiğinde sistem, bu konuma en yakın K durağı bulur. Ardından başlangıç ve hedef durak arasında en düşük maliyetli rota hesaplanır.

## Kullanılan Teknolojiler

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Veri formatı: JSON
- Çalıştırma ortamı: Docker
- Versiyon kontrolü: GitHub

## Kullanılan Veri Yapıları

### KD-Tree

Durakların koordinatlarını saklamak ve en yakın durakları bulmak için kullanılmıştır.

Ortalama karmaşıklık:

```text
O(log N)
```

En kötü durum:

```text
O(N)
```

### Graph

Toplu taşıma ağı graf olarak modellenmiştir.

- Düğümler: Duraklar
- Kenarlar: Duraklar arası bağlantılar
- Kenar özellikleri: süre, mesafe, hat bilgisi

### Min-Heap

Dijkstra algoritmasında en düşük maliyetli durağı seçmek için kullanılır.

```text
Ekleme: O(log N)
Çıkarma: O(log N)
```

### Hash Table

Durak bilgilerine hızlı erişim sağlamak için kullanılır.

```text
Ortalama erişim: O(1)
```

## Kullanılan Algoritmalar

### KNN

Kullanıcının seçtiği konuma en yakın K durağı bulur. Bu işlem KD-Tree üzerinde yapılır.

### Dijkstra

Başlangıç ve hedef durak arasında en kısa / en düşük maliyetli yolu bulur.

Bu projede kenar ağırlığı olarak süre değeri kullanılmıştır.

```text
O((V + E) log V)
```

## API Uç Noktaları

### GET /api/stops

Tüm durakları döndürür.

### GET /api/connections

Duraklar arası bağlantıları döndürür.

### POST /api/nearest

Kullanıcı koordinatına en yakın K durağı döndürür.

Örnek:

```json
{
  "x": 250,
  "y": 180,
  "k": 3
}
```

### POST /api/route

Başlangıç ve hedef durak arasında rota hesaplar.

Örnek:

```json
{
  "start": "D1",
  "target": "D6"
}
```

## GitHub Çalışma Planı

Ana branch'e doğrudan kod gönderilmeyecektir. Her ekip üyesi kendi branch'i üzerinde çalışacak ve Pull Request açacaktır.

```text
main
feature/frontend-ui
feature/backend-api
feature/graph-dijkstra
feature/kdtree-knn
feature/docs-docker
```

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

## Şu Ana Kadar Yapılanlar

- Proje konusu incelendi.
- Kullanılacak veri yapıları belirlendi.
- Sistem mimarisi tasarlandı.
- Frontend ve backend klasör yapısı oluşturuldu.
- Örnek şehir veri seti hazırlandı.
- Graph, KD-Tree, Min-Heap ve Hash Table yapıları oluşturuldu.
- Dijkstra algoritması eklendi.
- Docker yapılandırması hazırlandı.

## Sonraki Aşamalar

- Daha büyük test veri seti oluşturulacak.
- Rota maliyet modeline aktarma cezası eklenecek.
- Demo videosu hazırlanacak.
- UML diyagramları rapora eklenecek.
- Kod savunması için ekip içi prova yapılacak.