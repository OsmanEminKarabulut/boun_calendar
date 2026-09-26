# Boğaziçi Academic Calendar Sync 🗓️

Automated iCalendar (`.ics`) feed for Boğaziçi University's official academic calendar.  
*Boğaziçi Üniversitesi resmi akademik takvimi için otomatik senkronize edilen iCalendar (`.ics`) beslemesi.*

[![Update Academic Calendar](https://github.com/OsmanEminKarabulut/boun_calendar/actions/workflows/update_calendar.yml/badge.svg)](https://github.com/OsmanEminKarabulut/boun_calendar/actions/workflows/update_calendar.yml)

[🇬🇧 English](#english) • [🇹🇷 Türkçe](#türkçe)

---

<a name="english"></a>
## 🇬🇧 English

### Subscription URLs

Choose your preferred language and copy the URL to subscribe in your calendar application (Google Calendar, Apple Calendar, Outlook):

- **English Calendar (🇬🇧):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_en_calendar.ics
  ```

- **Turkish Calendar (🇹🇷):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_calendar.ics
  ```

### How to Subscribe

- **Google Calendar:** Open [Google Calendar](https://calendar.google.com) > Click **+** next to *Other calendars* > Select **From URL** > Paste the URL.
- **Apple Calendar (macOS / iOS):** Open Calendar > Select *File* > *New Calendar Subscription...* > Paste the URL.
- **Outlook:** Open Calendar > *Add calendar* > *Subscribe from web* > Paste the URL.

### Features

- **Multi-Language Feeds:** Native Turkish and English feeds synchronized directly from the official university system.
- **Daily Auto-Sync:** Automated via GitHub Actions to track official calendar updates daily.
- **RFC 5545 Compliant:** All-day events properly follow the exclusive end-date specification, with full event descriptions and category labels.
- **No Duplicates:** Uses persistent `UID`s for clean in-place updates.

---

<a name="türkçe"></a>
## 🇹🇷 Türkçe

### Abonelik Linkleri

Tercih ettiğiniz dilin bağlantısını kopyalayarak takvim uygulamanıza (Google Takvim, Apple Takvim, Outlook) abone olabilirsiniz:

- **Türkçe Takvim (🇹🇷):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_calendar.ics
  ```

- **İngilizce Takvim (🇬🇧):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_en_calendar.ics
  ```

### Nasıl Abone Olunur?

- **Google Takvim:** [Google Takvim](https://calendar.google.com)'i açın > *Diğer takvimler* yanındaki **+** işaretine tıklayın > **URL'den** seçeneğini seçin > Linki yapıştırın.
- **Apple Takvim (macOS / iOS):** Takvim uygulamasını açın > *Dosya* > *Yeni Takvim Aboneliği...* seçeneğini seçin > Linki yapıştırın.
- **Outlook:** Takvim'i açın > *Takvim ekle* > *Web'den abone ol* seçeneğini seçin > Linki yapıştırın.

### Özellikler

- **Çift Dil Desteği:** Resmi üniversite sisteminden doğrudan çekilen Türkçe ve İngilizce takvim akışları.
- **Günlük Otomatik Senkronizasyon:** GitHub Actions ile her gün resmi takvim değişiklikleri otomatik takip edilir.
- **RFC 5545 Standartlarına Tam Uyum:** Tüm gün etkinlikleri, açıklamalar ve kategori etiketleri standartlara uygun olarak üretilir.
- **Sıfır Çakışma:** Tekrarlayan etkinlikleri önleyen kalıcı `UID` yapısı kullanılır.

---

## Local Setup / Yerel Kurulum

```bash
git clone https://github.com/OsmanEminKarabulut/boun_calendar.git
cd boun_calendar

python -m venv venv
# Windows: venv\Scripts\activate | Unix: source venv/bin/activate
pip install -r requirements.txt

python main.py
```
