from flask import Flask, render_template, url_for, request
app=Flask(__name__)
@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('home.html')
    if request.method=='POST':

        from sklearn.datasets import load_iris
        from sklearn.linear_model import LogisticRegression
        X, y = load_iris(return_X_y=True)
        clf = LogisticRegression(solver='liblinear',random_state=0, C=50).fit(X, y)
        #clf = LogisticRegression(random_state=0).fit(X, y)

        X1=float(request.form['Sepal_length']) ;     X2=float(request.form['Sepal_width'])
        X3=float(request.form['Petal_length']) ;     X4=float(request.form['Petal_width'])

        x_test=([X1,X2,X3,X4],)
        irisCategory=clf.predict(x_test) ;      CateList=['setota','versicolor','virginica']
        result="예측품종은 " + CateList[irisCategory[0]] + "임"
        return render_template('home.html', result=result)

if __name__=='__main__':
    app.run(debug=True)
