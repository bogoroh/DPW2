class Page():
	def __init__(self):
		self.header ='''<!DOCTYPE>
<html>
    <head>
        <title>Welcome voter!</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" />
    </head>
    <body>
       '''   
		self.registration = form = '''
        <form method="GET" action="">
        	<label for="fName">First name:</label> <input type="text" name="fName" id="fName" />
        	<label for="lName">Last name:</label><input type="text" name="lName" id="lName"/>
			<select name="bday">
				<option value="na">Day</option>
				<option value="1">1</option>
				<option value="2">2</option>
				<option value="3">3</option>
				<option value="4">4</option>
				<option value="5">5</option>
				<option value="6">6</option>
				<option value="7">7</option>
				<option value="8">8</option>	
				<option value="9">9</option>
				<option value="10">10</option>
				<option value="11">11</option>
				<option value="12">12</option>	
				<option value="13">13</option>
				<option value="14">14</option>
				<option value="15">15</option>
				<option value="16">16</option>
				<option value="17">17</option>
				<option value="18">18</option>
				<option value="19">19</option>
				<option value="20">20</option>	
				<option value="21">21</option>
				<option value="22">22</option>
				<option value="23">23</option>
				<option value="24">24</option>	
				<option value="25">25</option>
				<option value="26">26</option>
				<option value="27">27</option>
				<option value="28">28</option>
				<option value="29">29</option>
				<option value="30">30</option>				  
				<option value="31">31</option>						  			  	  			  
			</select>         	
			<select name="bmonth">
				<option value="na">Month</option>
				<option value="jan">January</option>
				<option value="feb">Febrauary</option>
				<option value="march">March</option>
				<option value="april">April</option>
				<option value="may">May</option>
				<option value="june">June</option>
				<option value="july">July</option>
				<option value="august">August</option>	
				<option value="sept">September</option>
				<option value="oct">October</option>
				<option value="nov">November</option>
				<option value="dec">December</option>		  			  
			</select>
			<select name="byear">
				<option value="na">Year</option>
				<option value="2009">2009</option>
				<option value="2008">2008</option>
				<option value="2007">2007</option>
				<option value="2006">2006</option>
				<option value="2005">2005</option>
				<option value="2004">2004</option>
				<option value="2003">2003</option>
				<option value="2002">2002</option>
				<option value="2001">2001</option>
				<option value="2000">2000</option>
				<option value="1999">1999</option>
				<option value="1998">1998</option>
				<option value="1997">1997</option>
				<option value="1996">1996</option>
				<option value="1995">1995</option>
				<option value="1994">1994</option>
				<option value="1993">1993</option>
				<option value="1992">1992</option>
				<option value="1991">1991</option>
				<option value="1990">1990</option>
				<option value="1989">1989</option>
				<option value="1988">1988</option>
				<option value="1987">1987</option>
				<option value="1986">1986</option>
				<option value="1985">1985</option>
				<option value="1984">1984</option>
				<option value="1983">1983</option>
				<option value="1982">1982</option>
				<option value="1981">1981</option>
				<option value="1980">1980</option>
				<option value="1979">1979</option>
				<option value="1978">1978</option>
				<option value="1977">1977</option>
				<option value="1976">1976</option>
				<option value="1975">1975</option>
			</select> 
			<input type="radio" name="sex" value="male" id="male">
			<label for="male">Male</label>
			<input type="radio" name="sex" value="female" id="female">
			<label for="female">Female</label> 
        	
        	<label for="member">Select your members of the parlement(Up to 3 members)</label>
        	
			<div id="sites">
			    <input type="checkbox" name="site" id="koopa" value="koopatroop" /><label for="koopa"><img src="img/koopatroopa.png" alt="Koopa Troopa"/></label>
			    <input type="checkbox" name="site" id="larry" value="larry" /><label for="larry"><img src="img/larry.png" alt="Larry Troopa"  /></label>
			    <input type="checkbox" name="site" id="lemmy" value="lemmy" /><label for="lemmy"><img src="img/lemmy.png" alt="Lemmy Troopa"  /></label>
			    <input type="checkbox" name="site" id="ludwig" value="ludwig" /><label for="ludwig"><img src="img/ludwig.png" alt="Ludwig Troopa"  /></label>
			    <input type="checkbox" name="site" id="morton" value="morton" /><label for="morton"><img src="img/morton.png" alt="Morton Troopa"  /></label>
			</div>

        	
        	<input type="submit" value="submit" />
        </form>'''
		self.closer = '''
    </body>
</html>'''
	