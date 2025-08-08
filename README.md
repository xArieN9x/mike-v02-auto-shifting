# Mike Auto-Railway

## Cara Deploy Manual

1. Pergi ke [Railway](https://railway.app) dan login.  
2. Klik **New Project** → pilih **Deploy from GitHub**.  
3. Sambungkan akaun GitHub kalau belum.  
4. Cari repo `mike-auto-railway`.  
5. Pilih branch utama (biasanya `main` atau `master`).  
6. Setup environment variables berikut di Railway:  
   - `API_KEY`  
   - `GITHUB_TOKEN`  
   - `GITHUB_REPO` (contoh: `PakYa/mike-auto-railway`)  
   - `GITHUB_PATH` (contoh: `backup/memory_store.txt`)  
   - `GITHUB_CODE_PATH` (contoh: `backup/mike_v02_core.py`)  
   - `AUTO_BACKUP` (`true` atau `false`)  
7. Deploy dan start project.  

---

## Environment Variables yang perlu:

- `API_KEY` — kunci rahsia untuk akses API.  
- `GITHUB_TOKEN` — Personal Access Token GitHub dengan scope repo.  
- `GITHUB_REPO` — nama repo GitHub, contoh `PakYa/mike-auto-railway`.  
- `GITHUB_PATH` — path simpan memory, contoh `backup/memory_store.txt`.  
- `GITHUB_CODE_PATH` — path simpan kod, contoh `backup/mike_v02_core.py`.  
- `AUTO_BACKUP` — enable auto backup (true/false).  

---

Kalau nak buat button deploy kat README, Railway dah tak support **Create Template** macam dulu.  
Jadi kita kena deploy manual je.

---

**Selamat deploy, Pak Ya!**  
Kalau perlukan bantuan lagi, bagitau je.

