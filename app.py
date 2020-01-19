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
        average = getAverage(answers)
        textInfo = text(average)
        return render_template('report.html', score = average, displayText = textInfo)  

# input/form data collection for the question
@app.route("/inputAnswer", methods = ['POST', 'GET'])
def storeAnswer():
    global q_num
    if request.method == 'POST':
        
        # store answer in answer dictionary
        answer = request.form['answer']
        answers[q_num + 1] = answer

        # increment question index!
        q_num += 1
        # direct to next question
        return redirect("/question")

# method/algorithm to calculate the results?

# Rating goes from 1 - 10 
# BAD to GOOD

# function returns rating of mileage
# an old car with avery low mileage is BAD! FIX FOR ALGORITHM
def mileageRating( mileage ):
    if (mileage/100000 <= 10): return (10 - mileage/10000 + 1)
    else: return 1

# age is a huge factor when it comes to knowing the
# quality of the car, a two year old
def ageRating( age ):
    if (age <= 10): return 10 - age + 1
    else: return 1
    
# function returns last battery change
# batteries should be replaced after using 
# the car for three years
def batteryChange(years):
    if (years > 3): return 1
    elif (years >= 2.5 and years <=3): return 3.5
    elif (years < 2.5 and years < 2): return 6
    elif (years <= 1): return 10
    else: return 8

# function returns last oil change
# car depends on oil change based on year and age
# miles is MILES USED SINCE LAST OIL CHANGE
# this reflects if the owner of the car has been taking
# care of the car properly before selling it to you
def oilChange(age, miles):
    if (age >= 13): 
        # cars with the model 2008 or less should get
        # an oil change every 3000 miles
        if (miles < 2000): return 10
        elif (miles >= 5000): return 1
        else: return 5
    elif (age <= 13):
        if (miles < 75000): return 10
        elif (miles >= 10000): return 1
        else: return 5
    
# develops the final quality score for the car
def find_average(mileageRate, ageRate, batteryRate, oilRate):
    return (mileageRate + batteryRate + ageRate + oilRate)/4.0

# based on the average rate of the car, this will get displayed
# for the user!
def text(finalRate):
    good = "Congratulations! Based on what you have given us, we believe that the car is in good shape. \
            Given that the quality of the car is in good shape, now all you have to do is bargain it \
            for the right price. "
    medium_good = 'you are medium good'
    medium = 'you are medium'
    medium_bad = 'you are medium_bad'
    bad = 'you are doing bad'
    if (finalRate >= 1 and finalRate < 2):
        return bad
    elif (finalRate >= 2 and finalRate < 4):
        return medium_bad
    elif (finalRate >= 4 and finalRate < 6):
        return medium
    elif (finalRate <= 6 and finalRate < 8):
        return medium_good
    elif (finalRate >= 8 and finalRate < 10):
        return good

def getAverage(answers):
    indexNum = 0
    mRate = mileageRating(float(answers[1])) #mileage
    aRate = ageRating(float(answers[2])) #age
    bRate = batteryChange(float(answers[3])) #last battery change
    oRate = oilChange(ageRating(float(answers[2])), float(answers[4])) #last oil change 

    average = find_average(mRate, aRate, bRate, oRate) 
    return average



        

# main function
if __name__ == "__main__":
    app.run()

