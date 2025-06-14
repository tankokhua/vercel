from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!!!'

@app.route('/result')
def result():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template("result.html", result = dict)

@app.route('/about')
def about():
    return 'About'

@app.route('/gethints', methods=['GET', 'POST'])
def HintsHandler():
    _wordlength = request.form.get("wordlength").strip()
    _letters    = request.form.get("letters").lower().replace(' ', '', 12)
    _filters    = request.form.get("filters").lower().replace(' ', '', 12)
    _answers = "No valid answers."
    if re.search(r'\d', _wordlength) and 3<=int(_wordlength)<=9:
       try:
          words = " ".join(open("w%s" % _wordlength).readlines()).split()
          filterlist = ''.join(set(_letters))
   
          cnt=0
          _answers = ""
          for word in words:
              if not re.search(r'[^%s]' % filterlist, word):
                 skip = False
                 for ch in filterlist:
                   if word.count(ch)>_letters.count(ch):
                      skip = True
                      break
                 if skip:
                    continue
                 if len(_filters)==int(_wordlength) and not re.search(r'%s' % _filters, word):
                    continue
                 cnt+=1
                 _answers += " %s" % word
          if cnt==0:
             _answers = "No valid answers."
       except:
          _answers = "Error executing scrpt."
    else:
       _answers = "Wordlength must be between 3 to 9."

    logging.info("wordlength %s [%s] [%s]" % (_wordlength, _letters, _answers))
    return render_template("answers.htm", answers=_answers)

@app.route('/4p1w', methods=['GET', 'POST'])
def MainHandler():
    return render_template("index.htm", wordlength="", letters="", filters="")
