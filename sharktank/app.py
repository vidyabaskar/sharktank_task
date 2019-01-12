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
        cur = mysql.get_db().cursor()
        cat = request.form.getlist('searchcategory')
        input = request.form['searchfield']
        cat2 = request.form.getlist('searchcategory2')

        if cat:
            cat = cat[0]
        else:
            cat = ""

        if cat2:
            cat2 = cat2[0]
        else:
            cat2 = ""

        if cat:
            if cat == 'season':
                if input == '1':
                    cat = 'season01'
                elif input == '2':
                    cat = 'season02'
                elif input == '3':
                    cat = 'season03'
                elif input == '4':
                    cat = 'season04'
                elif input == '5':
                    cat = 'season05'
                elif input == '6':
                    cat = 'season06'
                else:
                    abort(404)
                cur.execute('''SELECT * FROM ''' + cat + ' natural join companydetails')
                rs = cur.fetchall()

            elif cat == 'cname':
                cur.execute('''SELECT * FROM season01 s natural join companydetails where s.company = \'''' + input + '\'')
                rs = cur.fetchall()
                if rs:
                    print(rs)
                else:
                    cur.execute('''SELECT * FROM season02 s natural join companydetails where s.company = \'''' + input + '\'')
                    rs = cur.fetchall()
                    print(rs)
                if rs:
                    print(rs)
                else:
                    cur.execute('''SELECT * FROM season03 s natural join companydetails where s.company = \'''' + input + '\'')
                    rs = cur.fetchall()
                if rs:
                    print(rs)
                else:
                    cur.execute('''SELECT * FROM season04 s natural join companydetails where s.company = \'''' + input + '\'')
                    rs = cur.fetchall()
                if rs:
                    print(rs)
                else:
                    cur.execute('''SELECT * FROM season05 s natural join companydetails where s.company = \'''' + input + '\'')
                    rs = cur.fetchall()
                if rs:
                    print(rs)
                else:
                    cur.execute('''SELECT * FROM season06 s natural join companydetails where s.company = \'''' + input + '\'')
                    rs = cur.fetchall()

            elif cat == 'deal' or cat == 'category' or cat == 'numsharks':
                t = list()
                cur.execute('''SELECT * FROM season01 s natural join companydetails where s.''' + cat +'''   = \'''' + input + '\'')
                rs = cur.fetchall()
                cur.execute('''SELECT * FROM season02 s natural join companydetails where s.''' + cat +'''   = \'''' + input + '\'')
                r = cur.fetchall()
                r = list(r)
                t.append(r)
                cur.execute('''SELECT * FROM season03 s natural join companydetails where s.''' + cat +'''   = \'''' + input + '\'')
                r = cur.fetchall()
                r = list(r)
                t.append(r)
                cur.execute('''SELECT * FROM season04 s natural join companydetails where s.''' + cat +'''   = \'''' + input + '\'')
                r = cur.fetchall()
                r = list(r)
                t.append(r)
                cur.execute('''SELECT * FROM season05 s natural join companydetails where s.''' + cat +'''   = \'''' + input + '\'')
                r = cur.fetchall()
                r = list(r)
                t.append(r)
                cur.execute('''SELECT * FROM season06 s natural join companydetails where s.''' + cat +'''   = \'''' + input + '\'')
                r = cur.fetchall()
                r = list(r)
                t.append(r)
                rs = list(rs)
                for i in t:
                    for j in i:
                        rs.append(j)
                rs = tuple(rs)

            elif cat == 'gender':
                t = list()
                cur.execute('''SELECT * FROM season01 s natural join companydetails c where c.''' + cat +'''   = \'''' + input + '\'')
                rs = cur.fetchall()
                cur.execute('''SELECT * FROM season02 s natural join companydetails c where c.''' + cat +'''   = \'''' + input + '\'')
                r = cur.fetchall()
                r = list(r)
                t.append(r)
                cur.execute('''SELECT * FROM season03 s natural join companydetails c where c.''' + cat +'''   = \'''' + input + '\'')
                r = cur.fetchall()
                r = list(r)
                t.append(r)
                cur.execute('''SELECT * FROM season04 s natural join companydetails c where c.''' + cat +'''   = \'''' + input + '\'')
                r = cur.fetchall()
                r = list(r)
                t.append(r)
                cur.execute('''SELECT * FROM season05 s natural join companydetails c where c.''' + cat +'''   = \'''' + input + '\'')
                r = cur.fetchall()
                r = list(r)
                t.append(r)
                cur.execute('''SELECT * FROM season06 s natural join companydetails c where c.''' + cat +'''   = \'''' + input + '\'')
                r = cur.fetchall()
                r = list(r)
                t.append(r)
                rs = list(rs)
                for i in t:
                    for j in i:
                        rs.append(j)
                rs = tuple(rs)


        return render_template('results.html',result=rs)
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

    else:
       abort(404)



if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 8100))
    app.run(host=host, port=port)
