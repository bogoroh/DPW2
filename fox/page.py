class Page():
    def __init__(self):
        self.__header = '''
<!DOCTYPE>
<html>
    <head>
            <title>Mike Taatgen's Fox</title>
            <link rel='stylesheet' href='css/main.css' />
            <link href='http://fonts.googleapis.com/css?family=Averia+Sans+Libre' rel='stylesheet' type='text/css'>
            <link href='http://fonts.googleapis.com/css?family=Roboto+Condensed' rel='stylesheet' type='text/css'>
</head>
    <body>
    '''
        self.__nav='''
        <h1> Animals </h1>
            <nav id="buttons">
				
                <a href='/?animal=0'><span>Red Panda</span></a>
                <a href='/?animal=1'><span>Great Auk</span></a>
                <a href='/?animal=2'><span>Leopard Cat</span></a>
            </nav>'''
        self.__content='''
         	<div id="wrapper">
            <h2>I am called {obj.name}</h2>
                <div class="col3">
                    <h3>My phylum is:</h3>
                    <p>{obj.phylum}</p>

                    <h3>My class is:</h3>
                    <p>{obj.cclass}</p>
              
                    <h3>My order is:</h3>
                    <p>{obj.order}</p>
                
                    <h3>My family is:</h3>
                    <p>{obj.family}</p>
               
                    <h3>My genus is:</h3>
                    <p>{obj.genus}</p>
             	</div>
                <div class="image">
                	<h3>This is me:</h3>
                	<img src='{obj.url}' width="550" height="400"/>
                </div>
                <div class="info">
                    <h3>My lifespan is:</h3>
                    <p>{obj.alifespan}</p>
                </div>
                <div class="info">
                    <h3>My habitat is:</h3>
                    <p>{obj.habitat}</p>
                </div>
                <div class="info">
                    <h3>You can find me:</h3>
                    <p>{obj.geolocation}</p>
                </div>
                <div class="info">
                    <h3>I say:</h3>
                    <p>{obj.sound}</p>
                </div>
    '''
        
        self.__foot= '''
            </div>
    </body>
</html>'''

#Returners
    def head(self):
        return self.__header

    def nav(self):
        return self.__nav
        
    def content(self,obj):
        content = self.__content.format(**locals())
        return content    

    def foot(self):
	    return self.__foot