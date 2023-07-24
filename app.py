from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_mail import Mail
from werkzeug.utils import secure_filename
from PIL import Image
import os
import re


app = Flask(__name__)
app.secret_key = 'ABC'

app.secret_key='cvbuilder'

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'your_email,
    MAIL_PASSWORD = 'your_password',
)
mail=Mail(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'S#@5ahil1P'
app.config['MYSQL_DB'] = 'cvbuilder'

mysql=MySQL(app)

# Configure file upload
app.config['UPLOAD_FOLDER'] = 'static/passport'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



# for error page rendering
@app.route('/error')
def error():
    return render_template('error.html')

# for index page rendering
@app.route('/')
def index():
   return render_template('index.html')

# for home page rendering
@app.route('/home')
def home():
    if 'name' in session :
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM templates')
        temp=cursor.fetchall()
        return render_template('home.html',temp=temp)
    else:
        return redirect('/')

# for about page rendering
@app.route('/about')
def about():
    if 'name' in session :
        return render_template('about.html')
    else:
        return redirect('/')

@app.route('/lol/<string:name>')
def lol(name):
    if 'name' in session :
        session["template"]=name
        return redirect('/test')
    else:
        return redirect('/')


# users details input form
@app.route('/test', methods=['POST','GET'])
def test():
    userid=int(session['userid'])
    # srno=1
    if 'name' in session:
        skills=''
        languages=''
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('SELECT * FROM skills')
        skills=cursor.fetchall()

        cursor.execute('SELECT * FROM languages')
        languages=cursor.fetchall()
        
        if request.method == 'POST':
            # personal detail

            
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                filename = None
            session['name']=request.form['name']
            session['email1']=request.form['email']
            session['profession']=request.form['profession']
            session['dob']=request.form['dob']
            session['objective']=request.form['objective']
            session['city']=request.form['city']
            session['country']=request.form['country']
            session['pin']=request.form['pin']
            session['phone']=request.form['phone']


            # work history
            # 1
            session['job_title1']=request.form['job_title1']
            session['employer1']=request.form['employer1']
            session['work_city1']=request.form['work_city1']
            session['work_country1']=request.form['work_country1']
            session['start_date1']=request.form['start_date1']
            session['end_date1']=request.form['end_date1']

            # 2
            # session['job_title2']=request.form['job_title2']
            # session['employer2']=request.form['employer2']
            # session['work_city2']=request.form['work_city2']
            # session['work_country2']=request.form['work_country2']
            # session['start_date2']=request.form['start_date2']
            # session['end_date2']=request.form['end_date2']


            # project detail
            # 1
            session['proj_title1']=request.form['proj_title1']
            session['proj_des1']=request.form['proj_des1']
            session['pro_start1']=request.form['pro_start1']
            session['pro_end1']=request.form['pro_end1']

            # 2
            # session['proj_title2']=request.form['proj_title2']
            # session['proj_des2']=request.form['proj_des2']
            # session['pro_start2']=request.form['pro_start2']
            # session['pro_end2']=request.form['pro_end2']


            # education detail
            # SSC 
            # session['school_name']=request.form['school_name']
            # session['school_loc']=request.form['school_loc']
            # session['school_per']=request.form['school_per']
            # session['school_board']=request.form['school_board']
            # session['school_start']=request.form['school_start']
            # session['school_end']=request.form['school_end']

            # HSC
            session['college_name']=request.form['college_name']
            session['college_loc']=request.form['college_loc']
            session['college_per']=request.form['college_per']
            session['field_study']=request.form['field_study']
            session['college_start']=request.form['college_start']
            session['college_end']=request.form['college_end']

            # degree
            session['deg_clg']=request.form['deg_clg']
            session['deg_loc']=request.form['deg_loc']
            session['deg_per']=request.form['deg_per']
            session['deg_std_fld']=request.form['deg_std_fld']
            session['deg_start']=request.form['deg_start']
            session['deg_end']=request.form['deg_end']

            # post degree
            session['post_deg_clg']=request.form['post_deg_clg']
            session['post_deg_loc']=request.form['post_deg_loc']
            session['post_deg_per']=request.form['post_deg_per']
            session['post_deg_std_fld']=request.form['post_deg_std_fld']
            session['post_deg_start']=request.form['post_deg_start']
            session['post_deg_end']=request.form['post_deg_end']

            # skill
            session['hidden_skills']=request.form['hidden_skills']


            # languages
            session['hidden_langs']=request.form['hidden_langs']


            # arranging the session data to variable to store in database

            name=session['name']
            email1=session['email1']
            profession=session['profession']
            dob=session['dob']
            objective=session['objective']
            city=session['city']
            country=session['country']
            pin=session['pin']
            phone=session['phone']

            job_title1=session['job_title1']
            employer1=session['employer1']
            work_city1=session['work_city1']
            work_country1=session['work_country1']
            start_date1=session['start_date1']
            end_date1=session['end_date1']

            # job_title2=session['job_title2']
            # employer2=session['employer2']
            # work_city2=session['work_city2']
            # work_country2=session['work_country2']
            # start_date2=session['start_date2']
            # end_date2=session['end_date2']

            proj_title1=session['proj_title1']
            proj_des1=session['proj_des1']
            pro_start1=session['pro_start1']
            pro_end1=session['pro_end1']

            # proj_title2=session['proj_title2']
            # proj_des2=session['proj_des2']
            # pro_start2=session['pro_start2']
            # pro_end2=session['pro_end2']

            # school_name=session['school_name']
            # school_loc=session['school_loc']
            # school_per=session['school_per']
            # school_board=session['school_board']
            # school_start=session['school_start']
            # school_end=session['school_end']

            college_name=session['college_name']
            college_loc=session['college_loc']
            college_per=session['college_per']
            field_study=session['field_study']
            college_start=session['college_start']
            college_end=session['college_end']

            deg_clg=session['deg_clg']
            deg_loc=session['deg_loc']
            deg_per=session['deg_per']
            deg_std_fld=session['deg_std_fld']
            deg_start=session['deg_start']
            deg_end=session['deg_end']

            post_deg_clg=session['post_deg_clg']
            post_deg_loc=session['post_deg_loc']
            post_deg_per=session['post_deg_per']
            post_deg_std_fld=session['post_deg_std_fld']
            post_deg_start=session['post_deg_start']
            post_deg_end=session['post_deg_end']

            hidden_skills=session['hidden_skills']
            hidden_langs=session['hidden_langs']

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # cursor.execute('INSERT INTO resume_detail (name, email, profession, objective, city, country, pin, phone, job_title1, employer1, work_city1, work_country1, start_date1,end_date1, job_title2, employer2 ,work_city2, work_country2, start_date2, end_date2, proj_title1, proj_des1,pro_start1, pro_end1, proj_title2, proj_des2, pro_start2, pro_end2, school_name, school_loc, school_per, school_board, school_start, school_end, college_name, college_loc, college_per, field_study, college_start, college_end, deg_clg, deg_loc, deg_per, deg_std_fld, deg_start, deg_end, post_deg_clg, post_deg_loc, post_deg_per, post_deg_std_fld, post_deg_start, post_deg_end, skills, languages ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (name, email, profession, objective, city, country, pin, phone, job_title1, employer1, work_city1, work_country1, start_date1,end_date1, job_title2, employer2 ,work_city2, work_country2, start_date2, end_date2, proj_title1, proj_des1,pro_start1, pro_end1, proj_title2, proj_des2, pro_start2, pro_end2, school_name, school_loc, school_per, school_board, school_start, school_end, college_name, college_loc, college_per, field_study, college_start, college_end, deg_clg, deg_loc, deg_per, deg_std_fld, deg_start, deg_end, post_deg_clg, post_deg_loc, post_deg_per, post_deg_std_fld, post_deg_start, post_deg_end, [hidden_skills], [hidden_langs] ,) )

            cursor.execute('INSERT INTO resume_detail (name, email, profession, objective, city, country, pin, phone, job_title1, employer1, work_city1, work_country1, start_date1,end_date1, proj_title1, proj_des1,pro_start1, pro_end1, college_name, college_loc, college_per, field_study, college_start, college_end, deg_clg, deg_loc, deg_per, deg_std_fld, deg_start, deg_end, post_deg_clg, post_deg_loc, post_deg_per, post_deg_std_fld, post_deg_start, post_deg_end, skills, languages, dob, image,userid ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (name, email1, profession, objective, city, country, pin, phone, job_title1, employer1, work_city1, work_country1, start_date1,end_date1, proj_title1, proj_des1,pro_start1, pro_end1, college_name, college_loc, college_per, field_study, college_start, college_end, deg_clg, deg_loc, deg_per, deg_std_fld, deg_start, deg_end, post_deg_clg, post_deg_loc, post_deg_per, post_deg_std_fld, post_deg_start, post_deg_end, [hidden_skills], [hidden_langs], dob , filename, userid) )

            mysql.connection.commit()
            cursor.close()
            return redirect('/template')
        return render_template('test.html', skills=skills, languages=languages)
    else:
        return redirect('/')

# templates render from fteching data from database
@app.route('/template')
def template():
    if 'name' in session :
        name=str(session["name"])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT image, name, email, profession, dob, objective, city, country, pin, phone FROM resume_detail WHERE name=%s ORDER BY srno DESC LIMIT 1",(name,))
        personal=cursor.fetchone()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT job_title1, employer1, work_city1, work_country1, start_date1, end_date1 FROM resume_detail WHERE name=%s ORDER BY srno DESC LIMIT 1",(name,))
        work=cursor.fetchone()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT proj_title1, proj_des1, pro_start1, pro_end1 FROM resume_detail WHERE name=%s ORDER BY srno DESC LIMIT 1",(name,))
        project=cursor.fetchone()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT college_name, college_loc, college_per, field_study, college_start, college_end FROM resume_detail WHERE name=%s ORDER BY srno DESC LIMIT 1",(name,))
        clg=cursor.fetchone()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT deg_clg, deg_loc, deg_per, deg_std_fld, deg_start, deg_end FROM resume_detail WHERE name=%s ORDER BY srno DESC LIMIT 1",(name,))
        deg_clg=cursor.fetchone()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT post_deg_clg, post_deg_loc, post_deg_per, post_deg_std_fld, post_deg_start, post_deg_end FROM resume_detail WHERE name=%s ORDER BY srno DESC LIMIT 1",(name,))
        post_deg_clg=cursor.fetchone()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(" SELECT skills FROM resume_detail WHERE name=%s ORDER BY srno DESC LIMIT 1",(name,))
        skills=cursor.fetchone()
        print(skills)
        newlist=list(skills.items())
        print(newlist)
        original_set=newlist
        skill_list=original_set[0][1].split(',')
        new_tuple=(original_set[0][0],skill_list)
        print(skill_list)
        for skill in skill_list:
            print(skill)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(" SELECT languages FROM resume_detail WHERE name=%s ORDER BY srno DESC LIMIT 1",(name,))
        languages=cursor.fetchone()
        print(languages)
        new_list_lang=list(languages.items())
        print(new_list_lang)
        original_set_lang=new_list_lang
        lang_list=original_set_lang[0][1].split(',')
        new_tuple_lang=(original_set_lang[0][0],lang_list)
        print(lang_list)
        for lang in lang_list:
            print(lang)
        template=str(session["template"])
        return render_template(''+template+'.html',personal=personal, work=work, project=project, clg=clg, deg_clg=deg_clg, post_deg_clg=post_deg_clg, skill_list=skill_list, lang_list=lang_list)
    else:
        return redirect('/')


# contact us or query
@app.route('/contact',methods=['POST','GET'])
def contact():
    if 'name' in session :
        if request.method=='POST':
          #Add entry to the database
          name = request.form['name']
          email = request.form['email']
          phone_num = request.form['phone_num']
          msg = request.form['msg']
          cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
          cursor.execute('INSERT INTO contacts values (NULL,%s,%s,%s,%s)', (name,email,phone_num,msg,) )
          mysql.connection.commit()
          mail.send_message('Received New Feedback !!!', 
                               sender=email,
                               recipients=['amaanalamgirshaikh@gmail.com'],
                               body = name + "\n" +msg + "\n" +phone_num,
                               )
        return render_template('contact.html')
    else:
        return redirect('/')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)


# login from
@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return redirect('/home') 
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)

