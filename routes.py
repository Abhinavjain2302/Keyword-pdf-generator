from flask import Flask,jsonify,request,render_template,send_from_directory
import requests
import re,os
import pdfkit
import bs4
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def form():
    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/getLinks',methods=['POST'])
def getLinks():
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
    List=[]
    tab_counts = min(30, len(links))
    for i in range(tab_counts):
	    List.append('https://google.com' + links[i].get('href'))
    requests.post('http://127.0.0.1:5000/pdfDownloader',json={'Result':List,'keyword':keyword})
    return render_template('download.html')
    

@app.route('/pdfDownloader',methods=['POST'])
def pdfDownloader():
    res=request.get_json()
    path_new=os.getcwd()+'/'+res['keyword']
    if os.path.isdir(path_new)==False:
        os.mkdir(path_new)
    
    config = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltox\\bin\\wkhtmltopdf.exe")
    for i in range(0,10):
        try:
            pdfkit.from_url(res['Result'][i],res['keyword']+'/'+res['keyword']+str(i)+'.pdf',configuration=config)
        except:
            # print("Trying another Link")
            continue
    return "True"

if __name__ == '__main__':
    app.run()
