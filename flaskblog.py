from flask import Flask, render_template, url_for
app = Flask(__name__)

#defined a list of dictionaries 1966
posts = [
{
	'author' : 'Chyngyzkan Samatov',
	'title' : 'Blog Post #1',
	'content' : 'TEST',
	'date_posted' : 'In Sha Allah God Willings'
},
{
	'author' : 'Saltanat Ruslanova',
	'title' : 'Blog Post #2',
	'content' : 'TEST',
	'date_posted' : 'In Sha Allah God Willings'
}

]


#basic routes  
@app.route("/") 
@app.route("/home")
def home(): #declared a function with no parameters
    return render_template('home.html', posts=posts)

#
@app.route("/about")
def about(): #defined one more function with no parameters
    return render_template('about.html', title='About')

#
if __name__ == '__main__':
	app.run(debug=True)
