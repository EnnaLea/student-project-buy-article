import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv", dtype={"id": str})


class Article:
    def __init__(self, cod_article):
        self.cod = cod_article
        self.name = df.loc[df["id"] == self.cod, 'name'].squeeze()
        self.price = df.loc[df["id"] == self.cod, 'price'].squeeze()

    def available(self):
        in_stock = df.loc[df['id'] == self.cod, 'in_stock'].squeeze()
        return in_stock


class Receipt:
    def __init__(self, article_id):
        self.article = article_id

    def print_receipt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.cod}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")



print(df)
cod = input("Enter the code of the article to buy: ")
article = Article(cod)
if article.available():
    receipt = Receipt(article)
    receipt.print_receipt()
else:
    print("The article doesn't exist")