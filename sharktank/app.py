from flask import Flask,request,abort,jsonify, render_template
import os
from flaskext.mysql import MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'sharktank'
mysql = MySQL(app)
CORS(app)



@app.route('/', methods=['GET' , 'POST'])
def search():

    if request.method == 'GET':
        return render_template('search.html')

    elif request.method == 'POST':
        cname = request.form['cname']
        season = request.form.getlist('season')
        cat = request.form.getlist('category')
        deal = request.form.getlist('deal')
        nosharks = request.form.getlist('nosharks')
        sharks = request.form.getlist('sharks')
        gender = request.form.getlist('gender')
        amount = request.form['amount']

        if season:
            season = season[0]
        else:
            season = ""
        if cat:
            cat = cat[0]
        else:
            cat = ""
        if deal:
            deal = deal[0]
        else:
            deal = ""
        if nosharks:
            nosharks = nosharks[0]
        else:
            nosharks = ""
        if gender:
            gender = gender[0]
        else:
            gender = ""
        if sharks:
            sharks = sharks[0]
        else:
            sharks = ""

        data = {
            'cname': cname, 'season': season, 'category': cat, 'deal': deal, 'numsharks': nosharks, 'sharks': sharks,
            'amount': amount
        }
        print(data)
        cur = mysql.get_db().cursor()

        
        # Compnay name:
        # Season:
        # Episode premiered:
        # Entrepreneur Gender:
        # Deal status:
        # Number of Inverstors:
        # Amount:
        # Equity:
        # Amount per shark:
        # Total value:

        if cname:
            cur.execute('''SELECT * FROM season01 natural join companydetails WHERE COMPANY = \''''+ cname + '\'')
            rs = cur.fetchall()
            print(rs)
            if rs == ():
                cur.execute('''SELECT * FROM season02 WHERE COMPANY = \'''' + cname + '\'')
                rs = cur.fetchall()
            if rs == ():
               cur.execute('''SELECT * FROM season03 WHERE COMPANY = \'''' + cname + '\'')
                rs = cur.fetchall()
            if rs == ():
                cur.execute('''SELECT * FROM season04 WHERE COMPANY = \'''' + cname + '\'')
                rs = cur.fetchall()
            if rs == ():
                cur.execute('''SELECT * FROM season05 WHERE COMPANY = \'''' + cname + '\'')
                rs = cur.fetchall()
            if rs == ():
                cur.execute('''SELECT * FROM season06 WHERE COMPANY = \'''' + cname + '\'')
                rs = cur.fetchall()
            for i in rs:
                if i[3] == 'Yes'

            else:
                return render_template('results.html',result=rs)

        elif season:
            if season == '1':
                cur.execute('''SELECT * FROM season01''')
                rs = cur.fetchall()
                rs = list(rs)
                r = []
                for i in rs:
                    i = list(i)
                    i.insert(1,season)
                    i = tuple(i)
                    r.append(i)
                rs = tuple(r)
                print(rs)
                return render_template('results.html', result=rs)

            elif season == '2':
                cur.execute('''SELECT * FROM season02''')
                rs = cur.fetchall()
                rs = list(rs)
                r = []
                for i in rs:
                    i = list(i)
                    i.insert(1,season)
                    i = tuple(i)
                    r.append(i)
                rs = tuple(r)
                print(rs)
                return render_template('results.html', result=rs)

            elif season == '3':
                cur.execute('''SELECT * FROM season03''')
                rs = list(rs)
                r = []
                for i in rs:
                    i = list(i)
                    i.insert(1,season)
                    i = tuple(i)
                    r.append(i)
                rs = tuple(r)
                print(rs)
                rs = cur.fetchall()
                return render_template('results.html', result=rs)

            elif season == '4':
                cur.execute('''SELECT * FROM season04''')
                rs = list(rs)
                r = []
                for i in rs:
                    i = list(i)
                    i.insert(1,season)
                    i = tuple(i)
                    r.append(i)
                rs = tuple(r)
                print(rs)
                rs = cur.fetchall()
                return render_template('results.html', result=rs)

            elif season == '5':
                cur.execute('''SELECT * FROM season05 ''')
                rs = list(rs)
                r = []
                for i in rs:
                    i = list(i)
                    i.insert(1,season)
                    i = tuple(i)
                    r.append(i)
                rs = tuple(r)
                print(rs)
                rs = cur.fetchall()
                return render_template('results.html', result=rs)

            elif season == '6':
                cur.execute('''SELECT * FROM season06''')
                rs = list(rs)
                r = []
                for i in rs:
                    i = list(i)
                    i.insert(1,season)
                    i = tuple(i)
                    r.append(i)
                rs = tuple(r)
                print(rs)
                rs = cur.fetchall()
                return render_template('results.html', result=rs,**data)
        elif deal:
            if deal == 'Yes':
                cur.execute('''SELECT * FROM dealproject''')
                rs = cur.fetchall()
        else:
            rs = "Error! No input selected"
            print(rs)
            abort(404)

    else:
       abort(404)



if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 8100))
    app.run(host=host, port=port)
