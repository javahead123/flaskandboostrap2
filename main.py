from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash





app = Flask(__name__, static_url_path='')



@app.route('/', methods=['POST', 'GET'])
def hello_world():
  if request.method == 'POST':
    print "Post request received"
  if request.method == 'GET':
    print "Get request received"
  return render_template('index.html')

@app.route('/index')
def get_static_index():
  return app.send_static_file('index.html')



if __name__ == '__main__':
  app.run(debug=True)
