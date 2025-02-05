# Ahlak ve Sünnet Dergisi

## Django Projesi Kurulum ve Kullanım Talimatları

Bu belge, Django projesinin kurulumu, sanal ortamın oluşturulması, bağımlılıkların kurulması ve projenin çalıştırılması için adım adım talimatları sunmaktadır.

## Gereksinimler

Aşağıdaki programlar bilgisayarınızda kurulu olmalıdır:

- **pip (Python paket yöneticisi)**
- **Virtualenv (veya diğer sanal ortam yöneticisi)**
- **Git** (proje klonlamak için)

## Projeyi Kurma

### 1. Projeyi Git ile İndirme

Öncelikle projeyi Git kullanarak bilgisayarınıza klonlayın:

```bash
git clone https://github.com/MetinQardasov11/Ahlak-ve-Sunnet-Dergisi.git
```
<br>

### 2. Sanal Ortam Oluşturma

#### MacOS / Linux:

```bash
python3 -m venv env
source env/bin/activate
```

#### Windows:

```bash
python -m venv env
.\env\Scripts\activate
```
<br>

### 3. Gerekli Paketleri Kurma

```bash
pip install -r requirements.txt
```
<br>

### 4.Migrasyonları Uygulama

#### MacOS / Linux:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

#### Windows:

```bash
python manage.py makemigrations
python manage.py migrate
```

<br>

### 5. Superuser (Yönetici) Oluşturma

#### MacOS / Linux:

```bash
python3 manage.py createsuperuser
```

#### Windows:

```bash
python manage.py createsuperuser
```

<br>

### 6. Statik Dosyaları Toplama

#### MacOS / Linux:

```bash
python3 manage.py collectstatic
```

#### Windows:

```bash
python manage.py collectstatic
```

<br>

### 7. Projeyi Çalıştırma

#### MacOS / Linux:

```bash
python3 manage.py runserver
```

#### Windows:

```bash
python manage.py runserver
```
<br>

###  Bu `README.md` dosyası, projeyi kurmak ve çalıştırmak için gereken tüm adımları sunuyor. Başka birine projeyi kurmayı kolaylaştıracaktır.