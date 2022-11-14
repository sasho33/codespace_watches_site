from website import create_app

# Starting application from init.py file

app=create_app()

if __name__ == '__main__':
     
    app.run(debug=True)