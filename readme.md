# 🌐 BetaFastDomain

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/badge/Async-Enabled-ff69b4?style=for-the-badge" alt="Async" />
  <img src="https://img.shields.io/badge/Creator-zakariaelqannaa--dv-orange?style=for-the-badge&logo=github" alt="Creator" />
</p>

<p align="center">
  <strong>High-performance, asynchronous CLI tool built in Python for instant domain availability and active DNS checking using modern RDAP protocols.</strong>
</p>

---

## 🚀 Key Features

- **⚡ Ultra-Fast Async Queries:** Checks dozens of domains simultaneously in parallel using `asyncio` & `httpx`.
- **🔍 Dual-Layer Verification:** Combines ICANN RDAP protocol lookup with active DNS Name Server (`NS`) resolution.
- **💡 Smart Auto-TLD Expansion:** Automatically checks `.com`, `.net`, `.io`, and `.ma` if no extension is specified.
- **🎨 Rich Terminal Interface:** Beautiful, colorful CLI tables powered by `rich`.
- **🔁 Interactive Console:** Continuous search loop with URL cleaning (`https://`, `www.` auto-strip).

---

## 🛠️ Built With

- **Language:** [Python 3.10+](https://www.python.org/)
- **HTTP Client:** [httpx](https://www.python-httpx.org/) *(Async HTTP)*
- **DNS Resolver:** [dnspython](https://www.dnspython.org/) *(Async DNS)*
- **Terminal UI:** [Rich](https://rich.readthedocs.io/)

---

## 💻 How to Run in Your IDE

### 1. Clone the repository
```bash
git clone [https://github.com/zakariaelqannaa-dv/betafastdomain.git](https://github.com/zakariaelqannaa-dv/betafastdomain.git)
cd betafastdomain
2. Set up a Virtual Environment
Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
## Bash
pip install httpx dnspython rich
4. Run the Application

## Bash
python app.py

###📂 Project Structure
Plaintext
betafastdomain/
├── app.py         # Main CLI Application & Terminal UI
├── checker.py     # Asynchronous DNS & RDAP Core Logic
└── README.md      # Documentation

###👤 Author
zakariaelqannaa-dv

### 📝 License
This project is MIT licensed.