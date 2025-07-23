# 🔓 Hash Cracker — Multi-threaded Hash Cracking Framework

A powerful, modular, and blazing-fast hash cracking tool written in Python.  
Supports **dictionary** and **character-based brute-force** attacks using multi-threading.

> 🧠 Built for learning, testing, and red team simulation — not blind brute force.

---

## 🚀 Features

- ✅ Supports popular hash types: `MD5`, `SHA1`, `SHA256`, `SHA224`, `SHA384`, `SHA512`
- ⚡ Multi-threaded dictionary + charset-based brute-force attack
- 🔐 Thread-safe hash matching with clean exit on match
- 🧠 Custom character set + min/max length for controlled brute
- 🧰 Flexible CLI with both wordlist and charset mode
- 🔒 Future-ready: easily extendable to `NTLM`, `bcrypt`, and more

---

## 🧪 Supported Hashes

| Hash Type | CLI Value |
|-----------|-----------|
| MD5       | `md5`     |
| SHA-1     | `sha1`    |
| SHA-256   | `sha256`  |
| SHA-224   | `sha224`  |
| SHA-384   | `sha384`  |
| SHA-512   | `sha512`  |

---

## ⚙️ Usage

```bash
python crack.py --hash <HASH> --type <HASH_TYPE> [options]
```

---

### 📖 Dictionary Mode

Crack using a wordlist:

```bash
python crack.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --type md5 --wordlist_path rockyou.txt --threads 30
```

---

### 💣 Brute-Force Mode

Crack using character set combinations:

```bash
python crack.py --hash d14d2f1a21df38436e4d7022e3cf9b8aa176d9f9 --type sha1 --string 1234567890qwerty --min_lenght 4 --max_lenght 6
```

> Use `--string` to provide charset  
> Use `--min_lenght` and `--max_lenght` to control password size

---

## 🧩 Arguments

| Flag                     | Description                                  |
|--------------------------|----------------------------------------------|
| `--hash` / `-hash`       | Hash to crack                                |
| `--type` / `-type`       | Hash type (`md5`, `sha1`, etc.)              |
| `--wordlist_path` / `-w` | Path to wordlist (dictionary mode)           |
| `--threads` / `-t`       | Number of threads to use                     |
| `--string` / `-s`        | Character set for brute-force mode           |
| `--min_lenght` / `-mi`   | Minimum length for brute-force               |
| `--max_lenght` / `-mx`   | Maximum length for brute-force               |
| `--mode_brute` / `-mb`   | Enable brute-force mode (optional toggle)    |

---

## 🧠 Notes

- Python's GIL limits true multithreading — use `--threads` wisely (20–50 recommended)
- Large charsets + long lengths = billions of combinations → use responsibly
- Salts/peppers, bcrypt/PBKDF2/Argon2 hashes are not supported (yet)
- This tool is for **educational or legal red-team use only**

---

## 📦 Upcoming / Future Features

- [ ] NTLM and bcrypt support
- [ ] Resume from failed/crashed sessions
- [ ] Logging cracked hashes to file
- [ ] Hybrid attack mode (wordlist + mutations)
- [ ] Rainbow table lookup module

---

##  Author

**err0rgod**  

> _"Know the limits of your code. Then break them with intent."_
