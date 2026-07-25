"""
36: PDF Merger
Automate compilation of multiple PDFs using pypdf.
"""
def merge_pdfs(pdf_list, output="merged.pdf"):
    try:
        from pypdf import PdfWriter
        merger = PdfWriter()
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write(output)
        merger.close()
        print(f"PDFs merged into {output}")
    except Exception as e:
        print("PDF Merge helper loaded:", e)

if __name__ == "__main__":
    merge_pdfs(["doc1.pdf", "doc2.pdf"])
