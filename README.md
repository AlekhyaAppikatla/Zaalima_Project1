# 📄 Invoice PDF Extractor

A GUI-based Python application that connects to your Gmail inbox, downloads PDF invoice attachments based on subject keywords, extracts key-value data from the PDFs, and displays the results in a table with the option to export to CSV.

---

## 🖼️ Features

- 🔐 Secure Gmail login (via app password)
- 📥 Downloads `.pdf` attachments with subject keyword **"Invoice"**
- 🧾 Extracts key-value data from PDF invoices
- 📊 Displays extracted data in a table
- 📁 Exports data to a `CSV` file
- 📜 Generates log file for debugging

---

## 🛠️ Technologies Used

- `Python 3.x`
- `tkinter` – GUI framework
- `imaplib`, `email` – Email handling via IMAP
- `PyPDF2` – PDF text extraction
- `pandas` – For CSV export
- `logging` – Logging application events
- `threading` – Background processing to keep GUI responsive

---

## 🚀 Getting Started

### 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/invoice-pdf-extractor.git
   cd invoice-pdf-extractor
   ```

2. **Install required packages**
   ```bash
   pip install pandas PyPDF2
   ```

   > Optional (for better PDF extraction):
   ```bash
   pip install pdfplumber
   ```

---

## 📩 Gmail Setup Instructions

To allow the app to connect to your Gmail:

1. Enable **IMAP** in Gmail settings:
   - Go to [Gmail Settings](https://mail.google.com/)
   - Navigate to **Forwarding and POP/IMAP**
   - Enable **IMAP**

2. Generate an **App Password**:
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Turn on **2-Step Verification**
   - Under **App Passwords**, generate a password for "Mail"

3. Use the generated password in the app for login.

---

## ▶️ How to Run

1. Open terminal and run:
   ```bash
   python invoice_extractor.py
   ```

2. In the GUI:
   - Enter your Gmail email address
   - Enter the generated **App Password**
   - Click **Download PDFs** to start fetching emails and extracting data

3. Once processed, the invoice data will appear in a table.

4. Click **Export to CSV** to save the data as `extracted_data.csv`.

5. Click **Exit** to close the app.

---

## 📁 Files and Outputs

| File/Folder         | Description                                         |
|---------------------|-----------------------------------------------------|
| `invoice_extractor.py` | Main Python script                                |
| `attachments/`      | Folder where downloaded PDF files are saved         |
| `extracted_data.csv`| Extracted invoice data in CSV format                |
| `invoice_app.log`   | Log file with application events                    |
| `README.md`         | This documentation file                             |

---

## 📊 Sample Output (Extracted Key-Value Table)

| Invoice Number | Date       | Amount | Customer Name |
|----------------|------------|--------|----------------|
| INV-2024-01    | 2024-07-01 | $250   | John Smith     |
| INV-2024-02    | 2024-07-02 | $400   | Jane Doe       |

> Extracted from PDF lines like: `Invoice Number: INV-2024-01`

---

## 💡 Future Enhancements

- 🧠 Use NLP or fuzzy matching for better key extraction
- 🔍 Add search/filtering functionality in UI
- 🖨️ Add support for scanned PDFs using OCR (`pytesseract`)
- 🔐 Add OAuth2 login for secure Gmail access
- 📦 Package app into `.exe` using `PyInstaller` for easier distribution

---

## 🧪 Testing Tips

- Use Gmail to send yourself PDF invoices with the subject: `Invoice`
- Try invoices with varied formatting to test extraction robustness
- Check the `attachments/` and `invoice_app.log` for troubleshooting

---

## 📃 License

MIT License. You can use, modify, and distribute freely.

---

## 👤 Author

**Alekya Appikatla**  
If you have any suggestions, feel free to reach out or contribute.

---
