import pyttsx3, PyPDF2


PDFread = PyPDF2.PdfReader(open("book.pdf", "rb"))
speaker = pyttsx3.init()

for page_num in range(len(PDFread.pages)):
    text = PDFread.pages[page_num].extract_text()
    clean_text = text.strip().replace("\n", " ")
    print(clean_text)

speaker.save_to_file(clean_text, "Story.mp3")
speaker.runAndWait()

speaker.stop()