# register form
@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()
            mail.send_message('Here is your Login Details.', 
                           sender='sahilvanarse4@gmail.com',
                           recipients=[email],
                           # body = userName + "\n" +email + "\n" +password,
                           body = "Dear " +userName+"," "\n"
                                        "Your new Account has been created, Welcome to the AP Resume!" "\n"
                                        "From now on please log in to your account using your " +email+ " email and your password " +password+"."
                           )
            mesage = 'You have successfully registered. Login details sent to your given E-mail !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

# logout template
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    session.pop('name', None)
    return redirect('/')

# dashboard template
@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    # session['user']=''
    if 'user' in session and session['user'] == 'amanshaikh':
        # return "<a href='/fun/skills'>skills</a><a href='/fun/languages'>language</a>"
        return redirect('/fun/skills')
    if 'user' in session and session['user'] == 'pratik':
        # return "<a href='/fun/skills'>skills</a><a href='/fun/languages'>language</a>"
        return redirect('/fun/skills')
    if request.method=='POST':
        username = request.form['uname']
        userpass = request.form['pass']
        session['user'] = username
        session['upass'] = userpass
    
        if username == 'amanshaikh' and userpass == 'amanshaikh' or username == 'pratik' and userpass == 'pratik':
            # return "<a href='/fun/skills'>skills</a><a href='/fun/languages'>language</a>"
            return redirect('/fun/skills')
        else:
            return redirect(url_for('error'))
    else:
        return render_template('adminlogin.html')


