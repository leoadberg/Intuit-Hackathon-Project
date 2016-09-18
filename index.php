<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="index.css">
    <script src="Script.js"></script>
    <title>Home</title>
</head>

<body onload ="init();">

    <header>
        <hgroup>
            <h1>Jumbo Jobs</h1>
            <h2></h2>
            <h3>The future of your career </h3>
            <h3></h3>
        </hgroup>
        
        <nav>
            <ul>
           </ul>
        </nav>
        
    </header>
    
    <section class = "Inputs">
        <article>
            <p>
            Salary projection for college students using predictive model based on US Census data.
            Fill in your industry, state, income minimum and prefered company size.
            </p>
            
            <form id="form" name="form" method="get" action="index.php">
            
            <table>
            
            <colgroup>
           <col span="1" style="width: 50%;">
           <col span="1" style="width: 50%;">
        </colgroup>
            <tr valign="top"><th>
            <table>
                  <tr valign="top">
                    <th>
                        <p><h3>Industry</h3>
                        </p>
                   		<h4>Shift click to select multiple</h4>
                    </th>
                    <th> 
                    <select multiple style="width:100%;" name="industry[]">
                    <option value="54">Professional, Scientific, and Technical Services</option>
                    <option value="541110">*     Offices of Lawyers</option>
                    <option value="541330">*     Engineering Services</option>
                    <option value="541430">*     Graphic Design Services</option>
                    <option value="541511">*     Custom Computer Programming Services</option>
                    <option value="541512">*     Computer Systems Design Services</option>
                    <option value="541513">*     Computer Facilities Management Services</option>
                    <option value="61">Educational Services</option>
                    <option value="62">Health Care and Social Assistance</option>
                    <option value="71">Arts, Entertainment, and Recreation</option>
                    <option value="81">Other Services (except Public Administration)</option>
                    </select>
 
                   </th>
                  </tr>
                  <tr>
                    <td>
                        <p>
                        <h3>State</h3>
                        </p>
                    </td>
                    <td>
                <select multiple style="width:100%;" name="state[]">
                    <option value="Alabama">Alabama</option>
                    <option value="Alaska">Alaska</option>
                    <option value="Arizona">Arizona</option>
                    <option value="Arkansas">Arkansas</option>
                    <option value="California">California</option>
                    <option value="Colorado">Colorado</option>
                    <option value="Connecticut">Connecticut</option>
                    <option value="Delaware">Delaware</option>
                    <option value="District Of Columbia">District Of Columbia</option>
                    <option value="Florida">Florida</option>
                    <option value="Georgia">Georgia</option>
                    <option value="Hawaii">Hawaii</option>
                    <option value="Idaho">Idaho</option>
                    <option value="Illinois">Illinois</option>
                    <option value="Indiana">Indiana</option>
                    <option value="Iowa">Iowa</option>
                    <option value="Kansas">Kansas</option>
                    <option value="Kentucky">Kentucky</option>
                    <option value="Louisiana">Louisiana</option>
                    <option value="Maine">Maine</option>
                    <option value="Maryland">Maryland</option>
                    <option value="Massachusetts">Massachusetts</option>
                    <option value="Michigan">Michigan</option>
                    <option value="Minnesota">Minnesota</option>
                    <option value="Mississippi">Mississippi</option>
                    <option value="Missouri">Missouri</option>
                    <option value="Montana">Montana</option>
                    <option value="Nebraska">Nebraska</option>
                    <option value="Nevada">Nevada</option>
                    <option value="New Hampshire">New Hampshire</option>
                    <option value="New Jersey">New Jersey</option>
                    <option value="New Mexico">New Mexico</option>
                    <option value="New York">New York</option>
                    <option value="North Carolina">North Carolina</option>
                    <option value="North Dakota">North Dakota</option>
                    <option value="Ohio">Ohio</option>
                    <option value="Oklahoma">Oklahoma</option>
                    <option value="Oregon">Oregon</option>
                    <option value="Pennsylvania">Pennsylvania</option>
                    <option value="Rhode Island">Rhode Island</option>
                    <option value="South Carolina">South Carolina</option>
                    <option value="South Dakota">South Dakota</option>
                    <option value="Tennessee">Tennessee</option>
                    <option value="Texas">Texas</option>
                    <option value="Utah">Utah</option>
                    <option value="Vermont">Vermont</option>
                    <option value="Virginia">Virginia</option>
                    <option value="Washington">Washington</option>
                    <option value="West Virginia">West Virginia</option>
                    <option value="Wisconsin">Wisconsin</option>
                    <option value="Wyoming">Wyoming</option>
                </select>
                   </td>
                  </tr>
                  <tr>
                     <td>
                        <p>
                        <h3>Minimum Salary</h3>
                        </p>
                    </td>
                    <td>
                        <input name="minSalary" type="text" value="0">
                    </td>
                  </tr>
                  <tr>
                    <td>
                    </td>
                    <td>
                     <input type="submit" name="Submit" value="Submit"/>
                    </td>
                  </tr> 
                </table>
                </th>
               <th style="height:100%;" valign="top">
                <section style="height:100%; width:100%;" class = "Outputs">
                    <div style="height:100%; width:100%;" id="printoutput">Output: <br>
                    
                    <?php
putenv('PYTHONPATH=/home/leoadberg/leo.adberg.com/python/3.4.3/lib/python3.4/site-packages:');
					exec('source python/3.4.3/venv/python343/bin/activate');
                    $states = "";
                    $industries = "";
                    $minsalary = $_GET['minSalary'];
                    foreach ($_GET['state'] as $selectedOption) {
    					$states = $states . $selectedOption . " ";
					}
					
                    foreach ($_GET['industry'] as $selectedOption) {
    					$industries = $industries . $selectedOption . " ";
					}
                    $states = preg_replace("/[;\{\}\[\]]/", "", $states);
                    $industries = preg_replace("/[;\{\}\[\]]/", "", $industries);
                    $minsalary = preg_replace("/[;\{\}\[\]]/", "", $minsalary);
					$out = shell_exec('source python/3.4.3/venv/python343/bin/activate 2>&1;python GetData.py -state '.$states.' -NAICS '.$industries.' -minSalary '.$minsalary.' 2>&1');
echo $out;                    
?>
                    </div>
                </section>
                </th>
                </table>
                </form>
                 </article>
       </section>   
    <footer>
        <nav>
            <ul>
           </ul>
        </nav>
            
        <small>&copy; thanatcha amir leo alex</small>
    </footer>
</body>
</html>
