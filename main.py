from website import create_app 
app = create_app()

if __name__ == "__main__":
    create_app
    app.run(debug=True)

import os

template_dir = os.path.join(os.path.dirname(base.html), 'Templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)
