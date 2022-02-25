from website import create_app 
app = create_app()

if __name__ == "__main__":
    create_app
    app.run(debug=True)

env = Environment(loader=FileSystemLoader(searchpath='C:\website\Templates')
template = env.get_template('login.html')
