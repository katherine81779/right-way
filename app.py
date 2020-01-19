from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# importing API here

# private variables here 
    # input from the user
brand = ""
make = ""
year = ""

# homepage link
@app.route("/")
def redir():
    return render_template('index.html')

# go to about page
@app.route("/about")
def goToAbout():
    return render_template('about.html')

@app.route("/car", methods = ['POST', 'GET'])
def storeCarInfo():
    global brand
    global make
    global year

    if request.method == 'POST':
        brand = request.form['brand']
        make = request.form['make']
        year = request.form['year']

        return redirect('/question')

# QUESTIONS
questions = ["q1", "q2","q3","q4"] # add to this later
q_num = 0 # keeps track of the q number we're on
answers = {}

# go to next question: gets called when you submit answer to each q
@app.route("/question")
def getNextQuestion():
    if (q_num < len(questions)):
        return render_template(questions[q_num] + ".html")
    else: # go to results page
        return render_template('report.html')  

# input/form data collection for the question
@app.route("/inputAnswer", methods = ['POST', 'GET'])
def storeAnswer():
    global q_num
    if request.method == 'POST':
        
        # store answer in answer dictionary
        answer = request.form['answer']
        answers[q_num] = answer

        # increment question index!
        q_num += 1
        # direct to next question
        return redirect("/question")

# method/algorithm to calculate the results?



# main function
if __name__ == "__main__":
    app.run()

