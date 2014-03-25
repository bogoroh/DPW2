# Mike Taatgen
# DPW
# 01-20-14
# Animals assignement

class Page():
    def __init__(self):
        self.__header = '''
<!DOCTYPE>
<html>
    <head>
            <title>Mike Taatgen Lab 4</title>
            <link rel='stylesheet' href='css/main.css' />
</head>
    <body>
        <div id="wrapper">'''
        self.__nav='''
            <nav>
                <a href='/?animal=0'><button>Black Dolphins</button></a>
                <a href='/?animal=1'><button>Leopard Shark</button></a>
                <a href='/?animal=2'><button>Blue Marlin</button></a>
            </nav>'''
        self.__content='''
            <h1>I am called {obj.name}</h1>
                <div>
                    <h3>My phylum is:</h3>
                    <p>{obj.phylum}</p>
                </div>
                <div>
                    <h3>My class is:</h3>
                    <p>{obj.cclass}</p>
                </div>
                <div>
                    <h3>My order is:</h3>
                    <p>{obj.order}</p>
                </div>
                <div>
                    <h3>My family is:</h3>
                    <p>{obj.family}</p>
                </div>
                <div>
                    <h3>My genus is:</h3>
                    <p>{obj.genus}</p>
                </div>
                <div>
                	<img src='{obj.url}'/>
                </div>
                <div>
                    <h3>My lifespan is:</h3>
                    <p>{obj.alifespan}</p>
                </div>
                <div>
                    <h3>My habitat is:</h3>
                    <p>{obj.habitat}</p>
                </div>
                <div>
                    <h3>You can find me:</h3>
                    <p>{obj.geolocation}</p>
                </div>
                <div>
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