@app.route('/fun/<string:cat>',methods=['POST','GET'])
def fun(cat):
    if 'option' in session:
        session.pop('option')
    session['option']=cat
    if 'user' in session and session["option"]=="languages":
        if session['user'] == 'amanshaikh' or session['user'] == 'pratik':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM languages')
            languages = cursor.fetchall()
            # print(list(skills))
            return render_template('b6index.html',data=languages,name=cat)

    if 'user' in session and session["option"]=="skills":
        if session['user'] == 'amanshaikh' or session['user'] == 'pratik':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM skills')
            skills = cursor.fetchall()
            # print(list(skills))
            return render_template('b6index.html',data=skills,name=cat)

    if 'user' in session and session["option"]=="userinfo":
        if session['user'] == 'amanshaikh' or session['user'] == 'pratik':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM user')
            skills = cursor.fetchall()
            # print(list(skills))
            return render_template('b6index.html',data=skills,name=cat)
    else:
        return render_template('adminlogin.html')


@app.route('/add_student', methods =['POST'])
def add_student():
    option=session["option"]
    if request.method=='POST' and session["option"] == "skills":
        name = request.form['name']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO skills (skills) VALUES ( %s)",(name,))
        # cursor.execute(query)
        mysql.connection.commit()
        flash('Skill added successfully')
        return redirect('/fun/'+option+'')

    if request.method=='POST' and session["option"] == "languages":
        name = request.form['name']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO languages (languages) VALUES ( %s)",(name,))
        # cursor.execute(query)
        mysql.connection.commit()
        flash('language added successfully')
        return redirect('/fun/'+option+'')



