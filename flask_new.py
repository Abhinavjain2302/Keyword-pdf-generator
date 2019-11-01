from flask import Flask,jsonify,request,render_template
import requests
import re
import pdfkit
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def form():
    return render_template("index.html")


@app.route('/first',methods=['POST'])
def first():
    keyword=request.form.get('keyword')
    page = requests.get("https://www.google.dz/search?q="+keyword)
    soup = BeautifulSoup(page.content,"html.parser")
    #links = soup.findAll("a")
    List=[]
    for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        List.append(re.split(":(?=http)",link["href"].replace("/url?q=","")))
    r=requests.post('http://127.0.0.1:5000/pdfDownloader',json={'Result':List})
    return r.text
    #return jsonify({'Result':List,'keyword':keyword})

@app.route('/pdfDownloader',methods=['POST'])
def pdfDownloader():
    res=request.get_json()
    config = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltox\\bin\\wkhtmltopdf.exe")
    # pdfkit.from_url(res['Result'][1],"nlp.pdf",configuration=config)
    pdfkit.from_url('https://www.techsparks.co.in/hot-topic-for-project-and-thesis-machine-learning/',"nlp2.pdf",configuration=config)
    return "True"



if __name__ == '__main__':
    app.run()
