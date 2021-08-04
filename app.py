from flask import Flask, request, render_template

app = Flask(__name__,static_url_path='/static')

def exceptionalZ(x,y):
    r=0
    try:
        r=x/y
    except ZeroDivisionError:
        return 0
    return x/y


def Percentage(marksObtained,totalMarks):
    per=0
    try:
        per=marksObtained/totalMarks
    except ZeroDivisionError:
        return 0
    return (marksObtained/totalMarks)*100
def exceptionalH(value):
    try:
        float(value)
        return float(value)
    except:
        print("Input must be a valid number. Non-special characters, commas and spaces are not accepted.")
        return -1
@app.route("/",methods=['GET','POST'])
def hello_world():
    error_message=''
    per=0
    fsobtained=0
    fstotal=0
    tsobtained=0
    tstotal=0
    if request.method=='POST':
        if 'm1' in request.form:
            m1=request.form.get('m1')
            m1=exceptionalH(m1)
            if 't1' in request.form:
                t1=request.form.get('t1')
                t1=exceptionalH(t1)
                if(t1>0):
                    fsobtained+=m1
                    fstotal+=t1

        if 'm2' in request.form:
            per=0
            m2=request.form.get('m2')
            m2=exceptionalH(m2)
            if 't2' in request.form:
                t2=request.form.get('t2')
                t2=exceptionalH(t2)
                if(t2>0):
                    fsobtained+=m2
                    fstotal+=t2

        if 'm3' in request.form:
            per=0
            m3=request.form.get('m3')
            m3=exceptionalH(m3)
            if 't3' in request.form:
                t3=request.form.get('t3')
                t3=exceptionalH(t3)
                if(t3>0):
                    fsobtained+=m3
                    fstotal+=t3

        if 'm4' in request.form:
            per=0
            m4=request.form.get('m4')
            m4=exceptionalH(m4)
            if 't4' in request.form:
                t4=request.form.get('t4')
                t4=exceptionalH(t4)
                if(t4>0):
                    tsobtained+=m4
                    tstotal+=t4

        if 'm5' in request.form:
            per=0
            m5=request.form.get('m5')
            m5=exceptionalH(m5)
            if 't5' in request.form:
                t5=request.form.get('t5')
                t5=exceptionalH(t5)
                if(t5>0):
                    tsobtained+=m5
                    tstotal+=t5
                

        if 'm6' in request.form:
            per=0
            m6=request.form.get('m6')
            m6=exceptionalH(m6)
            if 't6' in request.form:
                t6=request.form.get('t6')
                t6=exceptionalH(t6)
                if(t6>0):
                    tsobtained+=m6
                    tstotal+=t6
                    
        if 'm7' in request.form:
            per=0
            m7=request.form.get('m7')
            m7=exceptionalH(m7)
            if 't7' in request.form:
                t7=request.form.get('t7')
                t7=exceptionalH(t7)
                if(t7>0):
                    tsobtained+=m7
                    tstotal+=t7
    
   
    fsobtained=fsobtained/2
    fstotal=fstotal/2
    obtained=fsobtained+tsobtained
    total=fstotal+tstotal
    final=Percentage(obtained,total)
    return render_template("index.html",final=final)
if __name__=='__main__':
    app.run(debug=True)
