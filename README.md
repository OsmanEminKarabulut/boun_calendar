# Boğaziçi Academic Calendar Sync 🗓️

Automated iCalendar (`.ics`) feed for Boğaziçi University's official academic calendar and YADYOK (School of Foreign Languages) preparatory school calendar.  
*Boğaziçi Üniversitesi resmi akademik takvimi ve YADYOK (Yabancı Diller Yüksekokulu) hazırlık takvimi için otomatik senkronize edilen iCalendar (`.ics`) beslemesi.*

[![Update Academic Calendar](https://github.com/OsmanEminKarabulut/boun_calendar/actions/workflows/update_calendar.yml/badge.svg)](https://github.com/OsmanEminKarabulut/boun_calendar/actions/workflows/update_calendar.yml)

[🇬🇧 English](#english) • [🇹🇷 Türkçe](#türkçe)

---

<a name="english"></a>
## 🇬🇧 English

### Subscription URLs

Choose your preferred calendar and language, then copy the URL to subscribe in your calendar application (Google Calendar, Apple Calendar, Outlook):

#### 📚 General Academic Calendar (All University)
- **English Calendar (🇬🇧):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_en_calendar.ics
  ```
- **Turkish Calendar (🇹🇷):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_calendar.ics
  ```

#### 🎓 SFL / Preparatory School Calendar (YADYOK Only)
- **English SFL Calendar (🇬🇧):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_en_yadyok_calendar.ics
  ```
- **Turkish YADYOK Calendar (🇹🇷):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_tr_yadyok_calendar.ics
  ```

### How to Subscribe

- **Google Calendar:** Open [Google Calendar](https://calendar.google.com) > Click **+** next to *Other calendars* > Select **From URL** > Paste the URL.
- **Apple Calendar (macOS / iOS):** Open Calendar > Select *File* > *New Calendar Subscription...* > Paste the URL.
- **Outlook:** Open Calendar > *Add calendar* > *Subscribe from web* > Paste the URL.

### Features

- **General & YADYOK Feeds:** Subscribe either to the complete university academic calendar or exclusively to the School of Foreign Languages (SFL / Hazırlık) calendar.
- **Multi-Language Feeds:** Native Turkish and English feeds synchronized directly from the official university system.
- **Daily Auto-Sync:** Automated via GitHub Actions to track official calendar updates daily.
- **RFC 5545 Compliant:** All-day events properly follow the exclusive end-date specification, with full event descriptions and category labels.
- **No Duplicates:** Uses persistent `UID`s for clean in-place updates.

---

<a name="türkçe"></a>
## 🇹🇷 Türkçe

### Abonelik Linkleri

Takvim uygulamanıza (Google Takvim, Apple Takvim, Outlook) eklemek için ilgili takvim ve dil bağlantısını kopyalayın:

#### 📚 Genel Akademik Takvim (Tüm Üniversite)
- **Türkçe Takvim (🇹🇷):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_calendar.ics
  ```
- **İngilizce Takvim (🇬🇧):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_en_calendar.ics
  ```

#### 🎓 YADYOK / Hazırlık Okulu Takvimi (Sadece Hazırlık)
- **Türkçe YADYOK Takvimi (🇹🇷):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_tr_yadyok_calendar.ics
  ```
- **İngilizce SFL Takvimi (🇬🇧):**
  ```text
  https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_en_yadyok_calendar.ics
  ```

### Nasıl Abone Olunur?

- **Google Takvim:** [Google Takvim](https://calendar.google.com)'i açın > *Diğer takvimler* yanındaki **+** işaretine tıklayın > **URL'den** seçeneğini seçin > Linki yapıştırın.
- **Apple Takvim (macOS / iOS):** Takvim uygulamasını açın > *Dosya* > *Yeni Takvim Aboneliği...* seçeneğini seçin > Linki yapıştırın.
- **Outlook:** Takvim'i açın > *Takvim ekle* > *Web'den abone ol* seçeneğini seçin > Linki yapıştırın.

### Özellikler

- **Genel & YADYOK Seçeneği:** İster tüm üniversite takvimine, istersen sadece Yabancı Diller Yüksekokulu (YADYOK / Hazırlık) takvimine abone olma imkanı.
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
