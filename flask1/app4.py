from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':# als er iets gestuurt is met post doe dit
        date_string = request.form['date']
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        day_as_number = date_object.weekday()
        days_of_week_array = ['Maandag', 'Dinsdag', 'Woensdag', 'Vrijdag', 'Zaterdag', 'Zondag']
        day_of_week = days_of_week_array[day_as_number]
        return render_template('result.html', day_of_week=day_of_week)# stuur naar result
    return render_template('index3.html')#stuur naar index

if __name__ == '__main__':
    app.run(debug=True)
