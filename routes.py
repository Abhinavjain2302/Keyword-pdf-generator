from flask import Flask,jsonify,request,render_template
import requests
import re
import pdfkit
import bs4
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def form():
    return render_template("index.html")


@app.route('/first',methods=['POST'])
def first():
    keyword=request.form.get('keyword')
    # page = requests.get("https://www.google.dz/search?q="+keyword)
    # soup = BeautifulSoup(page.content,"html.parser")
    # #links = soup.findAll("a")
    # List=[]
    # for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    #     List.append(re.split(":(?=http)",link["href"].replace("/url?q=","")))
    # r=requests.post('http://127.0.0.1:5000/pdfDownloader',json={'Result':List})
    # return r.text
    # #return jsonify({'Result':List,'keyword':keyword})

    res = requests.get('https://google.com/search?q='+keyword)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    links = soup.select('div#main > div > div > div > a')
	#print(links)
	# chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	# webbrowser.register('chrome', 1,webbrowser.BackgroundBrowser(chrome_path))
	# webbrowser.get('chrome').open_new_tab('https://google.com' + links[0].get('href'))
    List=[]
    tab_counts = min(30, len(links))
    for i in range(tab_counts):
		# chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
		# webbrowser.register('chrome', 1,webbrowser.BackgroundBrowser(chrome_path))
		# webbrowser.get('chrome').open_new_tab('https://google.com' + links[i].get('href'))
	    List.append('https://google.com' + links[i].get('href'))
    r=requests.post('http://127.0.0.1:5000/pdfDownloader',json={'Result':List,'keyword':keyword})
    return r.text

@app.route('/pdfDownloader',methods=['POST'])
def pdfDownloader():
    res=request.get_json()
    config = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltox\\bin\\wkhtmltopdf.exe")
    pdfkit.from_url(res['Result'][1],res['keyword']+'.pdf',configuration=config)
    return "True"

if __name__ == '__main__':
    app.run()
