from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')
@app.route('/play/<int:num>') #stacking routes

@app.route('/play/<int:num>/<color>') 
#as i was creating adding to this, it was losing the one before (requiring all selectors) 
#stacking routes above solved this issue but they need parameters, so added default values so that I would not get an error
def play(num=3, color='pink'):
#added default values to my classes as 1 and pink so unless I change those, it default to those settings
    return render_template('index.html', num = num, color = color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

