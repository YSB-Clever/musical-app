from website import create_app 
app = create_app()

if __name__ == "__main__":
    create_app
    app.run(debug=True)

template_dir = os.path.join(os.path.dirname(__login.html__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)