@app.route('/edit/<sid>', methods = ['POST', 'GET'])
def get_student(sid):
    option=session["option"]
    if session["option"]=="skills":
        cursor = mysql.connection.cursor()
        query='SELECT * FROM skills WHERE id = %s'
        cursor.execute(query,(sid,))
        #cursor.execute('SELECT * FROM clg.studentdata WHERE sid = %s', (sid))
        data = cursor.fetchall()
        cursor.close()
        print(data[0])
        return render_template('b6edit.html', student = data)

    if session["option"]=="languages":
        cursor = mysql.connection.cursor()
        query='SELECT * FROM languages WHERE id = %s'
        cursor.execute(query,(sid,))
        #cursor.execute('SELECT * FROM clg.studentdata WHERE sid = %s', (sid))
        data = cursor.fetchall()
        cursor.close()
        print(data[0])
        return render_template('b6edit.html', student = data)
 
@app.route('/update/<nid>', methods=['POST'])
def update_student(nid):
    option=session["option"]
    if request.method == 'POST' and session["option"] == "skills":
        name = request.form['name']
        cursor = mysql.connection.cursor()
        query='UPDATE skills SET skills=%s where id=%s'
        cursor.execute(query,(name,nid))
        flash('Skill Updated Successfully')
        mysql.connection.commit()
        return redirect('/fun/'+option+'')

    if request.method == 'POST' and session["option"] == "languages":
        name = request.form['name']
        cursor = mysql.connection.cursor()
        query='UPDATE languages SET languages=%s where id=%s'
        cursor.execute(query,(name,nid))
        flash('language Updated Successfully')
        mysql.connection.commit()
        return redirect('/fun/'+option+'')

@app.route('/delete/<nid>', methods = ['POST','GET'])
def delete_student(nid):
    option=session["option"]
    if session["option"] == "skills":
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM skills WHERE id = {0}'.format(nid))
        #query='DELETE FROM clg.studentdata WHERE sid = %s'
        #cursor.execute(query,(nid))
        mysql.connection.commit()
        flash('Skill Removed Successfully')
        return redirect('/fun/'+option+'')
    
    if session["option"] == "languages":
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM languages WHERE id = {0}'.format(nid))
        #query='DELETE FROM clg.studentdata WHERE sid = %s'
        #cursor.execute(query,(nid))
        mysql.connection.commit()
        flash('language Removed Successfully')
        return redirect('/fun/'+option+'')

 

@app.route('/adminlogout')
def adminlogout():
    session.pop('loggedin', None)
    session.pop('user', None)
    # session.pop('email', None)
    # session.pop('name', None)
    return redirect('/')





if __name__ == '__main__':
   app.run(debug = True)












