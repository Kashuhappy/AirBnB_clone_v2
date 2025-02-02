<!DOCTYPE html>

<html lang="en">



<head>

    <title>Holberton School</title>
    

    
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/3-footer.css') }}">
    
    <link rel="stylesheet" href="{{ url_for('static', filename='../static/styles/3-header.css') }}">
    
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/4-common.css') }}">
    
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/6-filters.css') }}">
    
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/8-places.css') }}">
    
    <link rel="icon"
    
        href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png">
        
</head>



<body>

    <header>
    
        <div class="logo"></div>
        
    </header>
    
    <div class="container">
    
        <section class="filters">
        
            <div class="locations">
            
                <h3>States</h3>
                
                <h4>&nbsp;</h4>
                
                <div class="popover">
                
                    {% for state in states|sort(attribute="name") %}
                    
                    <h2>
                    
                        {{ state|attr('name') }}
                        
                    </h2>
                    
                    <ul>
                    
                        {% for city in state|attr("cities")|sort(attribute="name") %}
                        
                        <li>{{ city|attr('name')}}</li>
                        
                        {% endfor %}
                        
                    </ul>
                    
                    {% endfor %}
                    
                </div>
                
            </div>
            
            <div class="amenities">
            
                <h3>Amenity</h3>
                
                <h4>&nbsp;</h4>
                
                <div class="popover">
                
                    <ul>
                    
                        {% for ameniti in amenities|sort(attribute="name") %}
                        
                        <li>{{ ameniti|attr('name') }}</li>
                        
                        {% endfor %}
                        
                    </ul>
                    
                </div>
                
            </div>
            
            <div class="f_button">
            
                <button class="s_button">Search</button>
                
            </div>
            
        </section>
        
    </div>
    
    <footer>
    
        <p>Holberton School</p>
        
    </footer>
    
</body>



</html>
